# user_flexiai_rag/user_task_manager.py
import logging
from flexiai.config.logging_config import setup_logging
import subprocess
import urllib.parse


# Set up logging using your custom configuration
setup_logging(root_level=logging.INFO, file_level=logging.DEBUG, console_level=logging.ERROR)

class UserTaskManager:
    """
    UserTaskManager class handles user-defined tasks.
    """

    def __init__(self):
        """
        Initializes the UserTaskManager instance, setting up the logger.
        """
        self.logger = logging.getLogger(__name__)


    def search_youtube(self, query):
        """
        Searches YouTube for the given query and opens the search results page
        in the default web browser.

        Args:
            query (str): The search query string.

        Returns:
            dict: A dictionary containing the status, message, and result (URL)
        """
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

            # subprocess.run(['cmd.exe', '/c', 'start', '', youtube_search_url], check=True)

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


