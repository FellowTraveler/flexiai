# routes/api.py
from flask import Blueprint, request, jsonify, session as flask_session
from flexiai import FlexiAI
from flexiai.config.logging_config import setup_logging
import uuid

api_bp = Blueprint('api', __name__)
flexiai = FlexiAI()

# setup_logging() # Check logs -> app.log file after you activate this

def message_to_dict(message):
    """
    Convert a message object to a dictionary, including nested TextContentBlock objects.
    """
    message_dict = {
        'id': message.id,
        'role': message.role,
        'content': [block.text.value for block in message.content if hasattr(block, 'text') and hasattr(block.text, 'value')]
    }
    return message_dict

@api_bp.route('/run', methods=['POST'])
def run():
    data = request.json
    user_message = data['message']
    assistant_id = 'asst_XXXXXXXXXXXXXXXXXXXXXXXX'  # Update with your assistant ID
    thread_id = data.get('thread_id')
    
    # Use a session ID if available, else create a new one
    session_id = flask_session.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())  # Generate a new session ID
        flask_session['session_id'] = session_id
        flexiai.session_manager.create_session(session_id, {"thread_id": thread_id, "seen_message_ids": []})
    else:
        session_data = flexiai.session_manager.get_session(session_id)
        thread_id = session_data.get("thread_id", thread_id)

    if not thread_id:
        thread = flexiai.create_thread()
        thread_id = thread.id
        flexiai.session_manager.create_session(session_id, {"thread_id": thread_id, "seen_message_ids": []})

    last_retrieved_id = None
    flexiai.create_advanced_run(assistant_id, thread_id, user_message)
    messages = flexiai.retrieve_messages_dynamically(thread_id, limit=20, retrieve_all=False, last_retrieved_id=last_retrieved_id)

    # Retrieve seen message IDs from the session
    session_data = flexiai.session_manager.get_session(session_id)
    seen_message_ids = set(session_data.get("seen_message_ids", []))

    filtered_messages = []
    new_seen_message_ids = list(seen_message_ids)  # Make a list for session update

    for msg in messages:
        if msg.id not in seen_message_ids:  # Access the id attribute directly
            filtered_messages.append({
                "role": "You" if msg.role == "user" else "Assistant",  # Access the role and content attributes directly
                "message": " ".join([block.text.value for block in msg.content if hasattr(block, 'text') and hasattr(block.text, 'value')])
            })
            new_seen_message_ids.append(msg.id)
    
    # Update session with new seen message IDs
    flexiai.session_manager.create_session(session_id, {"thread_id": thread_id, "seen_message_ids": new_seen_message_ids})

    return jsonify(success=True, thread_id=thread_id, messages=filtered_messages)

@api_bp.route('/thread/<thread_id>/messages', methods=['GET'])
def get_thread_messages(thread_id):
    session_id = flask_session.get('session_id')
    if not session_id:
        return jsonify(success=False, message="Session not found"), 404

    messages = flexiai.retrieve_messages(thread_id, limit=20)
    formatted_messages = [
        {
            "role": "You" if msg.role == "user" else "Assistant",  # Access the role and content attributes directly
            "message": " ".join([block.text.value for block in msg.content if hasattr(block, 'text') and hasattr(block.text, 'value')])
        }
        for msg in messages
    ]
    return jsonify(success=True, thread_id=thread_id, messages=formatted_messages)

# Session management routes
@api_bp.route('/session', methods=['POST'])
def create_session():
    data = request.json
    session_id = data['session_id']
    session_data = data['data']
    session = flexiai.session_manager.create_session(session_id, session_data)
    return jsonify(success=True, session=session)

@api_bp.route('/session/<session_id>', methods=['GET'])
def get_session(session_id):
    try:
        session_data = flexiai.session_manager.get_session(session_id)
        return jsonify(success=True, session=session_data)
    except KeyError:
        return jsonify(success=False, message="Session not found"), 404

@api_bp.route('/session/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    success = flexiai.session_manager.delete_session(session_id)
    return jsonify(success=success)

@api_bp.route('/sessions', methods=['GET'])
def get_all_sessions():
    sessions = flexiai.session_manager.get_all_sessions()
    return jsonify(success=True, sessions=sessions)

@api_bp.route('/sessions', methods=['DELETE'])
def clear_all_sessions():
    success = flexiai.session_manager.clear_all_sessions()
    return jsonify(success=success)
