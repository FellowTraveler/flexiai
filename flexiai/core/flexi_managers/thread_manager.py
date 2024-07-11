# flexiai/core/thread_manager.py
from openai import OpenAIError

class ThreadManager:
    """
    ThreadManager handles the creation of new threads using the OpenAI or Azure OpenAI API.

    Attributes:
        client (OpenAI or AzureOpenAI): The client for interacting with OpenAI or Azure OpenAI services.
        logger (logging.Logger): The logger for logging information and errors.
    """

    def __init__(self, client, logger):
        """
        Initializes the ThreadManager instance with the specified client and logger.

        Args:
            client (OpenAI or AzureOpenAI): The client for interacting with OpenAI or Azure OpenAI services.
            logger (logging.Logger): The logger for logging information and errors.
        """
        self.client = client
        self.logger = logger

    def create_thread(self):
        """
        Creates a new thread.

        Returns:
            object: The newly created thread object.

        Raises:
            OpenAIError: If the API call to create a new thread fails.
            Exception: If an unexpected error occurs.
        """
        try:
            self.logger.info("Creating a new thread")
            thread = self.client.beta.threads.create()
            self.logger.info(f"Created thread with ID: {thread.id}")
            return thread
        except OpenAIError as e:
            self.logger.error(f"Failed to create a new thread: {str(e)}", exc_info=True)
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred while creating a thread: {str(e)}", exc_info=True)
            raise
