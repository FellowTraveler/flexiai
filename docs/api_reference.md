# FlexiAI API Reference

## Overview

FlexiAI is a flexible AI framework for managing interactions with OpenAI and Azure OpenAI services. This document provides a comprehensive reference for the methods and functionalities available in the `flexiai_client.py` module.

## Table of Contents

- [FlexiAI Class](#flexiai-class)
  - [__init__](#__init__)
  - [_initialize_openai_client](#_initialize_openai_client)
  - [_initialize_azure_openai_client](#_initialize_azure_openai_client)
  - [create_thread](#create_thread)
  - [add_user_message](#add_user_message)
  - [wait_for_run_completion](#wait_for_run_completion)
  - [create_run](#create_run)
  - [create_advanced_run](#create_advanced_run)
  - [retrieve_messages](#retrieve_messages)
  - [retrieve_message_object](#retrieve_message_object)
  - [process_and_print_messages](#process_and_print_messages)
  - [handle_requires_action](#handle_requires_action)
  - [determine_action_type](#determine_action_type)
  - [execute_personal_function_with_arguments](#execute_personal_function_with_arguments)
  - [call_assistant_with_arguments](#call_assistant_with_arguments)
- [User-Defined Functions](#user-defined-functions)
  - [register_user_functions](#register_user_functions)
  - [get_function_mappings](#get_function_mappings)
  - [Example User-Defined Functions](#example-user-defined-functions)

## FlexiAI Class

The `FlexiAI` class is designed to manage interactions with OpenAI and Azure OpenAI services, handling tasks such as creating threads, adding messages, and running threads with specified assistants.

### \_\_init\_\_

Initializes the FlexiAI instance by setting up logging, determining the credential type, and initializing the appropriate OpenAI or Azure OpenAI client. Also sets up task management and function mappings.

#### Parameters
None

#### Raises
- `ValueError`: If the credential type is unsupported.

#### Example Usage
```python
from flexiai.core.flexiai_client import FlexiAI

# Initialize FlexiAI instance
flexiai = FlexiAI()
```

---

### _initialize_openai_client

Initializes the OpenAI client using the API key from the configuration.

#### Returns
- `OpenAI`: Initialized OpenAI client.

#### Raises
- `ValueError`: If the OpenAI API key is not set.
- `Exception`: If the client initialization fails.

#### Example Usage
```python
# This method is used internally by FlexiAI and is not typically called directly.
```

---

### _initialize_azure_openai_client

Initializes the Azure OpenAI client using the API key, endpoint, and API version from the configuration.

#### Returns
- `AzureOpenAI`: Initialized Azure OpenAI client.

#### Raises
- `ValueError`: If the Azure OpenAI API key, endpoint, or API version is not set.
- `Exception`: If the client initialization fails.

#### Example Usage
```python
# This method is used internally by FlexiAI and is not typically called directly.
```

---

### create_thread

Creates a new thread.

#### Returns
- `object`: The newly created thread object.

#### Raises
- `OpenAIError`: If the API call to create a new thread fails.
- `Exception`: If an unexpected error occurs.

#### Example Usage
```python
# Create a new thread
thread = flexiai.create_thread()
print("Thread ID:", thread.id)
```

---

### add_user_message

Adds a user message to a specified thread.

#### Parameters
- `thread_id` (str): The ID of the thread.
- `user_message` (str): The user's message content.

#### Returns
- `object`: The message object that was added to the thread.

#### Raises
- `OpenAIError`: If the API call to add a user message fails.
- `Exception`: If an unexpected error occurs.

#### Example Usage
```python
# Add a user message to a thread
thread_id = "your_thread_id"
user_message = "What is the capital of France?"
message = flexiai.add_user_message(thread_id, user_message)
print("Message ID:", message.id)
```

---

### wait_for_run_completion

Waits for any active run in the thread to complete.

#### Parameters
- `thread_id` (str): The ID of the thread.

#### Raises
- `OpenAIError`: If the API call to retrieve thread runs fails.
- `Exception`: If an unexpected error occurs.

#### Example Usage
```python
# Wait for any active run to complete
thread_id = "your_thread_id"
flexiai.wait_for_run_completion(thread_id)
```

---

### create_run

Creates and runs a thread with the specified assistant, handling required actions.

#### Parameters
- `assistant_id` (str): The ID of the assistant.
- `thread_id` (str): The ID of the thread.

#### Returns
- `object`: The run object.

#### Raises
- `OpenAIError`: If any API call within this function fails.
- `Exception`: If an unexpected error occurs.

#### Example Usage
```python
# Create and run a thread with a specified assistant
assistant_id = "your_assistant_id"
thread_id = "your_thread_id"
run = flexiai.create_run(assistant_id, thread_id)
print("Run ID:", run.id)
```

---

### create_advanced_run

Creates and runs a thread with the specified assistant, user message, and handles required actions.

#### Parameters
- `assistant_id` (str): The ID of the assistant.
- `thread_id` (str): The ID of the thread.
- `user_message` (str): The user's message content.

#### Returns
- `object`: The run object.

#### Raises
- `OpenAIError`: If any API call within this function fails.
- `Exception`: If an unexpected error occurs.

#### Example Usage
```python
# Create and run a thread with a specified assistant and user message
assistant_id = "your_assistant_id"
thread_id = "your_thread_id"
user_message = "What is the capital of France?"
run = flexiai.create_advanced_run(assistant_id, thread_id, user_message)
print("Run ID:", run.id)
```

---

### retrieve_messages

Retrieves the message objects from a specified thread.

#### Parameters
- `thread_id` (str): The ID of the thread.
- `order` (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'desc'.
- `limit` (int, optional): The number of messages to retrieve. Defaults to 20.

#### Returns
- `list`: A list of dictionaries containing the message ID, role, and content of each message.

#### Raises
- `OpenAIError`: If the API call to retrieve messages fails.
- `Exception`: If an unexpected error occurs.

#### Example Usage
```python
# Retrieve messages from a thread
thread_id = "your_thread_id"
messages = flexiai.retrieve_messages(thread_id, order='asc', limit=10)
for message in messages:
    print(f"{message['role']}: {message['content']}")
```

---

### retrieve_message_object

Retrieves the message objects from a specified thread without formatting.

#### Parameters
- `thread_id` (str): The ID of the thread.
- `order` (str, optional): The order in which to retrieve messages, either 'asc' or 'desc'. Defaults to 'asc'.
- `limit` (int, optional): The number of messages to retrieve. Defaults to 20.

#### Returns
- `list`: A list of message objects.

#### Raises
- `OpenAIError`: If the API call to retrieve messages fails.
- `Exception`: If an unexpected error occurs.

#### Example Usage
```python
# Retrieve raw message objects from a thread
thread_id = "your_thread_id"
messages = flexiai.retrieve_message_object(thread_id, order='asc', limit=10)
print(messages)
```

---

### process_and_print_messages

Processes the message objects and prints the role and content value of each message.

#### Parameters
- `messages` (list): The list of message objects.

#### Example Usage
```python
# Process and print messages
messages = flexiai.retrieve_message_object(thread_id, order='asc', limit=10)
flexiai.process_and_print_messages(messages)
```

---

### handle_requires_action

Handles required actions from a run.

This method processes the required actions for a given run. It executes the necessary functions and submits the outputs back to the OpenAI API or Azure OpenAI.

#### Parameters
- `run` (object): The run object requiring actions.
- `assistant_id` (str): The ID of the assistant.
- `thread_id` (str): The ID of the thread.

#### Raises
- `OpenAIError`: If an error occurs when interacting with the OpenAI API.
- `Exception`: If an unexpected error occurs during the process.

#### Example Usage
```python
# This method is used internally by FlexiAI and is not typically called directly.
```

---

### determine_action_type

Determines the type of action required based on the function's name.

#### Parameters
- `function_name` (str): The name of the function.

#### Returns
- `str`: The type of action, either 'call_assistant' or 'personal_function'.

#### Example Usage
```python
# This method is used internally by FlexiAI and is not typically called directly.
```

---

### execute_personal_function_with_arguments

Dynam

ically executes a function from the function_mapping based on the provided function name and supplied arguments.

#### Parameters
- `function_name` (str): The name of the function to execute.
- `**arguments`: The arguments to pass to the function.

#### Returns
- `tuple`: A tuple containing the status (bool), message (str), and result (any).

#### Raises
- `Exception`: If the function execution fails.

#### Example Usage
```python
# This method is used internally by FlexiAI and is not typically called directly.
```

---

### call_assistant_with_arguments

Routes the function call to the appropriate assistant or internal function.

#### Parameters
- `function_name` (str): The name of the function to call.
- `**arguments`: The arguments to pass to the function.

#### Returns
- `tuple`: A tuple containing the status (bool), message (str), and result (any).

#### Raises
- `ValueError`: If the function is not found.
- `Exception`: If the function execution fails.

#### Example Usage
```python
# This method is used internally by FlexiAI and is not typically called directly.
```

---

## User-Defined Functions

FlexiAI supports the integration of user-defined functions to extend its capabilities. This section provides an overview of how user functions are registered and utilized within the framework.

### register_user_functions

Registers user-defined functions by merging them with existing function mappings.

#### Parameters
- `personal_function_mapping` (dict): The personal function mappings to be updated.
- `assistant_function_mapping` (dict): The assistant function mappings to be updated.

#### Returns
- `tuple`: A tuple containing the updated personal function mappings and assistant function mappings.

#### Example Usage
```python
from flexiai.assistant.function_mapping import register_user_functions

# Register user functions
personal_function_mapping = {}
assistant_function_mapping = {}
personal_function_mapping, assistant_function_mapping = register_user_functions(personal_function_mapping, assistant_function_mapping)
```

---

### get_function_mappings

Gets the function mappings for personal and assistant functions, including both internal and user-defined functions.

#### Returns
- `tuple`: A tuple containing the personal function mappings and assistant function mappings.

#### Example Usage
```python
from flexiai.assistant.function_mapping import get_function_mappings

# Get function mappings
personal_function_mapping, assistant_function_mapping = get_function_mappings()
```

---

### Example User-Defined Functions

Here are some examples of user-defined functions that can be registered with FlexiAI.

```python
# user_flexiai_rag/user_task_manager.py
import logging
from flexiai.config.logging_config import setup_logging
import subprocess
import urllib.parse

# Set up logging using your custom configuration
setup_logging(root_level=logging.INFO, file_level=logging.DEBUG, console_level=logging.ERROR)

class UserTaskManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def search_youtube(self, query):
        if not query:
            return {
                "status": False,
                "message": "Query cannot be empty.",
                "result": None
            }

        try:
            query_normalized = query.replace(" ", "+")
            query_encoded = urllib.parse.quote(query_normalized)
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

# user_flexiai_rag/user_function_mapping.py
from user_flexiai_rag.user_task_manager import UserTaskManager

def register_user_tasks():
    task_manager = UserTaskManager()

    personal_function_mapping = {
        'search_youtube': task_manager.search_youtube,
    }

    assistant_function_mapping = {
    }

    return personal_function_mapping, assistant_function_mapping
```
