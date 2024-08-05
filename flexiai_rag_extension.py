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
                "blinker==1.8.2\n"
                "build==1.2.1\n"
                "certifi==2024.7.4\n"
                "cffi==1.16.0\n"
                "charset-normalizer==3.3.2\n"
                "click==8.1.7\n"
                "cryptography==43.0.0\n"
                "distro==1.9.0\n"
                "docutils==0.21.2\n"
                "Flask==3.0.3\n"
                "flexiai==1.1.0\n"
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
                "numpy==2.0.1\n"
                "openai==1.35.0\n"
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
