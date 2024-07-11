# FlexiAI Usage Guide

## Table of Contents
1. [Initial Setup and Configuration](#initial-setup-and-configuration)
2. [Import Necessary Modules](#import-necessary-modules)
3. [Define the Assistant ID](#define-the-assistant-id)
4. [Create a New Thread](#create-a-new-thread)
5. [Variable to Store All Messages](#variable-to-store-all-messages)
6. [Add a User Message and Print the Message](#add-a-user-message-and-print-the-message)
7. [Create a Run to Get the Assistant's Response](#create-a-run-to-get-the-assistants-response)
8. [Retrieve and Store the Assistant's Response](#retrieve-and-store-the-assistants-response)
9. [Add Another User Message and Print the Message](#add-another-user-message-and-print-the-message)
10. [Create Another Run to Get the Assistant's Response](#create-another-run-to-get-the-assistants-response)
11. [Retrieve and Print the Last Messages](#retrieve-and-print-the-last-messages)
12. [Example to Show Different Formats for Retrieving Messages](#example-to-show-different-formats-for-retrieving-messages)

## Initial Setup and Configuration
- Changing and Verifying the Working Directory for Project Setup
- This section ensures that your working directory is set to the project root.

```python
import sys
import os

# Check current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# Change to your project root directory
project_root = '/your/project/directory'
os.chdir(project_root)
print(f"Changed Directory to: {os.getcwd()}")

# Add project root directory to sys.path
sys.path.append(project_root)
print(f"Project root added to sys.path")
```

## Import Necessary Modules
- Import required modules and set up logging.

```python
import logging
from flexiai.core.flexiai_client import FlexiAI
from flexiai.config.logging_config import setup_logging
from flexiai.core.utils.helpers import show_json, print_messages_as_json, print_run_details

# Setup logging using the predefined configuration
setup_logging(root_level=logging.DEBUG, file_level=logging.DEBUG, console_level=logging.ERROR)

# Initialize FlexiAI
flexiai = FlexiAI()
```

## Define the Assistant ID
- Define the assistant ID that will be used for interactions.

```python
# Use the given assistant ID
assistant_id = 'asst_AWAVO511bAbTVEdOvLNWitoT'  # Replace with the actual assistant ID
```

## Create a New Thread
- Create a new thread to start a conversation.

```python
thread = flexiai.create_thread()
thread_id = thread.id
print(f"Thread Created with ID: {thread_id}")
```

## Variable to Store All Messages
- Initialize variables to store messages and keep track of processed message IDs.

```python
all_messages = []
seen_message_ids = set()
```

## Add a User Message and Print the Message
- Add a message from the user to the thread and print the message details.

```python
user_message = "Tell me about the Eiffel Tower."
message = flexiai.add_user_message(thread_id=thread_id, user_message=user_message)
show_json(message)

# Store the message
all_messages.append({"role": "user", "content": user_message})
seen_message_ids.add(message.id)
```

## Create a Run to Get the Assistant's Response
- Create a run to get the response from the assistant.

```python
run = flexiai.create_run(assistant_id=assistant_id, thread_id=thread_id)
print_run_details(run)
```

## Retrieve and Store the Assistant's Response
- Retrieve messages from the thread and store them in a list.

```python
messages = flexiai.retrieve_messages(thread_id=thread_id, order='desc', limit=2)

for msg in messages:
    if msg['message_id'] not in seen_message_ids:
        all_messages.append(msg)
        seen_message_ids.add(msg['message_id'])

# Print all messages
for msg in all_messages:
    role = "🤖 Assistant" if msg['role'] == "assistant" else "🧑 You"
    print(f"{role}: {msg['content']}")
```

## Add Another User Message and Print the Message
- Add another message from the user to the thread and print the message details.
- This message will trigger the `search_youtube` function.

```python
user_message = "I would like to search on YouTube these keywords: Eiffel Tower."
message = flexiai.add_user_message(thread_id=thread_id, user_message=user_message)
show_json(message)

# Store the message
all_messages.append({"role": "user", "content": user_message})
seen_message_ids.add(message.id)
```

## Create Another Run to Get the Assistant's Response
- Create another run to get the assistant's response to the new message.
- The `create_run` function can handle `requires_action` and will trigger a search on YouTube with the `search_youtube` function if it is mapped in `user_flexiai_rag/user_function_mapping.py` and stored in `user_flexiai_rag/user_task_manager.py`.

```python
run = flexiai.create_run(assistant_id=assistant_id, thread_id=thread_id)
show_json(run)
```

## Retrieve and Print the Last Messages
- Retrieve the latest messages from the thread and print them.

```python
messages = flexiai.retrieve_messages(thread_id=thread_id, order='desc', limit=2)

for msg in messages:
    if msg['message_id'] not in seen_message_ids:
        all_messages.append(msg)
        seen_message_ids.add(msg['message_id'])

# Print all messages
for msg in all_messages:
    role = "🤖 Assistant" if msg['role'] == "assistant" else "🧑 You"
    print(f"{role}: {msg['content']}")
```

## Example to Show Different Formats for Retrieving Messages
- This section demonstrates two different formats for retrieving messages from a thread using FlexiAI.

### Retrieve Messages
- The `retrieve_messages` function fetches messages in a list of formatted dictionaries.
- The `order='desc'` argument specifies that the messages are retrieved in descending order (newest first).
- `limit=20` specifies the maximum number of messages to retrieve.
- The retrieved messages are printed to show their format.

```python
print(100*'=')
messages = flexiai.retrieve_messages(thread_id=thread_id, order='desc', limit=20)
print(messages)
print(100*'=')
```

### Retrieve Message Objects
- The `retrieve_message_object` function fetches the entire message objects from the thread.
- The `order='asc'` argument specifies that the messages are retrieved in ascending order (oldest first).
- `limit=20` specifies the maximum number of message objects to retrieve.
- The retrieved message objects are printed to show their detailed structure.

```python
messages = flexiai.retrieve_message_object(thread_id=thread_id, order='asc', limit=20)
print_messages_as_json(messages)
```
