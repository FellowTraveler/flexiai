# user_flexiai_rag/user_task_manager.py
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

    # Add your functions here...
    