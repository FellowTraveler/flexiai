# post_install/flexiai_rag_extension.py
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
        'user_functions_mapping.py': '''# user_flexiai_rag/user_functions_mapping.py
import logging
from user_flexiai_rag.user_functions_manager import FunctionsManager

logger = logging.getLogger(__name__)

async def map_user_functions():
    """
    Maps user-defined functions to FlexiAI asynchronously and efficiently, ready for future calls.
    
    This function should be awaited when called by the FunctionMapping class.
    """
    logger.info("Mapping user-defined functions...")

    # Initialize the FunctionsManager
    user_functions_manager = FunctionsManager()

    # Map user-defined personal and assistant functions
    user_personal_functions = {
        'search_youtube': user_functions_manager.search_youtube,
    }

    user_assistant_functions = {
        #  Functions to call other assistants, must end with '_assistant'
    }

    logger.info(f"User personal functions are: {list(user_personal_functions.keys())}")
    logger.info(f"User assistant functions are: {list(user_assistant_functions.keys())}")

    # Return the mappings
    return user_personal_functions, user_assistant_functions
''',
        'user_functions_manager.py': '''# user_flexiai_rag/user_functions_manager.py
import logging
import urllib.parse
import subprocess

class FunctionsManager:
    """
    FunctionsManager handles user-defined tasks, enabling RAG capabilities, interactions,
    and async operations for tasks such as saving/loading content, initializing agents,
    and YouTube searches.
    """

    def __init__(self):
        """
        Initializes the FunctionsManager instance.
        """
        self.logger = logging.getLogger(__name__)


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
        self.logger.info(f"Executing search on YouTube with query: {query}")

        if not query:
            return {
                "status": False,
                "message": "Query cannot be empty.",
                "result": None
            }

        try:
            query_encoded = urllib.parse.quote(query)
            youtube_search_url = f"https://www.youtube.com/results?search_query={query_encoded}"
            self.logger.info(f"Opening YouTube search for query: {query}")

            subprocess.run(['powershell.exe', '-Command', 'Start-Process', youtube_search_url], check=True)
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

    # Add your other functions to be used by assistants. Functions are of these types:
    # - personal functions: functions used by your assistant for personal tasks (execute actions 
    #                       or gather information to provide accurate results)
    # - assistant functions: functions that call other assistants in the Multi-Agent System, 
    #                        must end with '_assistant'

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
