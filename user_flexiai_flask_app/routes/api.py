# routes/api.py
import uuid
from flexiai import FlexiAI
from flask import Blueprint, request, jsonify, session as flask_session
from utils.markdown_converter import convert_markdown_to_html


# Create a Blueprint for the API routes
api_bp = Blueprint('api', __name__)
flexiai = FlexiAI()


def message_to_dict(message):
    """
    Convert a message object to a dictionary, including nested TextContentBlock objects.
    
    Args:
        message (object): The message object to convert.
    
    Returns:
        dict: The converted message dictionary.
    """
    message_dict = {
        'id': message.id,
        'role': message.role,
        'content': [block.text.value for block in message.content if hasattr(block, 'text') and hasattr(block.text, 'value')]
    }
    return message_dict


@api_bp.route('/run', methods=['POST'])
def run():
    """
    Route to handle running the assistant with the user's message.
    
    Retrieves the user's message from the request, manages session and thread IDs,
    sends the message to the assistant, retrieves the responses, converts them to HTML,
    and returns the responses as JSON.
    
    Returns:
        Response: JSON response containing success status, thread ID, and messages.
    """
    data = request.json
    user_message = data['message']
    assistant_id = 'asst_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Update with your Assistant ID
    thread_id = data.get('thread_id')

    session_id = flask_session.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        flask_session['session_id'] = session_id
        flexiai.session_manager.create_session(session_id, {"thread_id": thread_id, "seen_message_ids": []})
    else:
        session_data = flexiai.session_manager.get_session(session_id)
        thread_id = session_data.get("thread_id", thread_id)

    if not thread_id:
        thread_id = flexiai.multi_agent_system.thread_initialization(assistant_id)
        flexiai.session_manager.create_session(session_id, {"thread_id": thread_id, "seen_message_ids": []})

    last_retrieved_id = None
    flexiai.create_advanced_run(assistant_id, thread_id, user_message)
    messages = flexiai.retrieve_messages_dynamically(thread_id, limit=20, retrieve_all=False, last_retrieved_id=last_retrieved_id)

    session_data = flexiai.session_manager.get_session(session_id)
    seen_message_ids = set(session_data.get("seen_message_ids", []))

    filtered_messages = []
    new_seen_message_ids = list(seen_message_ids)

    for msg in messages:
        if msg.id not in seen_message_ids:
            content = " ".join([block.text.value for block in msg.content if hasattr(block, 'text') and hasattr(block.text, 'value')])
            html_content = convert_markdown_to_html(content)
            filtered_messages.append({
                "role": "You" if msg.role == "user" else "Assistant",
                "message": html_content
            })
            new_seen_message_ids.append(msg.id)

    flexiai.session_manager.create_session(session_id, {"thread_id": thread_id, "seen_message_ids": new_seen_message_ids})

    response_data = {
        'success': True,
        'thread_id': thread_id,
        'messages': filtered_messages
    }

    flexiai.logger.debug(f"Sending response data: {response_data}")
    return jsonify(response_data)
