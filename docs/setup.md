# Setup Guide

This guide will help you set up FlexiAI in your project, including installation steps, virtual environment creation, and post-installation setup.

### Table of Contents

- [Installation](#installation)
  - [Create a Virtual Environment](#create-a-virtual-environment)
    - [Using PowerShell](#using-powershell)
    - [Using Conda](#using-conda)
  - [Install FlexiAI](#install-flexiai-with-pip)
  - [Post-Installation Setup](#post-installation-setup)
    - [Enable Retrieval-Augmented Generation (RAG)](#enable-retrieval-augmented-generation-rag)
    - [FlexiAI Basic Flask Chat Application](#flexiai-basic-flask-chat-application)
- [Environment Setup](#environment-setup)
  - [Example .env File](#example-env-file)

---

## Installation

### Create a Virtual Environment

Creating a virtual environment helps manage dependencies and avoid conflicts. Choose either PowerShell or Conda to create your virtual environment.

#### Using PowerShell

```powershell
python -m venv .flexi_env
source .flexi_env/bin/activate
```

#### Using Conda

```powershell
conda create --name flexi_env python=3.12.4
conda activate flexi_env
```

### Install FlexiAI with pip

To install the FlexiAI framework using pip, run:

```powershell
pip install flexiai
```

### Post-Installation Setup

After installing, copy the `flexiai_rag_extension.py` and `flexiai_basic_flask_app.py` files to your project root directory and run them manually to set up additional necessary directories and files.

- [Download flexiai_rag_extension.py](https://github.com/SavinRazvan/flexiai/blob/main/post_install/flexiai_rag_extension.py): This script sets up the necessary structure and files for enabling Retrieval-Augmented Generation (RAG) capabilities in your FlexiAI project.
- [Download flexiai_basic_flask_app.py](https://github.com/SavinRazvan/flexiai/blob/main/post_install/flexiai_basic_flask_app.py): This script creates a basic Flask application structure, including routes, static files, templates, and main application files, to facilitate running a web server for your FlexiAI project.

#### Or create new files `flexiai_rag_extension.py` and `flexiai_basic_flask_app.py` in the root directory of your project.

<details>
<summary> ⬇️ Expand to see the code for `flexiai_rag_extension.py` ⬇️ </summary>

```python
# flexiai_rag_extension.py
import os

def create_logs_folder(project_root):
    log_folder = os.path.join(project_root, 'logs')
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
        print(f"Created directory: {log_folder}")

def create_user_flexiai_rag_folder(project_root):
    dst_folder = os.path.join(project_root, 'user_flexiai_rag')
    data_folder = os.path.join(dst_folder, 'data')

    # List of subdirectories to create inside 'data'
    data_subfolders = ['audio', 'corpus', 'csv', 'images', 'vectors_store']

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f"Created directory: {data_folder}")
    
    # Create the subdirectories under 'data'
    for subfolder in data_subfolders:
        subfolder_path = os.path.join(data_folder, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            print(f"Created directory: {subfolder_path}")
    
    files_content = {
        '__init__.py': "# user_flexiai_rag/__init__.py\n",
        'user_function_mapping.py': '''# user_flexiai_rag/user_function_mapping.py
import logging
from user_flexiai_rag.user_task_manager import UserTaskManager

logger = logging.getLogger(__name__)

def register_user_tasks(multi_agent_system, run_manager):
    """
    Registers user-defined tasks with the FlexiAI framework.

    This function initializes the UserTaskManager and sets up mappings for personal and assistant functions.
    It logs the registration process and returns the function mappings.

    Args:
        multi_agent_system (MultiAgentSystemManager): The multi-agent system manager instance.
        run_manager (RunManager): The run manager instance.

    Returns:
        tuple: A tuple containing two dictionaries:
            - user_personal_functions (dict): Mapping of personal function names to their implementations.
            - user_assistant_functions (dict): Mapping of assistant function names to their implementations.
    """
    task_manager = UserTaskManager(multi_agent_system, run_manager)

    user_personal_functions = {
        # MAS functions for each agent:
        'save_processed_content': task_manager.save_processed_content,
        'load_processed_content': task_manager.load_processed_content,
        'initialize_agent': task_manager.initialize_agent,
        # Functions used by your assistants
        'search_youtube': task_manager.search_youtube,
    }

    user_assistant_functions = {
       'communicate_with_assistant': task_manager.continue_conversation_with_assistant,
       # Other designs for MAS or other assistants
    }

    logger.info("Registering user tasks")
    logger.debug(f"User personal functions: {list(user_personal_functions.keys())}")
    logger.debug(f"User assistant functions: {list(user_assistant_functions.keys())}")

    return user_personal_functions, user_assistant_functions
''',
        'user_helpers.py': "# user_flexiai_rag/user_helpers.py\n",
        'user_task_manager.py': '''# user_flexiai_rag/user_task_manager.py
import logging
import urllib.parse
import subprocess
from threading import Lock
from flexiai.core.flexi_managers.run_manager import RunManager
from flexiai.core.flexi_managers.thread_manager import ThreadManager
from flexiai.core.flexi_managers.message_manager import MessageManager
from flexiai.core.flexi_managers.multi_agent_system import MultiAgentSystemManager


class UserTaskManager:
    """
    UserTaskManager class handles user-defined tasks for AI assistants, enabling 
    Retrieval-Augmented Generation (RAG) capabilities and interaction within the 
    Multi-Agent System.

    This class provides methods to save and load processed content, continue conversations 
    with assistants, initialize agents, and perform specific tasks such as YouTube searches.
    """

    def __init__(self, multi_agent_system: MultiAgentSystemManager, run_manager: RunManager):
        """
        Initializes the UserTaskManager instance, setting up the logger and a lock for thread safety.

        Args:
            multi_agent_system (MultiAgentSystemManager): The multi-agent system manager instance.
            run_manager (RunManager): The run manager instance.
        """
        self.logger = logging.getLogger(__name__)
        self.lock = Lock()
        self.multi_agent_system = multi_agent_system
        self.run_manager = run_manager
        self.message_manager = multi_agent_system.message_manager


    def log_function_call(self, func_name, params=None):
        """
        Logs the function call.
        
        Args:
            func_name (str): The name of the function being called.
            params (dict, optional): Parameters passed to the function.
        """
        param_str = f" with params: {params}" if params else ""
        self.logger.info(f"Function called: {func_name}{param_str}")


    def save_processed_content(self, from_assistant_id, to_assistant_id, processed_content):
        """
        Saves the processed user content for RAG purposes, allowing AI assistants to 
        store and retrieve contextual information.

        Args:
            from_assistant_id (str): The assistant identifier from which the content originates.
            to_assistant_id (str): The assistant identifier to which the content is directed.
            processed_content (str): The processed content to store.

        Returns:
            bool: True if content is saved successfully, False otherwise.
        """
        return self.multi_agent_system.save_processed_content(from_assistant_id, to_assistant_id, processed_content)


    def load_processed_content(self, from_assistant_id, to_assistant_id, multiple_retrieval):
        """
        Loads the stored processed user content, enabling AI assistants to access 
        previously stored information for enhanced context and continuity in RAG.

        Args:
            from_assistant_id (str): The assistant identifier from which the content originates.
            to_assistant_id (str): The assistant identifier to which the content is directed.
            multiple_retrieval (bool): Whether to retrieve content from all sources, not just the specified to_assistant_id.

        Returns:
            list: A list of stored user content if found, otherwise an empty list.
        """
        return self.multi_agent_system.load_processed_content(from_assistant_id, to_assistant_id, multiple_retrieval)


    def continue_conversation_with_assistant(self, assistant_id, user_content):
        """
        Continues the conversation with an assistant by submitting user content 
        and managing the resulting run, allowing dynamic and contextually aware interactions.

        Args:
            assistant_id (str): The unique identifier for the assistant.
            user_content (str): The content submitted by the user.

        Returns:
            tuple: A tuple containing a success status, a message detailing the outcome, and the processed content.
        """
        return self.multi_agent_system.continue_conversation_with_assistant(assistant_id, user_content)


    def initialize_agent(self, assistant_id):
        """
        Initializes an agent for the given assistant ID. If a thread already exists for the assistant ID,
        it returns a message indicating the existing thread. Otherwise, it creates a new thread and returns
        a message indicating successful initialization.

        Args:
            assistant_id (str): The unique identifier for the assistant.

        Returns:
            str: A message indicating the result of the initialization.
        """
        return self.multi_agent_system.initialize_agent(assistant_id)


    def search_youtube(self, query):
        """
        Searches YouTube for the given query and opens the search results page
        in the default web browser. This function demonstrates integration with 
        external services as part of RAG capabilities.

        Args:
            query (str): The search query string.

        Returns:
            dict: A dictionary containing the status, message, and result (URL)
        """
        self.log_function_call('search_youtube', {'query': query})

        if not query:
            return {
                "status": False,
                "message": "Query cannot be empty.",
                "result": None
            }

        try:
            # Normalize spaces to ensure consistent encoding
            query_normalized = query.replace(" ", "+")
            query_encoded = urllib.parse.quote(query_normalized)
            youtube_search_url = (
                f"https://www.youtube.com/results?search_query={query_encoded}"
            )
            self.logger.info(f"Opening YouTube search for query: {query}")

            # Use PowerShell to open the URL
            subprocess.run(
                ['powershell.exe', '-Command', 'Start-Process', youtube_search_url],
                check=True
            )
            self.logger.info("YouTube search page opened successfully.")
            return {
                "status": True,
                "message": "YouTube search page opened successfully.",
                "result": youtube_search_url
            }
        except subprocess.CalledProcessError as e:
            error_message = f"Subprocess error: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }
        except Exception as e:
            error_message = f"Failed to open YouTube search for query: {query}. Error: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }

    # Here you will add your other functions used by your Assistant/s (personal functions or 
    # calling other assistants functions -> those names must end with 'assistant)'
''',
    }
    
    for filename, content in files_content.items():
        file_path = os.path.join(dst_folder, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")

def create_env_file(project_root):
    env_file = os.path.join(project_root, '.env')
    if not os.path.exists(env_file):
        with open(env_file, 'w') as f:
            f.write(
                "# ============================================================================================ #\n"
                "#                                      OpenAI Configuration                                    #\n"
                "# ============================================================================================ #\n"
                "# Replace 'your_openai_api_key_here' with your actual OpenAI API key.\n"
                "OPENAI_API_KEY=your_openai_api_key_here\n\n"
                "# Replace 'your_openai_api_version_here' with your actual OpenAI API version.\n"
                "# Example for OpenAI: 2020-11-07\n"
                "OPENAI_API_VERSION=your_openai_api_version_here\n\n"
                "# Replace 'your_openai_organization_id_here' with your actual OpenAI Organization ID.\n"
                "OPENAI_ORGANIZATION_ID=your_openai_organization_id_here\n\n"
                "# Replace 'your_openai_project_id_here' with your actual OpenAI Project ID.\n"
                "OPENAI_PROJECT_ID=your_openai_project_id_here\n\n"
                "# Replace 'your_openai_assistant_version_here' with your actual OpenAI Assistant version.\n"
                "# Example for Assistant: v1 or v2\n"
                "OPENAI_ASSISTANT_VERSION=your_openai_assistant_version_here\n\n\n"
                "# ============================================================================================ #\n"
                "#                                      Azure OpenAI Configuration                              #\n"
                "# ============================================================================================ #\n"
                "# Replace 'your_azure_openai_api_key_here' with your actual Azure OpenAI API key.\n"
                "AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here\n\n"
                "# Replace 'your_azure_openai_endpoint_here' with your actual Azure OpenAI endpoint.\n"
                "AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here\n\n"
                "# Replace 'your_azure_openai_api_version_here' with your actual Azure OpenAI API version.\n"
                "# Example for Azure: 2024-05-01-preview\n"
                "AZURE_OPENAI_API_VERSION=your_azure_openai_api_version_here\n\n\n"
                "# ============================================================================================ #\n"
                "#                                      General Configuration                                   #\n"
                "# ============================================================================================ #\n"
                "# Set this to 'openai' if you are using OpenAI, or 'azure' if you are using Azure OpenAI.\n"
                "CREDENTIAL_TYPE=openai\n\n"
            )
        print(f"Created file: {env_file}")

def create_requirements_file(project_root):
    requirements_file = os.path.join(project_root, 'requirements.txt')
    if not os.path.exists(requirements_file):
        with open(requirements_file, 'w') as f:
            f.write(
                "annotated-types==0.7.0\n"
                "anyio==4.4.0\n"
                "azure-common==1.1.28\n"
                "azure-core==1.30.2\n"
                "azure-identity==1.17.1\n"
                "azure-mgmt-core==1.4.0\n"
                "azure-mgmt-resource==23.1.1\n"
                "bleach==6.1.0\n"
                "build==1.2.1\n"
                "certifi==2024.7.4\n"
                "cffi==1.16.0\n"
                "charset-normalizer==3.3.2\n"
                "click==8.1.7\n"
                "cryptography==43.0.0\n"
                "distro==1.9.0\n"
                "docutils==0.21.2\n"
                "Flask==3.0.3\n"
                "glob2==0.7\n"
                "h11==0.14.0\n"
                "httpcore==1.0.5\n"
                "httpx==0.27.0\n"
                "idna==3.7\n"
                "importlib_metadata==8.2.0\n"
                "iniconfig==2.0.0\n"
                "isodate==0.6.1\n"
                "itsdangerous==2.2.0\n"
                "jaraco.classes==3.4.0\n"
                "jaraco.context==5.3.0\n"
                "jaraco.functools==4.0.1\n"
                "jeepney==0.8.0\n"
                "Jinja2==3.1.4\n"
                "keyring==25.2.1\n"
                "markdown-it-py==3.0.0\n"
                "MarkupSafe==2.1.5\n"
                "mdurl==0.1.2\n"
                "more-itertools==10.3.0\n"
                "msal==1.30.0\n"
                "msal-extensions==1.2.0\n"
                "nest-asyncio==1.6.0\n"
                "nh3==0.2.18\n"
                "numpy==1.26.4\n"
                "nltk==3.8.1\n"
                "faiss-cpu==1.8.0\n"
                "openai==1.40.2\n"
                "packaging==24.1\n"
                "pillow==10.4.0\n"
                "pip-upgrade-outdated==1.5\n"
                "pkginfo==1.10.0\n"
                "platformdirs==3.7.0\n"
                "pluggy==1.5.0\n"
                "portalocker==2.10.1\n"
                "pycparser==2.22\n"
                "pydantic==2.7.4\n"
                "pydantic-settings==2.3.3\n"
                "pydantic_core==2.18.4\n"
                "Pygments==2.18.0\n"
                "PyJWT==2.8.0\n"
                "pyproject_hooks==1.1.0\n"
                "pytest==8.3.1\n"
                "python-dotenv==1.0.1\n"
                "readme_renderer==44.0\n"
                "requests==2.32.3\n"
                "requests-toolbelt==1.0.0\n"
                "rfc3986==2.0.0\n"
                "rich==13.7.1\n"
                "SecretStorage==3.3.3\n"
                "setuptools==69.5.1\n"
                "six==1.16.0\n"
                "sniffio==1.3.1\n"
                "soupsieve==2.5\n"
                "tinycss2==1.3.0\n"
                "tqdm==4.66.4\n"
                "typing_extensions==4.12.2\n"
                "urllib3==2.2.2\n"
                "webencodings==0.5.1\n"
                "Werkzeug==3.0.3\n"
                "zipp==3.19.2\n"
            )
        print(f"Created file: {requirements_file}")

if __name__ == '__main__':
    project_root = os.getcwd()

    try:
        create_logs_folder(project_root)
        create_user_flexiai_rag_folder(project_root)
        create_env_file(project_root)
        create_requirements_file(project_root)
    except Exception as e:
        print(f"Post-installation step failed: {e}")

```

</details>

<details>
<summary> ⬇️ Expand to see the code for `flexiai_basic_flask_app.py` ⬇️ </summary>

```python
# flexiai_basic_flask_app.py
import os

def create_folder_structure(project_root):
    folder_structure = {
        'logs': [],
        'routes': ['api.py'],
        'static/css': ['styles.css'],
        'static/images': [],
        'static/js': ['scripts.js'],
        'templates': ['index.html'],
        'utils': ['markdown_converter.py']
    }
    
    for folder, files in folder_structure.items():
        folder_path = os.path.join(project_root, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created directory: {folder_path}")
        
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write('')
                print(f"Created file: {file_path}")

def write_file_content(project_root):
    files_content = {
        'routes/api.py': '''import uuid
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
    assistant_id = 'asst_XXXXXXXXXXXXXXXXXXXXXXXXXX'  # Update with your assistant ID
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
''',

        'static/css/styles.css': '''/* Base Styles */
body {
    font-family: 'Open Sans', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #535353;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    height: 100vh;
}

/* Chat Container */
#chat-container {
    width: 100%;
    max-width: 680px;
    height: calc(100vh - 2rem);
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    border-radius: 8px;
    margin: 1rem 0;
    overflow: hidden;
}

/* Links */
a {
    color: #89e600;
}

/* Messages Container */
#messages {
    padding: 1rem;
    flex: 1;
    overflow-y: auto;
    margin: 0;
    color: #e1e1e6;
}

/* Message Item */
.message {
    padding: 0.5rem 0;
    margin: 0.5rem 0;
    border-radius: 4px;
    word-wrap: break-word;
    display: flex;
    align-items: flex-start;
    animation: fadeIn 0.5s ease-in-out;
}

/* Animation for messages */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Message Container */
.message-container {
    display: flex;
    align-items: flex-start;
    width: 100%;
}

/* Avatar */
.avatar {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background-color: #25272a;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
    font-size: 1.2em;
    color: #ffffff;
    border: 1px solid #c6c6c6;
    overflow: hidden;
}

/* Avatar Images */
.avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
}

/* Message Content */
.message-content {
    flex: 1;
    padding: 0.5rem 0.9rem;
    border-radius: 20px;
    font-size: 0.7em;
    line-height: 1.5rem;
    background-color: #3a3f4b;
    color: #e1e1e6;
    position: relative;
    word-break: break-word;
    overflow: hidden;
}

/* User Message */
.user .message-content {
    background-color: #3a3a3a;
    text-align: left;
    color: #e1e1e6;
}

/* Assistant Message */
.assistant .message-content {
    background-color: #404a63;
    text-align: left;
}

/* Error Message */
.error .message-content {
    background-color: #ff4c4c;
    text-align: center;
    color: #fff;
}

/* Input Container */
#input-container {
    display: flex;
    align-items: center;
    padding: 0.75rem 1rem;
    border-top: 1px solid #353940;
    background-color: #ffffff;
    position: relative;
}

/* Message Input */
#message-input {
    width: 91%;
    height: 40px;
    max-height: calc(1.5rem * 10);
    padding: 0.75rem;
    border: 1px solid #484e5c;
    border-radius: 20px;
    margin-right: 0.5rem;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
    transition: border-color 0.3s;
    background-color: #3a3a3a;
    color: #e1e1e6;
    resize: none;
    overflow-y: hidden;
    box-sizing: border-box;
    font-family: 'Open Sans', sans-serif;
    font-size: 1rem;
    line-height: 1.5rem;
}

#message-input:focus {
    border-color: #5a5a5a;
    outline: none;
}

/* Send Button */
#send-button {
    width: 44px;
    height: 44px;
    border: none;
    border-radius: 50%;
    background-color: #404a63;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.1s;
    position: absolute;
    right: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}
#send-button::before {
    content: '';
    display: block;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 12px solid white;
    transition: transform 0.3s;
}
#send-button:hover::before {
    animation: bounce 0.3s infinite alternate;
}
#send-button:hover {
    background-color: #2a3552;
}
#send-button:active {
    transform: scale(0.95);
}

@keyframes bounce {
    from {
        transform: translateY(0);
    }
    to {
        transform: translateY(-3px);
    }
}

/* Markdown Content */
.markdown-content {
    font-size: 1rem;
    line-height: 1.5rem;
    margin: 0;
    word-break: break-word;
}

.markdown-content h1, .markdown-content h2, .markdown-content h3 {
    border-bottom: 1px solid #444;
    padding-bottom: 0.3em;
    margin-top: 0.5em;
    font-size: 1.2em;
    color: #ffffff;
}

.markdown-content p {
    margin: 0.5em 0;
}

.markdown-content code {
    background-color: #2e2e2e;
    border-radius: 3px;
    padding: 0.2em 0.4em;
    color: #e1e1e6;
}

.markdown-content pre {
    background-color: #2e2e2e;
    padding: 6px;
    border-radius: 3px;
    overflow-x: auto;
    font-size: 0.95em;
    color: #e1e1e6;
    position: relative;
}

.markdown-content ol, .markdown-content ul {
    margin-left: 1em;
    padding-left: 0.5em;
    list-style-position: outside !important;
}

.markdown-content ol {
    list-style-type: decimal !important;
}

.markdown-content ul {
    list-style-type: disc !important;
}

.markdown-content li {
    list-style: inherit !important;
    margin: 0.5em 0;
}

.markdown-content blockquote {
    border-left: 4px solid #ccc;
    padding-left: 1em;
    margin-left: 0;
    color: #666;
}

.markdown-content a {
    color: #89e600;
    text-decoration: none;
}

.markdown-content a:hover {
    text-decoration: underline;
}

/* Headers in Messages */
.message-content h3 {
    margin: 0;
    padding: 0.5rem 0;
    font-size: 1rem;
    font-weight: bold;
    color: #ffffff;
}

/* Markdown Headers */
.markdown-content h1,
.markdown-content h2,
.markdown-content h3 {
    border-bottom: 1px solid #444;
    padding-bottom: 0.3em;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
    font-size: 1.2em;
    color: #ffffff;
}

/* Responsive Design */
@media (max-width: 600px) {
    #chat-container {
        height: calc(100vh - 2rem);
    }
    #message-input {
        padding: 0.75rem;
    }
    #send-button {
        padding: 0.75rem;
        width: 40px;
        height: 40px;
    }
    .avatar {
        width: 30px;
        height: 30px;
        font-size: 1em;
    }
    .message-content {
        font-size: 0.7em;
        padding: 0.5rem 0.9rem;
    }
    .markdown-content {
        font-size: 0.85em;
    }
}

.copy-code-button {
    background-color: #373737;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    position: absolute;
    top: 5px;
    right: 5px;
    border-radius: 2px;
}

.copy-code-button:hover {
    background-color: #333131;
}

pre.sourceCode {
    position: relative;
}''',

        'static/js/scripts.js': '''// static/js/scripts.js
let threadId = null;
let isProcessing = false;

document.getElementById('send-button').addEventListener('click', sendMessage);

const messageInput = document.getElementById('message-input');
messageInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && event.shiftKey) {
        const cursorPosition = this.selectionStart;
        const value = this.value;
        this.value = value.substring(0, cursorPosition) + "\\n" + value.substring(cursorPosition);
        this.selectionStart = cursorPosition + 1;
        this.selectionEnd = cursorPosition + 1;
        event.preventDefault();
    } else if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
    autoResizeTextarea();
});

messageInput.addEventListener('input', autoResizeTextarea);

function autoResizeTextarea() {
    const maxRows = 10;
    const lineHeight = parseInt(window.getComputedStyle(messageInput).lineHeight);
    messageInput.style.height = '40px'; // Reset height to calculate new height
    const currentHeight = messageInput.scrollHeight;

    if (currentHeight > lineHeight * maxRows) {
        messageInput.style.height = (lineHeight * maxRows) + 'px';
        messageInput.style.overflowY = 'scroll';
    } else {
        messageInput.style.height = currentHeight + 'px';
        messageInput.style.overflowY = 'hidden';
    }
}

autoResizeTextarea();

function sendMessage() {
    const message = messageInput.value.trim();

    if (message === '') {
        alert('Message cannot be empty or whitespace.');
        return;
    }

    if (isProcessing) {
        alert('Please wait for the assistant to respond before sending a new message.');
        return;
    }

    addMessage('You', message, 'user', true);

    messageInput.value = '';
    autoResizeTextarea();

    isProcessing = true;

    fetch('/api/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message, thread_id: threadId })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // console.log('Received data from backend:', data);
        if (data.success) {
            threadId = data.thread_id;
            updateChat(data.messages).then(() => {
                isProcessing = false;
                addCopyButtons();
                if (typeof MathJax !== 'undefined') {
                    MathJax.typesetPromise();  // Re-render MathJax after updating the chat
                } else {
                    console.error('MathJax is not loaded.');
                }
            });
        } else {
            addMessage('Error', 'Failed to get response from assistant.', 'error');
            isProcessing = false;
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
        addMessage('Error', 'An error occurred: ' + error.message, 'error');
        isProcessing = false;
    });
}

function addMessage(role, text, className, isUserMessage = false) {
    // console.log('Adding message:', { role, text, className, isUserMessage });
    const messageElement = document.createElement('div');
    messageElement.className = `message ${className}`;

    const avatar = role === 'You' ? '/static/images/user.png' : '/static/images/assistant.png';

    const formattedText = isUserMessage ? text.replace(/\\n/g, '<br>') : text;

    try {
        const htmlContent = window.marked.parse(formattedText);
        // console.log('HTML content after marked parsing:', htmlContent);
        messageElement.innerHTML = `
            <div class="message-container">
                <div class="avatar"><img src="${avatar}" alt="${role}"></div>
                <div class="message-content">
                    <div class="markdown-content">${htmlContent}</div>
                </div>
            </div>`;
    } catch (error) {
        console.error('Markdown conversion error:', error);
        messageElement.innerHTML = `
            <div class="message-container">
                <div class="avatar"><img src="${avatar}" alt="${role}"></div>
                <div class="message-content">
                    <div class="markdown-content">${formattedText}</div>
                </div>
            </div>`;
    }

    const messagesContainer = document.getElementById('messages');
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    if (typeof MathJax !== 'undefined') {
        MathJax.typesetPromise();  // Re-render MathJax after adding the new message
    } else {
        console.error('MathJax is not loaded.');
    }
}

function updateChat(messages) {
    return new Promise((resolve) => {
        messages.forEach(msg => {
            // console.log('Updating chat with message:', msg);
            if (msg.role === 'Assistant') {
                addMessage('Assistant', msg.message, 'assistant');
            }
        });
        resolve();
    });
}

function addCopyButtons() {
    document.querySelectorAll('pre code').forEach((block) => {
        if (block.parentNode.querySelector('.copy-code-button')) {
            return;
        }
        const copyButton = document.createElement('button');
        copyButton.innerText = 'Copy';
        copyButton.className = 'copy-code-button';
        copyButton.addEventListener('click', () => {
            navigator.clipboard.writeText(block.innerText).then(() => {
                copyButton.innerText = 'Copied!';
                setTimeout(() => {
                    copyButton.innerText = 'Copy';
                }, 2000);
            });
        });
        const pre = block.parentNode;
        pre.style.position = 'relative';
        pre.insertBefore(copyButton, block);
    });
}
''',

        'templates/index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlexiAI Chat Application</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <div id="chat-container">
        <div id="messages"></div>
        <div id="input-container">
            <textarea id="message-input" placeholder="Type your message here..."></textarea>
            <button id="send-button"></button>
        </div>
    </div>
    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
</body>
</html>
''',

        'utils/markdown_converter.py': '''# utils/markdown_converter.py
import subprocess
import logging


# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def preprocess_markdown(markdown_text):
    """
    Preprocess markdown text to ensure LaTeX formulas are correctly formatted for Pandoc.

    Args:
        markdown_text (str): The markdown text to preprocess.

    Returns:
        str: The preprocessed markdown text.
    """
    # Ensure LaTeX formulas are correctly formatted
    preprocessed_text = markdown_text.replace("\\[", "$$").replace("\\]", "$$")
    return preprocessed_text


def convert_markdown_to_html(markdown_text):
    """
    Convert markdown text to HTML using the Pandoc tool and ensure the output is properly handled.

    Args:
        markdown_text (str): The markdown text to convert.

    Returns:
        str: The converted HTML text. If conversion fails, returns the original markdown text.
    """
    # logger.debug(f"Converting markdown text: {markdown_text}")
    try:
        # Preprocess markdown to ensure LaTeX formulas are recognized
        preprocessed_text = preprocess_markdown(markdown_text)
        # logger.debug(f"Preprocessed markdown text: {preprocessed_text}")

        # Execute the Pandoc command to convert markdown to HTML with LaTeX support
        process = subprocess.Popen(['pandoc', '-f', 'markdown', '-t', 'html', '--mathjax'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=preprocessed_text.encode('utf-8'))

        # Check if the Pandoc command executed successfully
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, stderr.decode('utf-8'))

        # Decode the output from bytes to string
        html_output = stdout.decode('utf-8')
        # logger.debug(f"Pandoc conversion output: {html_output}")

        return html_output
    except subprocess.CalledProcessError as e:
        logger.error(f"Pandoc conversion failed: {e}")
        return markdown_text
    except Exception as e:
        logger.error(f"Error converting markdown to HTML: {e}")
        return markdown_text
''',

        'app.py': '''import os
import logging
from flask import Flask, session, render_template
from datetime import timedelta
from routes.api import api_bp
from flexiai import FlexiAI
from flexiai.config.logging_config import setup_logging


# Initialize application-specific logging
setup_logging(
    root_level=logging.INFO,
    file_level=logging.INFO,
    console_level=logging.INFO,
    enable_file_logging=True,       # Set to False to disable file logging
    enable_console_logging=True     # Set to False to disable console logging
)

# Initialize Flask application with static and template folders
app = Flask(__name__, static_folder='static', template_folder='templates')

# Secure the session with a secret key
app.secret_key = os.urandom(24)

# Set session cookie attributes
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # or 'Strict'

# Register the API blueprint with a URL prefix
app.register_blueprint(api_bp, url_prefix='/api')

# Initialize FlexiAI instance
flexiai = FlexiAI()


@app.before_request
def before_request():
    """
    Function to run before each request to ensure sessions are permanent
    and set the session lifetime to 60 minutes.
    """
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)


@app.route('/')
def index():
    """
    Route for the index page, rendering the index.html template.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Configure the root logger to log at INFO level
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Clear existing handlers from the root logger to prevent duplicate logs
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Configure specific loggers to log at INFO level
    loggers = ['werkzeug', 'httpx', 'flexiai', 'user_function_mapping']
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        if logger.hasHandlers():
            logger.handlers.clear()

    # Add console handler to the root logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    root_logger.addHandler(console_handler)

    # Run the Flask application on host 127.0.0.1 and port 5000
    app.run(host='127.0.0.1', port=5000, debug=False)
'''
    }
    
    for relative_path, content in files_content.items():
        file_path = os.path.join(project_root, relative_path)
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Written content to: {file_path}")

if __name__ == '__main__':
    project_root = os.getcwd()

    try:
        create_folder_structure(project_root)
        write_file_content(project_root)
    except Exception as e:
        print(f"Post-installation step failed: {e}")


```

</details>

### Enable Retrieval-Augmented Generation (RAG)

Running the `flexiai_rag_extension.py` script will automatically create the necessary structure and files to enable the Retrieval-Augmented Generation (RAG) module in your project.

Here's an overview of the created structure for the RAG extension (some files are as examples, will receive recieve empty folders to set your files):

```plaintext
📦your_project
 ┃ 
 ┣ 📂user_flexiai_rag
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📂audio
 ┃ ┃ ┃ ┣ 📜Travelers_of_the_Cosmos.mp3
 ┃ ┃ ┃ ┣ 📜output.mp3
 ┃ ┃ ┃ ┣ 📜output_hd.mp3
 ┃ ┃ ┃ ┗ 📜test_output.wav
 ┃ ┃ ┣ 📂corpus
 ┃ ┃ ┃ ┣ 📂another_folder
 ┃ ┃ ┃ ┃ ┣ 📜probability.txt
 ┃ ┃ ┃ ┃ ┗ 📜python.txt
 ┃ ┃ ┃ ┣ 📜artificial_intelligence.txt
 ┃ ┃ ┃ ┣ 📜machine_learning.txt
 ┃ ┃ ┃ ┣ 📜natural_language_processing.txt
 ┃ ┃ ┃ ┗ 📜neural_network.txt
 ┃ ┃ ┣ 📂csv
 ┃ ┃ ┃ ┣ 📜identify_person.csv
 ┃ ┃ ┃ ┗ 📜products.csv
 ┃ ┃ ┣ 📂images
 ┃ ┃ ┃ ┣ 📜generated_image_1aec1dd8-b386-43d1-9a6c-ae6a7d5aeb21.png
 ┃ ┃ ┃ ┗ 📜generated_image_1bc706cc-85e5-4b53-b6f7-af3810d79177.png
 ┃ ┃ ┗ 📂vectors_store
 ┃ ┃ ┃ ┣ 📜updated_vector_store_after_replacement.index
 ┃ ┃ ┃ ┣ 📜updated_vector_store_after_replacement.index.meta
 ┃ ┃ ┃ ┣ 📜vector_store.index
 ┃ ┃ ┃ ┗ 📜vector_store.index.meta
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜user_function_mapping.py                  
 ┃ ┣ 📜user_helpers.py
 ┃ ┗ 📜user_task_manager.py
 ┣ 📂logs
 ┣ 📜requirements.txt
 ┣ 📜.env
 ┃
 ┗ ...
```

### FlexiAI Basic Flask Chat Application

Running the `flexiai_basic_flask_app.py` script will automatically create the necessary structure and files to set up a basic Flask chat application in your project.

Here's an overview of the created structure for the Flask app:

```plaintext
📦your_project
 ┃
 ┣ 📂logs
 ┃ ┗ 📜app.log
 ┣ 📂routes
 ┃ ┗ 📜api.py
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📂other_images
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 161351.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 161358.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 161449.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 165158.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 165318.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 165338.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 165350.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 165358.png
 ┃ ┃ ┃ ┗ 📜Screenshot 2024-07-12 165558.png
 ┃ ┃ ┣ 📜assistant.png
 ┃ ┃ ┗ 📜user.png
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js
 ┃ ┗ 📜favicon.ico
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📂utils
 ┃ ┗ 📜markdown_converter.py
 ┣ 📜app.py
 ┃
 ┗ ...
```

#### Post-Installation Steps

1. **Run the `flexiai_rag_extension.py` and `flexiai_basic_flask_app.py` files to create your starter folders and files.**

    ```powershell
    python flexiai_rag_extension.py
    python flexiai_basic_flask_app.py
    ```

2. **Install Requirements**

    Install the required dependencies using `pip`.

    ```powershell
    pip install -r requirements.txt
    ```

3. **Update the Assistant ID**

    Open the `routes/api.py` file and replace the placeholder assistant ID with your main assistant ID.

    ```python
    assistant_id = 'your_main_assistant_id'
    ```

4. **Add Images**

    In the `static` folder:
    - Add an `favicon.ico` image.
    - In the `static/images` folder, add `assistant.png` and `user.png` for the chat avatars.

    This ensures that your chat application has the necessary visual elements.

---

## Environment Setup

Before using FlexiAI, set up your environment variables. The `flexiai_rag_extension.py` script will create a `.env` file in your project root directory with the following template:

### Example .env File

```bash
# ============================================================================================ #
#                                      OpenAI Configuration                                    #
# ============================================================================================ #
# Replace 'your_openai_api_key_here' with your actual OpenAI API key.
OPENAI_API_KEY=your_openai_api_key_here

# Replace 'your_openai_api_version_here' with your actual OpenAI API version.
# Example for OpenAI: 2020-11-07
OPENAI_API_VERSION=your_openai_api_version_here

# Replace 'your_openai_organization_id_here' with your actual OpenAI Organization ID.
OPENAI_ORGANIZATION_ID=your_openai_organization_id_here

# Replace 'your_openai_project_id_here' with your actual OpenAI Project ID.
OPENAI_PROJECT_ID=your_openai_project_id_here

# Replace 'your_openai_assistant_version_here' with your actual OpenAI Assistant version.
# Example for Assistant: v1 or v2
OPENAI_ASSISTANT_VERSION=your_openai_assistant_version_here


# ============================================================================================ #
#                                      Azure OpenAI Configuration                              #
# ============================================================================================ #
# Replace 'your_azure_openai_api_key_here' with your actual Azure OpenAI API key.
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here

# Replace 'your_azure_openai_endpoint_here' with your actual Azure OpenAI endpoint.
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here

# Replace 'your_azure_openai_api_version_here' with your actual Azure OpenAI API version.
# Example for Azure: 2024-05-01-preview
AZURE_OPENAI_API_VERSION=your_azure_openai_api_version_here


# ============================================================================================ #
#                                      General Configuration                                   #
# ============================================================================================ #
# Set this to 'openai' if you are using OpenAI, or 'azure' if you are using Azure OpenAI.
CREDENTIAL_TYPE=openai

```

---
