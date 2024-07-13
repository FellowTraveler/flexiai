# flexiai/core/flexiai_client.py
import logging
from flexiai.assistant.task_manager import TaskManager
from flexiai.assistant.function_mapping import get_function_mappings, register_user_functions
from flexiai.credentials.credential_manager import CredentialManager
from flexiai.core.flexi_managers.message_manager import MessageManager
from flexiai.core.flexi_managers.run_manager import RunManager
from flexiai.core.flexi_managers.session_manager import SessionManager
from flexiai.core.flexi_managers.thread_manager import ThreadManager
from flexiai.core.flexi_managers.vector_store_manager import VectorStoreManager


class FlexiAI:
    """
    FlexiAI is a flexible AI framework for managing interactions with OpenAI and
    Azure OpenAI services. It supports dynamic creation and management of threads,
    adding user messages, and running threads with specified assistants, handling
    required actions and logging all activities.

    Attributes:
        logger (logging.Logger): Logger for logging information and errors.
        client (OpenAI or AzureOpenAI): Client for interacting with OpenAI or Azure OpenAI services.
        task_manager (TaskManager): Manages tasks and their execution.
        personal_function_mapping (dict): Mapping of function names to their personal function implementations.
        assistant_function_mapping (dict): Mapping of function names to their assistant function implementations.
        message_manager (MessageManager): Manages messages within threads.
        run_manager (RunManager): Manages runs within threads.
        session_manager (SessionManager): Manages sessions.
        thread_manager (ThreadManager): Manages threads.
        vector_store_manager (VectorStoreManager): Manages vector stores.
    """

    def __init__(self):
        """
        Initializes the FlexiAI instance by setting up logging, determining the
        credential type, and initializing the appropriate OpenAI or Azure OpenAI client. 
        Also sets up task management and function mappings.
        """
        # Initialize the logger for this class
        self.logger = logging.getLogger(__name__)

        # Initialize the credential manager and get the client
        self.credential_manager = CredentialManager()
        self.client = self.credential_manager.client

        # Initialize the task manager
        self.task_manager = TaskManager()

        # Get the function mappings for personal functions and assistant calling functions
        self.personal_function_mapping, self.assistant_function_mapping = get_function_mappings()

        # Register user functions
        self.personal_function_mapping, self.assistant_function_mapping = register_user_functions(
            self.personal_function_mapping,
            self.assistant_function_mapping
        )

        # Initialize manager classes
        self.message_manager = MessageManager(self.client, self.logger, self.personal_function_mapping, self.assistant_function_mapping)
        self.run_manager = RunManager(self.client, self.logger, self.personal_function_mapping, self.assistant_function_mapping, self.message_manager)
        self.session_manager = SessionManager(self.client, self.logger)
        self.thread_manager = ThreadManager(self.client, self.logger)
        self.vector_store_manager = VectorStoreManager(self.client, self.logger)

    def create_thread(self):
        """
        Creates a new thread.

        Returns:
            object: The newly created thread object.

        Raises:
            OpenAIError: If the API call to create a new thread fails.
            Exception: If an unexpected error occurs.
        """
        return self.thread_manager.create_thread()

    def add_user_message(self, thread_id, user_message):
        """
        Adds a user message to a specified thread.

        Args:
            thread_id (str): The ID of the thread.
            user_message (str): The user's message content.

        Returns:
            object: The message object that was added to the thread.

        Raises:
            OpenAIError: If the API call to add a user message fails.
            Exception: If an unexpected error occurs.
        """
        return self.message_manager.add_user_message(thread_id, user_message)

    def wait_for_run_completion(self, thread_id):
        """
        Waits for any active run in the thread to complete.

        Args:
            thread_id (str): The ID of the thread.

        Raises:
            OpenAIError: If the API call to retrieve thread runs fails.
            Exception: If an unexpected error occurs.
        """
        self.run_manager.wait_for_run_completion(thread_id)

    def create_run(self, assistant_id, thread_id):
        """
        Creates and runs a thread with the specified assistant, handling required actions.

        Args:
            assistant_id (str): The ID of the assistant.
            thread_id (str): The ID of the thread.

        Returns:
            object: The run object if the run completes successfully, None otherwise.

        Raises:
            OpenAIError: If any API call within this function fails.
            Exception: If an unexpected error occurs.
        """
        return self.run_manager.create_run(assistant_id, thread_id)

    def create_advanced_run(self, assistant_id, thread_id, user_message):
        """
        Creates and runs a thread with the specified assistant, user message and handling
        required actions.

        Args:
            assistant_id (str): The ID of the assistant.
            thread_id (str): The ID of the thread.
            user_message (str): The user's message content.

        Returns:
            object: The run object if the run completes successfully, None otherwise.

        Raises:
            OpenAIError: If any API call within this function fails.
            Exception: If an unexpected error occurs.
        """
        return self.run_manager.create_advanced_run(assistant_id, thread_id, user_message)

    def retrieve_messages(self, thread_id, order='desc', limit=20):
        """
        Retrieves the message objects from a specified thread.

        Args:
            thread_id (str): The ID of the thread.
            order (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'desc'.
            limit (int, optional): The number of messages to retrieve. Defaults to 20.

        Returns:
            list: A list of dictionaries containing the message ID, role, and content
            of each message.

        Raises:
            OpenAIError: If the API call to retrieve messages fails.
            Exception: If an unexpected error occurs.
        """
        return self.message_manager.retrieve_messages(thread_id, order, limit)

    def retrieve_message_object(self, thread_id, order='asc', limit=20):
        """
        Retrieves the message objects from a specified thread.

        Args:
            thread_id (str): The ID of the thread.
            order (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'asc'.
            limit (int, optional): The number of messages to retrieve. Defaults to 20.

        Returns:
            list: A list of message objects.

        Raises:
            OpenAIError: If the API call to retrieve messages fails.
            Exception: If an unexpected error occurs.
        """
        return self.message_manager.retrieve_message_object(thread_id, order, limit)

    def process_and_print_messages(self, messages):
        """
        Processes the message objects and prints the role and content value of each message.

        Args:
            messages (list): The list of message objects.
        """
        self.message_manager.process_and_print_messages(messages)

    def create_vector_store(self, name):
        """
        Creates a new vector store.

        Args:
            name (str): The name of the vector store.

        Returns:
            object: The newly created vector store object.

        Raises:
            RuntimeError: If the API call to create a new vector store fails.
        """
        return self.vector_store_manager.create_vector_store(name)

    def upload_files_and_poll(self, vector_store_id, file_paths):
        """
        Uploads files to the vector store and polls the status of the file batch for completion.

        Args:
            vector_store_id (str): The ID of the vector store.
            file_paths (list): A list of file paths to upload.

        Returns:
            object: The file batch object after upload and completion.

        Raises:
            RuntimeError: If the API call to upload files or poll status fails.
        """
        return self.vector_store_manager.upload_files_and_poll(vector_store_id, file_paths)

    def update_assistant_with_vector_store(self, assistant_id, vector_store_id):
        """
        Updates the assistant to use the new vector store.

        Args:
            assistant_id (str): The ID of the assistant.
            vector_store_id (str): The ID of the vector store.

        Returns:
            object: The updated assistant object.

        Raises:
            RuntimeError: If the API call to update the assistant fails.
        """
        return self.vector_store_manager.update_assistant_with_vector_store(assistant_id, vector_store_id)

    def list_vector_stores(self):
        """
        Retrieves a list of all existing vector stores.

        Returns:
            list: A list of vector store objects.

        Raises:
            RuntimeError: If the API call to list vector stores fails.
        """
        return self.vector_store_manager.list_vector_stores()

    def retrieve_vector_store_details(self, vector_store_id):
        """
        Retrieves detailed information about a specific vector store.

        Args:
            vector_store_id (str): The ID of the vector store.

        Returns:
            object: The vector store object with detailed information.

        Raises:
            RuntimeError: If the API call to retrieve vector store details fails.
        """
        return self.vector_store_manager.retrieve_vector_store_details(vector_store_id)

    def delete_vector_store(self, vector_store_id):
        """
        Deletes a vector store.

        Args:
            vector_store_id (str): The ID of the vector store.

        Returns:
            bool: True if the vector store was deleted successfully, False otherwise.

        Raises:
            RuntimeError: If the API call to delete the vector store fails.
        """
        return self.vector_store_manager.delete_vector_store(vector_store_id)

    def list_files_in_vector_store(self, vector_store_id, batch_id):
        """
        Lists all files that have been uploaded to a specific vector store.

        Args:
            vector_store_id (str): The ID of the vector store.
            batch_id (str): The ID of the file batch.

        Returns:
            list: A list of files in the vector store.

        Raises:
            RuntimeError: If the API call to list files in the vector store fails.
        """
        return self.vector_store_manager.list_files_in_vector_store(vector_store_id, batch_id)

    def retrieve_file_batch_details(self, vector_store_id, batch_id):
        """
        Retrieves the status and details of a specific file batch within a vector store.

        Args:
            vector_store_id (str): The ID of the vector store.
            batch_id (str): The ID of the file batch.

        Returns:
            object: The file batch object with detailed information.

        Raises:
            RuntimeError: If the API call to retrieve file batch details fails.
        """
        return self.vector_store_manager.retrieve_file_batch_details(vector_store_id, batch_id)


    def search_files_in_vector_store(self, vector_store_id, query):
        """
        Searches for files in a vector store based on a query.

        Args:
            vector_store_id (str): The ID of the vector store.
            query (str): The search query.

        Returns:
            list: A list of search results.

        Raises:
            RuntimeError: If the search operation fails.
        """
        return self.vector_store_manager.search_files_in_vector_store(vector_store_id, query)

