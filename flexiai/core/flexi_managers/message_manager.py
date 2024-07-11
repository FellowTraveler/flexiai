from openai import OpenAIError

class MessageManager:
    """
    MessageManager is responsible for managing messages in threads, including adding
    user messages, retrieving messages, and processing message content.

    Attributes:
        client (OpenAI or AzureOpenAI): The client for interacting with OpenAI or Azure OpenAI services.
        logger (logging.Logger): The logger for logging information and errors.
        personal_function_mapping (dict): Mapping of function names to their personal function implementations.
        assistant_function_mapping (dict): Mapping of function names to their assistant function implementations.
    """

    def __init__(self, client, logger, personal_function_mapping, assistant_function_mapping):
        """
        Initializes the MessageManager instance with the specified client, logger,
        and function mappings.

        Args:
            client (OpenAI or AzureOpenAI): The client for interacting with OpenAI or Azure OpenAI services.
            logger (logging.Logger): The logger for logging information and errors.
            personal_function_mapping (dict): Mapping of function names to their personal function implementations.
            assistant_function_mapping (dict): Mapping of function names to their assistant function implementations.
        """
        self.client = client
        self.logger = logger
        self.personal_function_mapping = personal_function_mapping
        self.assistant_function_mapping = assistant_function_mapping

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
        try:
            self.logger.info(f"Adding user message to thread {thread_id}: {user_message}")
            message = self.client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_message
            )
            self.logger.info(f"Added user message with ID: {message.id}")
            return message
        except OpenAIError as e:
            self.logger.error(f"Failed to add a user message to the thread {thread_id}: {str(e)}", exc_info=True)
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred while adding a user message to thread {thread_id}: {str(e)}", exc_info=True)
            raise

    def retrieve_messages(self, thread_id, order='desc', limit=20):
        """
        Retrieves messages from a specified thread.

        Args:
            thread_id (str): The ID of the thread.
            order (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'desc'.
            limit (int, optional): The number of messages to retrieve. Defaults to 20.

        Returns:
            list: A list of dictionaries containing the message ID, role, and content of each message.

        Raises:
            OpenAIError: If the API call to retrieve messages fails.
            Exception: If an unexpected error occurs.
        """
        try:
            params = {'order': order, 'limit': limit}
            response = self.client.beta.threads.messages.list(thread_id=thread_id, **params)
            if not response.data:
                self.logger.info("No data found in the response or no messages.")
                return []

            self.logger.info(f"Retrieved {len(response.data)} messages from thread {thread_id}")
            messages = response.data[::-1]
            formatted_messages = []

            for message in messages:
                message_id = message.id
                role = message.role
                content_blocks = message.content
                content_value = " ".join([
                    block.text.value for block in content_blocks if hasattr(block, 'text') and hasattr(block.text, 'value')
                ])

                self.logger.info(f"Message ID: {message_id}, Role: {role}, Content: {content_blocks}")

                formatted_messages.append({
                    'message_id': message_id,
                    'role': role,
                    'content': content_value
                })

            return formatted_messages
        except OpenAIError as e:
            self.logger.error(f"Failed to fetch messages for thread {thread_id}: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred while fetching messages: {str(e)}")
            raise

    def retrieve_message_object(self, thread_id, order='asc', limit=20):
        """
        Retrieves message objects from a specified thread.

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
        try:
            params = {'order': order, 'limit': limit}
            response = self.client.beta.threads.messages.list(thread_id=thread_id, **params)
            if not response.data:
                self.logger.info("No data found in the response or no messages.")
                return []

            self.logger.info(f"Retrieved {len(response.data)} messages from thread {thread_id}")
            messages = response.data
            return messages
        except OpenAIError as e:
            self.logger.error(f"Failed to fetch messages for thread {thread_id}: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred while fetching messages: {str(e)}")
            raise

    def process_and_print_messages(self, messages):
        """
        Processes and prints the role and content of each message.

        Args:
            messages (list): The list of message objects.
        """
        for message in messages:
            role = "Assistant" if message.role == "assistant" else "User"
            content_blocks = message.content
            content_value = " ".join([
                block.text.value for block in content_blocks if hasattr(block, 'text') and hasattr(block.text, 'value')
            ])

            print(f"{role}: {content_value}")
