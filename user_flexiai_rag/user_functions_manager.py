# user_flexiai_rag/user_functions_manager.py
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

