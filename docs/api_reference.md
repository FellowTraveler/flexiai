# API Reference

This document provides a comprehensive reference for the FlexiAI framework's API. It includes detailed descriptions of the main classes, methods, and their usage to help developers integrate and utilize FlexiAI effectively.

## Table of Contents

- [FlexiAI](#flexiai)
  - [Class Definition](#class-definition)
  - [Methods](#methods)
    - [`__init__`](#__init__)
    - [`create_thread`](#create_thread)
    - [`retrieve_thread`](#retrieve_thread)
    - [`update_thread`](#update_thread)
    - [`delete_thread`](#delete_thread)
    - [`attach_assistant_to_thread`](#attach_assistant_to_thread)
    - [`add_user_message`](#add_user_message)
    - [`wait_for_run_completion`](#wait_for_run_completion)
    - [`create_run`](#create_run)
    - [`create_advanced_run`](#create_advanced_run)
    - [`create_and_monitor_run`](#create_and_monitor_run)
    - [`retrieve_messages`](#retrieve_messages)
    - [`retrieve_message_object`](#retrieve_message_object)
    - [`process_and_print_messages`](#process_and_print_messages)
    - [`assistant_transformer`](#assistant_transformer)
    - [`create_vector_store`](#create_vector_store)
    - [`upload_files_and_poll`](#upload_files_and_poll)
    - [`update_assistant_with_vector_store`](#update_assistant_with_vector_store)
    - [`list_vector_stores`](#list_vector_stores)
    - [`retrieve_vector_store_details`](#retrieve_vector_store_details)
    - [`delete_vector_store`](#delete_vector_store)
    - [`list_files_in_vector_store`](#list_files_in_vector_store)
    - [`retrieve_file_batch_details`](#retrieve_file_batch_details)
    - [`search_files_in_vector_store`](#search_files_in_vector_store)
    - [`call_parallel_functions`](#call_parallel_functions)
    - [`add_messages_dynamically`](#add_messages_dynamically)
    - [`retrieve_messages_dynamically`](#retrieve_messages_dynamically)
- [CredentialManager](#credentialmanager)
  - [Class Definition](#class-definition-1)
  - [Methods](#methods-1)
    - [`__init__`](#__init__-1)
    - [`_get_client`](#_get_client)
- [CredentialStrategy](#credentialstrategy)
  - [Class Definition](#class-definition-2)
  - [Methods](#methods-2)
    - [`get_client`](#get_client)

## FlexiAI

The `FlexiAI` class is the core of the FlexiAI framework, providing methods to manage threads, runs, and message retrieval. This class enables the integration of both OpenAI and Azure OpenAI services.

### Class Definition

```python
class FlexiAI:
    def __init__(self):
        # Initialization code here

    def create_thread(self):
        # Method to create a new thread

    def retrieve_thread(self, thread_id):
        # Method to retrieve a specific thread

    def update_thread(self, thread_id, metadata=None, tool_resources=None):
        # Method to update a thread

    def delete_thread(self, thread_id):
        # Method to delete a thread

    def attach_assistant_to_thread(self, assistant_id, thread_id):
        # Method to attach an assistant to a thread

    def add_user_message(self, thread_id, user_message):
        # Method to add a user message to a thread

    def wait_for_run_completion(self, thread_id):
        # Method to wait for run completion

    def create_run(self, assistant_id, thread_id):
        # Method to create a run

    def create_advanced_run(self, assistant_id, thread_id, user_message):
        # Method to create an advanced run with a user message

    def create_and_monitor_run(self, assistant_id, thread_id, user_message=None, role=None, metadata=None):
        # Method to create and monitor a run

    def retrieve_messages(self, thread_id, order='desc', limit=20):
        # Method to retrieve messages from a thread

    def retrieve_message_object(self, thread_id, order='asc', limit=20):
        # Method to retrieve message objects from a thread

    def process_and_print_messages(self, messages):
        # Method to process and print messages

    def assistant_transformer(self, thread_id, new_assistant_id):
        # Method to attach a new assistant to an existing thread

    def create_vector_store(self, name):
        # Method to create a new vector store

    def upload_files_and_poll(self, vector_store_id, file_paths):
        # Method to upload files to a vector store

    def update_assistant_with_vector_store(self, assistant_id, vector_store_id):
        # Method to update an assistant to use the new vector store

    def list_vector_stores(self):
        # Method to list all vector stores

    def retrieve_vector_store_details(self, vector_store_id):
        # Method to retrieve details about a vector store

    def delete_vector_store(self, vector_store_id):
        # Method to delete a vector store

    def list_files_in_vector_store(self, vector_store_id, batch_id):
        # Method to list all files in a vector store

    def retrieve_file_batch_details(self, vector_store_id, batch_id):
        # Method to retrieve details of a file batch in a vector store

    def search_files_in_vector_store(self, vector_store_id, query):
        # Method to search for files in a vector store

    def call_parallel_functions(self, tasks):
        # Method to run parallel tool calls in an asynchronous event loop

    def add_messages_dynamically(self, thread_id, messages, role=None, metadata=None):
        # Method to add multiple user messages dynamically

    def retrieve_messages_dynamically(self, thread_id, order='asc', limit=20, retrieve_all=False, last_retrieved_id=None):
        # Method to retrieve messages dynamically from a thread
```

### Methods

#### `__init__`

Initializes the `FlexiAI` instance. Sets up necessary configurations and dependencies.

#### `create_thread`

Creates a new thread using the `ThreadManager`.

- **Returns**: 
  - `str`: The ID of the newly created thread.

#### `retrieve_thread`

Retrieves details of a specific thread by its ID using the `ThreadManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the thread to retrieve.

- **Returns**: 
  - `object`: The thread object.

#### `update_thread`

Updates a thread with the given details using the `ThreadManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the thread to update.
  - `metadata` (dict, optional): Metadata to update for the thread.
  - `tool_resources` (dict, optional): Tool resources to update for the thread.

- **Returns**: 
  - `object`: The updated thread object.

#### `delete_thread`

Deletes a thread by its ID using the `ThreadManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the thread to delete.

- **Returns**: 
  - `bool`: True if the thread was deleted successfully, False otherwise.

#### `attach_assistant_to_thread`

Attaches an assistant to an existing thread using the `ThreadManager`.

- **Parameters**:
  - `assistant_id` (str): The ID of the assistant.
  - `thread_id` (str): The ID of the thread.

- **Returns**: 
  - `object`: The run object indicating the assistant has been attached.

#### `add_user_message`

Adds a user message to a specified thread using the `MessageManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the thread.
  - `user_message` (str): The content of the user's message.

- **Returns**: 
  - `object`: The message object that was added to the thread.

#### `wait_for_run_completion`

Waits for the completion of a run on a specified thread using the `RunManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the thread to wait for run completion.

#### `create_run`

Creates a new run for a specified assistant and thread using the `RunManager`.

- **Parameters**:
  - `assistant_id` (str): The ID of the assistant.
  - `thread_id` (str): The ID of the thread.

- **Returns**: 
  - `object`: The run object if successful, None otherwise.

#### `create_advanced_run`

Creates an advanced run with a user message for a specified assistant and thread using the `RunManager`.

- **Parameters**:
  - `assistant_id` (str): The ID of the assistant.
  - `thread_id` (str): The ID of the thread.
  - `user_message` (str): The user's message content.

- **Returns**: 
  - `object`: The run object if successful, None otherwise.

#### `create_and_monitor_run`

Creates and runs a thread with the specified assistant, optionally adding a user message, and monitors its status until completion or failure using the `RunManager`.

- **Parameters**:
  - `assistant_id` (str): The ID of the assistant.
  - `thread_id` (str): The ID of the thread.
  - `user_message` (str, optional): The user's message content to add before creating the run.
  - `role` (str, optional): The role of the message sender. Defaults to

 'user'.
  - `metadata` (dict, optional): Metadata to include with the message.

- **Returns**: 
  - `None`

#### `retrieve_messages`

Retrieves messages from a specified thread using the `MessageManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the thread.
  - `order` (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'desc'.
  - `limit` (int, optional): The number of messages to retrieve. Defaults to 20.

- **Returns**: 
  - `list`: A list of dictionaries containing the message ID, role, and content of each message.

#### `retrieve_message_object`

Retrieves message objects from a specified thread using the `MessageManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the thread.
  - `order` (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'asc'.
  - `limit` (int, optional): The number of messages to retrieve. Defaults to 20.

- **Returns**: 
  - `list`: A list of message objects.

#### `process_and_print_messages`

Processes and prints the role and content of each message using the `MessageManager`.

- **Parameters**:
  - `messages (list)`: The list of message objects.

#### `assistant_transformer`

Attaches a new assistant to an existing thread and runs the thread to speak with the new assistant using the `RunManager`.

- **Parameters**:
  - `thread_id` (str): The ID of the existing thread.
  - `new_assistant_id` (str): The ID of the new assistant to attach.

- **Returns**: 
  - `object`: The final run object indicating the result of the interaction.

#### `create_vector_store`

Creates a new vector store with a specified name using the `VectorStoreManager`.

- **Parameters**:
  - `name` (str): The name of the vector store.

- **Returns**: 
  - `object`: The newly created vector store object.

#### `upload_files_and_poll`

Uploads files to a vector store and polls the status of the file batch for completion using the `VectorStoreManager`.

- **Parameters**:
  - `vector_store_id` (str): The ID of the vector store.
  - `file_paths` (list): A list of file paths to upload.

- **Returns**: 
  - `object`: The file batch object after upload and completion.

#### `update_assistant_with_vector_store`

Updates an assistant to use the new vector store using the `VectorStoreManager`.

- **Parameters**:
  - `assistant_id` (str): The ID of the assistant.
  - `vector_store_id` (str): The ID of the vector store.

- **Returns**: 
  - `object`: The updated assistant object.

#### `list_vector_stores`

Retrieves a list of all existing vector stores using the `VectorStoreManager`.

- **Returns**: 
  - `list`: A list of vector store objects.

#### `retrieve_vector_store_details`

Retrieves detailed information about a specific vector store using the `VectorStoreManager`.

- **Parameters**:
  - `vector_store_id` (str): The ID of the vector store.

- **Returns**: 
  - `object`: The vector store object with detailed information.

#### `delete_vector_store`

Deletes a vector store using the `VectorStoreManager`.

- **Parameters**:
  - `vector_store_id` (str): The ID of the vector store.

- **Returns**: 
  - `bool`: True if the vector store was deleted successfully, False otherwise.

#### `list_files_in_vector_store`

Lists all files that have been uploaded to a specific vector store using the `VectorStoreManager`.

- **Parameters**:
  - `vector_store_id` (str): The ID of the vector store.
  - `batch_id` (str): The ID of the file batch.

- **Returns**: 
  - `list`: A list of files in the vector store.

#### `retrieve_file_batch_details`

Retrieves the status and details of a specific file batch within a vector store using the `VectorStoreManager`.

- **Parameters**:
  - `vector_store_id` (str): The ID of the vector store.
  - `batch_id` (str): The ID of the file batch.

- **Returns**: 
  - `object`: The file batch object with detailed information.

#### `search_files_in_vector_store`

Searches for files in a vector store based on a query using the `VectorStoreManager`.

- **Parameters**:
  - `vector_store_id` (str): The ID of the vector store.
  - `query` (str): The search query.

- **Returns**: 
  - `list`: A list of search results.

#### `call_parallel_functions`

Wrapper to run parallel tool calls in an asynchronous event loop.

- **Parameters**:
  - `tasks` (list): A list of dictionaries where each dictionary contains:
    - `function_name` (str): The name of the function to call.
    - `parameters` (dict): The parameters to pass to the function.

- **Returns**: 
  - `list`: A list of results from each function call.

#### `add_messages_dynamically`

Adds multiple user messages to a specified thread dynamically with optional metadata.

- **Parameters**:
  - `thread_id` (str): The ID of the thread.
  - `messages` (list): A list of dictionaries containing the message content and optional metadata. Each dictionary should have the following structure:
    ```json
    {
        "content": "Message content",
        "metadata": {"key": "value"} (optional)
    }
    ```
  - `role` (str, optional): The role of the message sender. Defaults to None.
  - `metadata` (dict, optional): Default metadata to include with each message if not provided in individual messages.

- **Returns**: 
  - `list`: A list of message objects that were added to the thread.

- **Raises**: 
  - `OpenAIError`: If the API call to add a message fails.
  - `Exception`: If an unexpected error occurs.

#### `retrieve_messages_dynamically`

Retrieves messages from a specified thread dynamically.

- **Parameters**:
  - `thread_id` (str): The ID of the thread from which to retrieve messages.
  - `order` (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'asc'.
  - `limit` (int, optional): The maximum number of messages to retrieve in a single request. Defaults to 20.
  - `retrieve_all` (bool, optional): Whether to retrieve all messages in the thread. If False, only retrieves up to the limit. Defaults to False.
  - `last_retrieved_id` (str, optional): The ID of the last retrieved message to fetch messages after it. Defaults to None.

- **Returns**: 
  - `list`: A list of message objects retrieved from the thread.

- **Raises**: 
  - `OpenAIError`: If the API call to retrieve messages fails.
  - `Exception`: If an unexpected error occurs.

## CredentialManager

The `CredentialManager` class manages the credentials and provides the appropriate client based on the credential type.

### Class Definition

```python
class CredentialManager:
    def __init__(self):
        self.credential_type = config.CREDENTIAL_TYPE
        self.client = self._get_client()

    def _get_client(self):
        # Method to get the appropriate client based on credential type
```

### Methods

#### `__init__`

Initializes the `CredentialManager` instance. Sets up the credential type and retrieves the client.

#### `_get_client`

Gets the appropriate client based on the credential type.

- **Returns**: 
  - `Client`: The API client for the specified credential type.

## CredentialStrategy

The `CredentialStrategy` class is an abstract base class for credential strategies. This class defines the interface for different credential strategies to get their respective API clients.

### Class Definition

```python
class CredentialStrategy(ABC):
    @abstractmethod
    def get_client(self):
        # Abstract method to get the API client
```

### Methods

#### `get_client`

Abstract method to get the API client. This method should be implemented by all subclasses to return the appropriate client for the given credential strategy.

- **Returns**: 
  - `Client`: The API client for the specific credential strategy.


---
