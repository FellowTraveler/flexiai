# Setup Guide

This guide will help you set up FlexiAI in your project, including installation steps, virtual environment creation, and post-installation setup.

## Table of Contents

- [Installation](#installation)
  - [Create a Virtual Environment](#create-a-virtual-environment)
    - [Using PowerShell](#using-powershell)
    - [Using Conda](#using-conda)
  - [Install FlexiAI with `pip`](#install-flexiai-with-pip)
  - [Post-Installation Setup](#post-installation-setup)
    - [Enable Retrieval-Augmented Generation (RAG)](#enable-retrieval-augmented-generation-rag)
- [Environment Setup](#environment-setup)
  - [Example .env File](#example-env-file)

---

## Installation

### Create a Virtual Environment

Creating a virtual environment helps manage dependencies and avoid conflicts. Choose either PowerShell or Conda to create your virtual environment.

#### Using PowerShell

```powershell
python -m venv env
source env/bin/activate
```

#### Using Conda

```powershell
conda create --name flexiai_env python=3.12.4
conda activate flexiai_env
```

### Install FlexiAI with pip

To install the FlexiAI framework using `pip`, run:

```powershell
pip install flexiai
```

### Post-Installation Setup

After installing, copy the `flexiai_rag_extension.py` and `flexiai_basic_flask_app.py` files to your project root directory and run them manually to set up additional necessary directories and files.

- [Download flexiai_rag_extension.py](https://github.com/SavinRazvan/flexiai/blob/main/flexiai_rag_extension.py): This script sets up the necessary structure and files for enabling Retrieval-Augmented Generation (RAG) capabilities in your FlexiAI project.
- [Download flexiai_basic_flask_app.py](https://github.com/SavinRazvan/flexiai/blob/main/flexiai_basic_flask_app.py): This script creates a basic Flask application structure, including routes, static files, templates, and main application files, to facilitate running a web server for your FlexiAI project.

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
    
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f"Created directory: {data_folder}")
    
    files_content = {
        '__init__.py': "# user_flexiai_rag/__init__.py\n",
        'user_function_mapping.py': (
            "# user_flexiai_rag/user_function_mapping.py\n"
            "import logging\n"
            "from user_flexiai_rag.user_task_manager import UserTaskManager\n\n"
            "logger = logging.getLogger(__name__)\n\n"
            "def register_user_tasks(multi_agent_system, run_manager):\n"
            "    \"\"\"\n"
            "    Registers user-defined tasks with the FlexiAI framework.\n\n"
            "    This function initializes the UserTaskManager and sets up mappings for personal and assistant functions.\n"
            "    It logs the registration process and returns the function mappings.\n\n"
            "    Args:\n"
            "        multi_agent_system (MultiAgentSystemManager): The multi-agent system manager instance.\n"
            "        run_manager (RunManager): The run manager instance.\n\n"
            "    Returns:\n"
            "        tuple: A tuple containing two dictionaries:\n"
            "            - user_personal_functions (dict): Mapping of personal function names to their implementations.\n"
            "            - user_assistant_functions (dict): Mapping of assistant function names to their implementations.\n"
            "    \"\"\"\n"
            "    task_manager = UserTaskManager(multi_agent_system, run_manager)\n\n"
            "    user_personal_functions = {\n"
            "        # MAS functions for each agent:\n"
            "        'save_processed_content': task_manager.save_processed_content,\n"
            "        'load_processed_content': task_manager.load_processed_content,\n"
            "        'initialize_agent': task_manager.initialize_agent,\n"
            "        # Functions used by your assistants\n"
            "        'search_youtube': task_manager.search_youtube,\n"
            "    }\n\n"
            "    user_assistant_functions = {\n"
            "       'communicate_with_assistant': task_manager.continue_conversation_with_assistant,\n"
            "       # Other designs for MAS or other assistants\n"
            "    }\n\n"
            "    logger.info(\"Registering user tasks\")\n"
            "    logger.debug(f\"User personal functions: {list(user_personal_functions.keys())}\")\n"
            "    logger.debug(f\"User assistant functions: {list(user_assistant_functions.keys())}\")\n\n"
            "    return user_personal_functions, user_assistant_functions\n"
        ),
        'user_helpers.py': "# user_flexiai_rag/user_helpers.py\n",
        'user_task_manager.py': (
            "# user_flexiai_rag/user_task_manager.py\n"
            "import logging\n"
            "import urllib.parse\n"
            "import subprocess\n"
            "from threading import Lock\n"
            "from flexiai.core.flexi_managers.run_manager import RunManager\n"
            "from flexiai.core.flexi_managers.thread_manager import ThreadManager\n"
            "from flexiai.core.flexi_managers.message_manager import MessageManager\n"
            "from flexiai.core.flexi_managers.multi_agent_system import MultiAgentSystemManager\n\n\n"
            "class UserTaskManager:\n"
            "    \"\"\"\n"
            "    UserTaskManager class handles user-defined tasks for AI assistants, enabling \n"
            "    Retrieval-Augmented Generation (RAG) capabilities and interaction within the \n"
            "    Multi-Agent System.\n\n"
            "    This class provides methods to save and load processed content, continue conversations \n"
            "    with assistants, initialize agents, and perform specific tasks such as YouTube searches.\n"
            "    \"\"\"\n\n"
            "    def __init__(self, multi_agent_system: MultiAgentSystemManager, run_manager: RunManager):\n"
            "        \"\"\"\n"
            "        Initializes the UserTaskManager instance, setting up the logger and a lock for thread safety.\n\n"
            "        Args:\n"
            "            multi_agent_system (MultiAgentSystemManager): The multi-agent system manager instance.\n"
            "            run_manager (RunManager): The run manager instance.\n"
            "        \"\"\"\n"
            "        self.logger = logging.getLogger(__name__)\n"
            "        self.lock = Lock()\n"
            "        self.multi_agent_system = multi_agent_system\n"
            "        self.run_manager = run_manager\n"
            "        self.message_manager = multi_agent_system.message_manager\n\n\n"
            "    def log_function_call(self, func_name, params=None):\n"
            "        \"\"\"\n"
            "        Logs the function call.\n"
            "        \n"
            "        Args:\n"
            "            func_name (str): The name of the function being called.\n"
            "            params (dict, optional): Parameters passed to the function.\n"
            "        \"\"\"\n"
            "        param_str = f\" with params: {params}\" if params else \"\"\n"
            "        self.logger.info(f\"Function called: {func_name}{param_str}\")\n\n\n"
            "    def save_processed_content(self, from_assistant_id, to_assistant_id, processed_content):\n"
            "        \"\"\"\n"
            "        Saves the processed user content for RAG purposes, allowing AI assistants to \n"
            "        store and retrieve contextual information.\n\n"
            "        Args:\n"
            "            from_assistant_id (str): The assistant identifier from which the content originates.\n"
            "            to_assistant_id (str): The assistant identifier to which the content is directed.\n"
            "            processed_content (str): The processed content to store.\n\n"
            "        Returns:\n"
            "            bool: True if content is saved successfully, False otherwise.\n"
            "        \"\"\"\n"
            "        return self.multi_agent_system.save_processed_content(from_assistant_id, to_assistant_id, processed_content)\n\n\n"
            "    def load_processed_content(self, from_assistant_id, to_assistant_id, multiple_retrieval):\n"
            "        \"\"\"\n"
            "        Loads the stored processed user content, enabling AI assistants to access \n"
            "        previously stored information for enhanced context and continuity in RAG.\n\n"
            "        Args:\n"
            "            from_assistant_id (str): The assistant identifier from which the content originates.\n"
            "            to_assistant_id (str): The assistant identifier to which the content is directed.\n"
            "            multiple_retrieval (bool): Whether to retrieve content from all sources, not just the specified to_assistant_id.\n\n"
            "        Returns:\n"
            "            list: A list of stored user content if found, otherwise an empty list.\n"
            "        \"\"\"\n"
            "        return self.multi_agent_system.load_processed_content(from_assistant_id, to_assistant_id, multiple_retrieval)\n\n\n"
            "    def continue_conversation_with_assistant(self, assistant_id, user_content):\n"
            "        \"\"\"\n"
            "        Continues the conversation with an assistant by submitting user content \n"
            "        and managing the resulting run, allowing dynamic and contextually aware interactions.\n\n"
            "        Args:\n"
            "            assistant_id (str): The unique identifier for the assistant.\n"
            "            user_content (str): The content submitted by the user.\n\n"
            "        Returns:\n"
            "            tuple: A tuple containing a success status, a message detailing the outcome, and the processed content.\n"
            "        \"\"\"\n"
            "        return self.multi_agent_system.continue_conversation_with_assistant(assistant_id, user_content)\n\n\n"
            "    def initialize_agent(self, assistant_id):\n"
            "        \"\"\"\n"
            "        Initializes an agent for the given assistant ID. If a thread already exists for the assistant ID,\n"
            "        it returns a message indicating the existing thread. Otherwise, it creates a new thread and returns\n"
            "        a message indicating successful initialization.\n\n"
            "        Args:\n"
            "            assistant_id (str): The unique identifier for the assistant.\n\n"
            "        Returns:\n"
            "            str: A message indicating the result of the initialization.\n"
            "        \"\"\"\n"
            "        return self.multi_agent_system.initialize_agent(assistant_id)\n\n\n"
            "    def search_youtube(self, query):\n"
            "        \"\"\"\n"
            "        Searches YouTube for the given query and opens the search results page\n"
            "        in the default web browser. This function demonstrates integration with \n"
            "        external services as part of RAG capabilities.\n\n"
            "        Args:\n"
            "            query (str): The search query string.\n\n"
            "        Returns:\n"
            "            dict: A dictionary containing the status, message, and result (URL)\n"
            "        \"\"\"\n"
            "        self.log_function_call('search_youtube', {'query': query})\n\n"
            "        if not query:\n"
            "            return {\n"
            "                \"status\": False,\n"
            "                \"message\": \"Query cannot be empty.\",\n"
            "                \"result\": None\n"
            "            }\n\n"
            "        try:\n"
            "            # Normalize spaces to ensure consistent encoding\n"
            "            query_normalized = query.replace(\" \", \"+\")\n"
            "            query_encoded = urllib.parse.quote(query_normalized)\n"
            "            youtube_search_url = (\n"
            "                f\"https://www.youtube.com/results?search_query={query_encoded}\"\n"
            "            )\n"
            "            self.logger.info(f\"Opening YouTube search for query: {query}\")\n\n"
            "            # Use PowerShell to open the URL\n"
            "            subprocess.run(\n"
            "                ['powershell.exe', '-Command', 'Start-Process', youtube_search_url],\n"
            "                check=True\n"
            "            )\n"
            "            self.logger.info(\"YouTube search page opened successfully.\")\n"
            "            return {\n"
            "                \"status\": True,\n"
            "                \"message\": \"YouTube search page opened successfully.\",\n"
            "                \"result\": youtube_search_url\n"
            "            }\n"
            "        except subprocess.CalledProcessError as e:\n"
            "            error_message = f\"Subprocess error: {str(e)}\"\n"
            "            self.logger.error(error_message, exc_info=True)\n"
            "            return {\n"
            "                \"status\": False,\n"
            "                \"message\": error_message,\n"
            "                \"result\": None\n"
            "            }\n"
            "        except Exception as e:\n"
            "            error_message = f\"Failed to open YouTube search for query: {query}. Error: {str(e)}\"\n"
            "            self.logger.error(error_message, exc_info=True)\n"
            "            return {\n"
            "                \"status\": False,\n"
            "                \"message\": error_message,\n"
            "                \"result\": None\n"
            "            }\n"
        ),
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
                "CREDENTIAL_TYPE=openai\n"
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
                "blinker==1.8.2\n"
                "certifi==2024.7.4\n"
                "cffi==1.16.0\n"
                "charset-normalizer==3.3.2\n"
                "click==8.1.7\n"
                "cryptography==43.0.0\n"
                "distro==1.9.0\n"
                "Flask==3.0.3\n"
                "glob2==0.7\n"
                "h11==0.14.0\n"
                "httpcore==1.0.5\n"
                "httpx==0.27.0\n"
                "idna==3.7\n"
                "iniconfig==2.0.0\n"
                "isodate==0.6.1\n"
                "itsdangerous==2.2.0\n"
                "Jinja2==3.1.4\n"
                "MarkupSafe==2.1.5\n"
                "msal==1.30.0\n"
                "msal-extensions==1.2.0\n"
                "nest-asyncio==1.6.0\n"
                "openai==1.35.0\n"
                "packaging==24.1\n"
                "platformdirs==3.7.0\n"
                "pluggy==1.5.0\n"
                "portalocker==2.10.1\n"
                "pycparser==2.22\n"
                "pydantic==2.7.4\n"
                "pydantic-settings==2.3.3\n"
                "pydantic_core==2.18.4\n"
                "PyJWT==2.8.0\n"
                "pytest==8.3.1\n"
                "python-dotenv==1.0.1\n"
                "requests==2.32.3\n"
                "six==1.16.0\n"
                "sniffio==1.3.1\n"
                "tqdm==4.66.4\n"
                "typing_extensions==4.12.2\n"
                "urllib3==2.2.2\n"
                "Werkzeug==3.0.3\n"
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

def create_logs_folder(project_root):
    log_folder = os.path.join(project_root, 'logs')
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
        print(f"Created directory: {log_folder}")

def create_routes_folder(project_root):
    routes_folder = os.path.join(project_root, 'routes')
    if not os.path.exists(routes_folder):
        os.makedirs(routes_folder)
        print(f"Created directory: {routes_folder}")
    
    files_content = {
        'api.py': (
            "# routes/api.py\n"
            "from flask import Blueprint, request, jsonify, session as flask_session\n"
            "from flexiai import FlexiAI\n"
            "from flexiai.config.logging_config import setup_logging\n"
            "import uuid\n\n"
            "api_bp = Blueprint('api', __name__)\n"
            "flexiai = FlexiAI()\n\n"
            "# setup_logging() # Check logs -> app.log file after you activate this\n\n"
            "def message_to_dict(message):\n"
            "    \"\"\"\n"
            "    Convert a message object to a dictionary, including nested TextContentBlock objects.\n"
            "    \"\"\"\n"
            "    message_dict = {\n"
            "        'id': message.id,\n"
            "        'role': message.role,\n"
            "        'content': [block.text.value for block in message.content if hasattr(block, 'text') and hasattr(block.text, 'value')]\n"
            "    }\n"
            "    return message_dict\n\n"
            "@api_bp.route('/run', methods=['POST'])\n"
            "def run():\n"
            "    data = request.json\n"
            "    user_message = data['message']\n"
            "    assistant_id = 'asst_bxt62YG46C5wn4t5U1ESqJZf'  # Updated assistant ID\n"
            "    thread_id = data.get('thread_id')\n\n"
            "    session_id = flask_session.get('session_id')\n"
            "    if not session_id:\n"
            "        session_id = str(uuid.uuid4())  # Generate a new session ID\n"
            "        flask_session['session_id'] = session_id\n"
            "        flexiai.session_manager.create_session(session_id, {\"thread_id\": thread_id, \"seen_message_ids\": []})\n"
            "    else:\n"
            "        session_data = flexiai.session_manager.get_session(session_id)\n"
            "        thread_id = session_data.get(\"thread_id\", thread_id)\n\n"
            "    if not thread_id:\n"
            "        thread = flexiai.create_thread()\n"
            "        thread_id = thread.id\n"
            "        flexiai.session_manager.create_session(session_id, {\"thread_id\": thread_id, \"seen_message_ids\": []})\n\n"
            "    last_retrieved_id = None\n"
            "    flexiai.create_advanced_run(assistant_id, thread_id, user_message)\n"
            "    messages = flexiai.retrieve_messages_dynamically(thread_id, limit=20, retrieve_all=False, last_retrieved_id=last_retrieved_id)\n\n"
            "    session_data = flexiai.session_manager.get_session(session_id)\n"
            "    seen_message_ids = set(session_data.get(\"seen_message_ids\", []))\n\n"
            "    filtered_messages = []\n"
            "    new_seen_message_ids = list(seen_message_ids)\n\n"
            "    for msg in messages:\n"
            "        if msg.id not in seen_message_ids:\n"
            "            filtered_messages.append({\n"
            "                \"role\": \"You\" if msg.role == \"user\" else \"Assistant\",\n"
            "                \"message\": \" \".join([block.text.value for block in msg.content if hasattr(block, 'text') and hasattr(block.text, 'value')])\n"
            "            })\n"
            "            new_seen_message_ids.append(msg.id)\n\n"
            "    flexiai.session_manager.create_session(session_id, {\"thread_id\": thread_id, \"seen_message_ids\": new_seen_message_ids})\n\n"
            "    return jsonify(success=True, thread_id=thread_id, messages=filtered_messages)\n\n"
            "@api_bp.route('/thread/<thread_id>/messages', methods=['GET'])\n"
            "def get_thread_messages(thread_id):\n"
            "    session_id = flask_session.get('session_id')\n"
            "    if not session_id:\n"
            "        return jsonify(success=False, message=\"Session not found\"), 404\n\n"
            "    messages = flexiai.retrieve_messages(thread_id, limit=20)\n"
            "    formatted_messages = [\n"
            "        {\n"
            "            \"role\": \"You\" if msg.role == \"user\" else \"Assistant\",\n"
            "            \"message\": \" \".join([block.text.value for block in msg.content if hasattr(block, 'text') and hasattr(block.text, 'value')])\n"
            "        }\n"
            "        for msg in messages\n"
            "    ]\n"
            "    return jsonify(success=True, thread_id=thread_id, messages=formatted_messages)\n\n"
            "@api_bp.route('/session', methods=['POST'])\n"
            "def create_session():\n"
            "    data = request.json\n"
            "    session_id = data['session_id']\n"
            "    session_data = data['data']\n"
            "    session = flexiai.session_manager.create_session(session_id, session_data)\n"
            "    return jsonify(success=True, session=session)\n\n"
            "@api_bp.route('/session/<session_id>', methods=['GET'])\n"
            "def get_session(session_id):\n"
            "    try:\n"
            "        session_data = flexiai.session_manager.get_session(session_id)\n"
            "        return jsonify(success=True, session=session_data)\n"
            "    except KeyError:\n"
            "        return jsonify(success=False, message=\"Session not found\"), 404\n\n"
            "@api_bp.route('/session/<session_id>', methods=['DELETE'])\n"
            "def delete_session(session_id):\n"
            "    success = flexiai.session_manager.delete_session(session_id)\n"
            "    return jsonify(success=success)\n\n"
            "@api_bp.route('/sessions', methods=['GET'])\n"
            "def get_all_sessions():\n"
            "    sessions = flexiai.session_manager.get_all_sessions()\n"
            "    return jsonify(success=True, sessions=sessions)\n\n"
            "@api_bp.route('/sessions', methods=['DELETE'])\n"
            "def clear_all_sessions():\n"
            "    success = flexiai.session_manager.clear_all_sessions()\n"
            "    return jsonify(success=success)\n"
        )
    }
    
    for filename, content in files_content.items():
        file_path = os.path.join(routes_folder, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")

def create_static_folder(project_root):
    static_folder = os.path.join(project_root, 'static')
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)
        print(f"Created directory: {static_folder}")
    
    subfolders = ['css', 'images', 'js']
    files_content = {
        'css/styles.css': (
            "/* static/css/styles.css */\n\n"
            "/* Import Open Sans Font */\n"
            "@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');\n\n"
            "/* Base Styles */\n"
            "body {\n"
            "    font-family: 'Open Sans', sans-serif;\n"
            "    margin: 0;\n"
            "    padding: 0;\n"
            "    background-color: #535353;\n"
            "    display: flex;\n"
            "    justify-content: center;\n"
            "    align-items: flex-start;\n"
            "    height: 100vh;\n"
            "}\n\n"
            "/* Chat Container */\n"
            "#chat-container {\n"
            "    width: 100%;\n"
            "    max-width: 680px;\n"
            "    height: calc(100vh - 2rem);\n"
            "    display: flex;\n"
            "    flex-direction: column;\n"
            "    background-color: #ffffff;\n"
            "    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);\n"
            "    border-radius: 8px;\n"
            "    margin: 1rem 0;\n"
            "    overflow: hidden;\n"
            "}\n\n"
            "/* Links */\n"
            "a {\n"
            "    color: #89e600;\n"
            "}\n\n"
            "/* Messages List */\n"
            "#messages {\n"
            "    list-style-type: none;\n"
            "    padding: 1rem;\n"
            "    flex: 1;\n"
            "    overflow-y: auto;\n"
            "    margin: 0;\n"
            "    color: #e1e1e6;\n"
            "}\n\n"
            "/* Message Item */\n"
            "#messages li {\n"
            "    padding: 0.5rem 0;\n"
            "    margin: 0.5rem 0;\n"
            "    border-radius: 4px;\n"
            "    word-wrap: break-word;\n"
            "    display: flex;\n"
            "    align-items: flex-start;\n"
            "    animation: fadeIn 0.5s ease-in-out;\n"
            "}\n\n"
            "/* Animation for messages */\n"
            "@keyframes fadeIn {\n"
            "    from { opacity: 0; transform: translateY(10px); }\n"
            "    to { opacity: 1; transform: translateY(0); }\n"
            "}\n\n"
            "/* Message Container */\n"
            ".message-container {\n"
            "    display: flex;\n"
            "    align-items: flex-start;\n"
            "    width: 100%;\n"
            "}\n\n"
            "/* Avatar */\n"
            ".avatar {\n"
            "    width: 45px;\n"
            "    height: 45px;\n"
            "    border-radius: 50%;\n"
            "    background-color: #25272a;\n"
            "    display: flex;\n"
            "    justify-content: center;\n"
            "    align-items: center;\n"
            "    margin-right: 10px;\n"
            "    font-size: 1.2em;\n"
            "    color: #ffffff;\n"
            "    border: 1px solid #c6c6c6;\n"
            "    overflow: hidden;\n"
            "}\n\n"
            "/* Avatar Images */\n"
            ".avatar img {\n"
            "    width: 100%;\n"
            "    height: 100%;\n"
            "    border-radius: 50%;\n"
            "}\n\n"
            "/* Message Content */\n"
            ".message-content {\n"
            "    flex: 1;\n"
            "    padding: 0.75rem 1rem;\n"
            "    border-radius: 4px;\n"
            "    font-size: 0.9em;\n"
            "    background-color: #3a3f4b;\n"
            "    color: #e1e1e6;\n"
            "    position: relative;\n"
            "}\n\n"
            "/* User Message */\n"
            ".user .message-content {\n"
            "    background-color: #3a3a3a;\n"
            "    text-align: left;\n"
            "    color: #e1e1e6;\n"
            "}\n\n"
            "/* Assistant Message */\n"
            ".assistant .message-content {\n"
            "    background-color: #404a63;\n"
            "    text-align: left;\n"
            "}\n\n"
            "/* Error Message */\n"
            "#error {\n"
            "    background-color: #ff4c4c;\n"
            "    text-align: center;\n"
            "    color: #fff;\n"
            "}\n"
            "#error-message {\n"
            "    color: #fff;\n"
            "}\n\n"
            "/* Input Container */\n"
            "#input-container {\n"
            "    display: flex;\n"
            "    align-items: center;\n"
            "    padding: 0.75rem 1rem;\n"
            "    border-top: 1px solid #353940;\n"
            "    background-color: #ffffff;\n"
            "}\n\n"
            "/* Message Input */\n"
            "#message-input {\n"
            "    flex: 1;\n"
            "    padding: 0.75rem;\n"
            "    border: 1px solid #484e5c;\n"
            "    border-radius: 20px;\n"
            "    margin-right: 0.5rem;\n"
            "    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);\n"
            "    transition: border-color 0.3s;\n"
            "    background-color: #3a3a3a;\n"
            "    color: #e1e1e6;\n"
            "    width: 100%;\n"
            "    box-sizing: border-box;\n"
            "}\n"
            "#message-input:focus {\n"
            "    border-color: #5a5a5a;\n"
            "    outline: none;\n"
            "}\n\n"
            "/* Send Button */\n"
            "#send-button {\n"
            "    padding: 0.75rem 1rem;\n"
            "    border: none;\n"
            "    border-radius: 20px;\n"
            "    background-color: #404a63;\n"
            "    color: white;\n"
            "    cursor: pointer;\n"
            "    transition: background-color 0.3s, transform 0.1s;\n"
            "    flex-shrink: 0;\n"
            "}\n"
            "#send-button:hover {\n"
            "    background-color: #2a3552;\n"
            "}\n"
            "#send-button:active {\n"
            "    transform: scale(0.95);\n"
            "}\n\n"
            "/* Markdown Content */\n"
            ".markdown-content {\n"
            "    font-size: 0.9em;\n"
            "    line-height: 1.4em;\n"
            "    margin: 0;\n"
            "}\n\n"
            ".markdown-content h1, .markdown-content h2, .markdown-content h3 {\n"
            "    border-bottom: 1px solid #444;\n"
            "    padding-bottom: 0.3em;\n"
            "    margin-top: 0.5em;\n"
            "    font-size: 1.1em;\n"
            "}\n\n"
            ".markdown-content p {\n"
            "    margin: 0.5em 0;\n"
            "}\n\n"
            ".markdown-content code {\n"
            "    background-color: #2e2e2e;\n"
            "    border-radius: 3px;\n"
            "    padding: 0.2em 0.4em;\n"
            "    color: #e1e1e6;\n"
            "}\n\n"
            ".markdown-content pre {\n"
            "    background-color: #2e2e2e;\n"
            "    padding: 1em;\n"
            "    border-radius: 3px;\n"
            "    overflow-x: auto;\n"
            "    font-size: 0.85em;\n"
            "    color: #e1e1e6;\n"
            "}\n\n"
            ".markdown-content ol, .markdown-content ul {\n"
            "    margin-left: -1em;\n"
            "    padding-left: 1.5em;\n"
            "}\n\n"
            "/* Responsive Design */\n"
            "@media (max-width: 600px) {\n"
            "    #chat-container {\n"
            "        height: calc(100vh - 2rem);\n"
            "    }\n"
            "    #message-input {\n"
            "        padding: 0.75rem;\n"
            "    }\n"
            "    #send-button {\n"
            "        padding: 0.75rem 1rem;\n"
            "    }\n"
            "    .avatar {\n"
            "        width: 30px;\n"
            "        height: 30px;\n"
            "        font-size: 1em;\n"
            "    }\n"
            "    .message-content {\n"
            "        font-size: 0.85em;\n"
            "        padding: 0.75rem 1rem;\n"
            "    }\n"
            "    .markdown-content {\n"
            "        font-size: 0.85em;\n"
            "    }\n"
            "}\n"
        ),
        'js/scripts.js': (
            "// static/js/scripts.js\n\n"
            "let threadId = null;\n\n"
            "document.getElementById('send-button').addEventListener('click', sendMessage);\n"
            "document.getElementById('message-input').addEventListener('keypress', function(event) {\n"
            "    if (event.key === 'Enter') {\n"
            "        sendMessage();\n"
            "    }\n"
            "});\n\n"
            "function sendMessage() {\n"
            "    const messageInput = document.getElementById('message-input');\n"
            "    const message = messageInput.value.trim();\n"
            "    if (message === '') return;\n\n"
            "    console.log('Sending message:', message);\n\n"
            "    // Add user message to chat directly without retrieval\n"
            "    addMessage('You', message, 'user');\n\n"
            "    // Send message to server\n"
            "    fetch('/api/run', {\n"
            "        method: 'POST',\n"
            "        headers: { 'Content-Type': 'application/json' },\n"
            "        body: JSON.stringify({ message: message, thread_id: threadId })\n"
            "    })\n"
            "    .then(response => response.json())\n"
            "    .then(data => {\n"
            "        console.log('Received response:', data); // Log the response to debug\n"
            "        if (data.success) {\n"
            "            threadId = data.thread_id;\n"
            "            updateChat(data.messages);\n"
            "        } else {\n"
            "            addMessage('Error', 'Failed to get response from assistant.', 'error');\n"
            "        }\n"
            "    })\n"
            "    .catch(error => {\n"
            "        console.error('Fetch error:', error);\n"
            "        addMessage('Error', 'An error occurred: ' + error.message, 'error');\n"
            "    });\n\n"
            "    // Clear input\n"
            "    messageInput.value = '';\n"
            "}\n\n"
            "function addMessage(role, text, className) {\n"
            "    console.log('Adding message:', role, text);\n\n"
            "    const messageElement = document.createElement('li');\n"
            "    messageElement.className = className;\n\n"
            "    // Determine avatar based on role\n"
            "    const avatar = role === 'You' ? '/static/images/user.png' : '/static/images/assistant.png';\n\n"
            "    // Convert markdown to HTML\n"
            "    try {\n"
            "        const htmlContent = window.marked.parse(text);\n"
            "        console.log('HTML Content:', htmlContent); // Log the HTML content to debug\n"
            "        messageElement.innerHTML = `\n"
            "            <div class=\"message-container\">\n"
            "                <div class=\"avatar\"><img src=\"${avatar}\" alt=\"${role}\" /></div>\n"
            "                <div class=\"message-content\">\n"
            "                    <div class=\"markdown-content\">${htmlContent}</div>\n"
            "                </div>\n"
            "            </div>`;\n"
            "    } catch (error) {\n"
            "        console.error('Markdown conversion error:', error);\n"
            "        messageElement.innerHTML = `\n"
            "            <div class=\"message-container\">\n"
            "                <div class=\"avatar\"><img src=\"${avatar}\" alt=\"${role}\" /></div>\n"
            "                <div class=\"message-content\">\n"
            "                    <div class=\"markdown-content\">${text}</div>\n"
            "                </div>\n"
            "            </div>`;\n"
            "    }\n\n"
            "    const messagesContainer = document.getElementById('messages');\n"
            "    messagesContainer.appendChild(messageElement);\n"
            "    messagesContainer.scrollTop = messagesContainer.scrollHeight;\n"
            "}\n\n"
            "function updateChat(messages) {\n"
            "    messages.forEach(msg => {\n"
            "        if (msg.role === 'Assistant') {\n"
            "            addMessage('Assistant', msg.message, 'assistant');\n"
            "        }\n"
            "    });\n"
            "}\n\n"
            "// Test if marked is available\n"
            "if (typeof window.marked !== 'undefined') {\n"
            "    console.log('Marked library is loaded');\n"
            "} else {\n"
            "    console.error('Marked library is not loaded');\n"
            "}\n"
        ),
    }
    
    for subfolder in subfolders:
        subfolder_path = os.path.join(static_folder, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            print(f"Created directory: {subfolder_path}")

    for filename, content in files_content.items():
        file_path = os.path.join(static_folder, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")

def create_templates_folder(project_root):
    templates_folder = os.path.join(project_root, 'templates')
    if not os.path.exists(templates_folder):
        os.makedirs(templates_folder)
        print(f"Created directory: {templates_folder}")
    
    files_content = {
        'index.html': (
            "<!-- templates/index.html -->\n"
            "<!DOCTYPE html>\n"
            "<html lang=\"en\">\n"
            "<head>\n"
            "    <meta charset=\"UTF-8\">\n"
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            "    <title>FlexiAI Chat Application</title>\n"
            "    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/styles.css') }}\">\n"
            "    <link rel=\"icon\" href=\"{{ url_for('static', filename='favicon.ico') }}\" type=\"image/x-icon\">\n"
            "</head>\n"
            "<body>\n"
            "    <div id=\"chat-container\">\n"
            "        <ul id=\"messages\"></ul>\n"
            "        <div id=\"input-container\">\n"
            "            <input type=\"text\" id=\"message-input\" placeholder=\"Type your message here...\">\n"
            "            <button id=\"send-button\">Send</button>\n"
            "        </div>\n"
            "    </div>\n\n"
            "    <!-- Include the Marked.js library -->\n"
            "    <script src=\"https://cdn.jsdelivr.net/npm/marked/marked.min.js\"></script>\n"
            "    <!-- Custom JavaScript file -->\n"
            "    <script src=\"{{ url_for('static', filename='js/scripts.js') }}\"></script>\n"
            "</body>\n"
            "</html>\n"
        )
    }
    
    for filename, content in files_content.items():
        file_path = os.path.join(templates_folder, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")

def create_main_files(project_root):
    main_files_content = {
        'app.py': (
            "# app.py\n"
            "import os\n"
            "from flask import Flask, session, render_template\n"
            "from datetime import timedelta\n"
            "from routes.api import api_bp\n"
            "from flexiai import FlexiAI\n\n"
            "app = Flask(__name__, static_folder='static', template_folder='templates')\n"
            "app.secret_key = os.urandom(24)  # Secure the session with a secret key\n"
            "app.register_blueprint(api_bp, url_prefix='/api')\n\n"
            "flexiai = FlexiAI()\n\n"
            "@app.before_request\n"
            "def before_request():\n"
            "    session.permanent = True\n"
            "    app.permanent_session_lifetime = timedelta(minutes=30)  # Set session lifetime\n\n"
            "@app.route('/')\n"
            "def index():\n"
            "    return render_template('index.html')\n\n"
            "if __name__ == '__main__':\n"
            "    app.run(host='0.0.0.0', port=5000, debug=False)\n"
        ),
        'run.py': (
            "# run.py\n"
            "import os\n"
            "from dotenv import load_dotenv\n"
            "from app import app\n\n"
            "# Load environment variables from .env file\n"
            "load_dotenv()\n\n"
            "# Set Flask-related environment variables programmatically\n"
            "os.environ['FLASK_APP'] = 'run.py'\n"
            "os.environ['FLASK_ENV'] = 'development'\n"
            "os.environ['FLASK_DEBUG'] = '1'\n\n"
            "if __name__ == '__main__':\n"
            "    app.run(host='0.0.0.0', port=5000, debug=False)\n"
        )
    }
    
    for filename, content in main_files_content.items():
        file_path = os.path.join(project_root, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")

if __name__ == '__main__':
    project_root = os.getcwd()

    try:
        create_logs_folder(project_root)
        create_routes_folder(project_root)
        create_static_folder(project_root)
        create_templates_folder(project_root)
        create_main_files(project_root)
    except Exception as e:
        print(f"Post-installation step failed: {e}")


```

</details>

### Enable Retrieval-Augmented Generation (RAG)

Running the `flexiai_rag_extension.py` and `flexiai_basic_flask_app.py` scripts will automatically create the necessary structure and files to enable the Retrieval-Augmented Generation (RAG) module and the basic Flask app in your project.

Here's an overview of the created structure:

```plaintext
📦your_project
 ┃
 ┣ 📂user_flexiai_rag
 ┃ ┣ 📂data
 ┃ ┃ ┗ 📜your data files
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜user_function_mapping.py
 ┃ ┣ 📜user_helpers.py             
 ┃ ┗ 📜user_task_manager.py
 ┣
 ┣ 📂logs
 ┣ 📂routes
 ┃ ┗ 📜api.py
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📜assistant.png              <- Add your Assistant image, make sure to have same name
 ┃ ┃ ┗ 📜user.png                   <- Add your User image, make sure to have same name
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js
 ┃ ┗ 📜favicon.ico                  <- Add your favicon.ico image, make sure to have same name
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📜app.py
 ┣ 📜run.py
 ┣ 📜requirements.txt
 ┗ 📜.env
 ┣ 
 ...
 ┣ 📂 other folders ...
 ┣ 📜 other files ...
 ┣  ...

```

#### Run the `flexiai_rag_extension.py` and `flexiai_basic_flask_app.py` files to create your starter folders and files.

```powershell
python flexiai_rag_extension.py
python flexiai_basic_flask_app.py
```

### Install Requirements

Install the required dependencies using `pip`.

```powershell
pip install -r requirements.txt
```

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
