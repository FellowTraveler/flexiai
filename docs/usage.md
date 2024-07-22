# Usage Guide

This guide will help you understand how to use the FlexiAI framework to interact with AI assistants. Below are step-by-step instructions and an example script to get you started.

## Table of Contents

- [Basic Usage](#basic-usage)
- [Running the Example Script](#running-the-example-script)
- [Customizing the Script](#customizing-the-script)

---

## Basic Usage

FlexiAI allows you to create and manage AI assistants that can handle various tasks. The following sections provide a basic overview of how to set up and use an AI assistant with FlexiAI.

## Running the Example Script

Below is an example script (`chat.py`) that demonstrates how to use FlexiAI to interact with an AI assistant. The script sets up logging, initializes FlexiAI, creates a new thread for the assistant, and enters a loop to continuously get user input and interact with the assistant.

### `chat.py`

```python
import logging
from flexiai.core.flexiai_client import FlexiAI
from flexiai.config.logging_config import setup_logging
from flexiai.core.utils.helpers import HelperFunctions

# Define global variables for role names
USER_ROLE_NAME = "You"
ASSISTANT_ROLE_NAME = "Alpha"

def main():
    # Set up logging using your custom configuration
    setup_logging()
    
    # Initialize FlexiAI
    flexiai = FlexiAI()

    # Use the given assistant ID
    assistant_id = 'asst_XXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with the actual assistant ID

    # Initialize MultiAgentSystemManager
    multi_agent_system = flexiai.multi_agent_system

    # Initialize a new thread for the given assistant ID
    try:
        thread_id, status = multi_agent_system.check_for_thread_and_status(assistant_id)
        if not thread_id:
            thread_id = multi_agent_system.thread_initialization(assistant_id)
            if thread_id:
                logging.info(f"Initialized thread with ID: {thread_id} for assistant ID: {assistant_id}")
            else:
                logging.error(f"Failed to initialize thread for assistant ID: {assistant_id}")
                return
        else:
            logging.info(f"Thread with ID: {thread_id} already exists for assistant ID: {assistant_id}, Status: {status}")
    except Exception as e:
        logging.error(f"Error initializing thread for assistant ID {assistant_id}: {e}", exc_info=True)
        return

    # Variable to store all messages
    all_messages = []
    last_retrieved_id = None

    # Loop to continuously get user input and interact with the assistant
    while True:
        # Get user input
        user_message = input(f"{USER_ROLE_NAME}: ")

        # Exit the loop if the user types 'exit'
        if user_message.lower() == 'exit':
            print("Exiting...")
            break

        logging.info(f"User message: {user_message}")

        # Run the thread and handle required actions
        try:
            flexiai.create_and_monitor_run(assistant_id, thread_id, user_message)
            
            # Retrieve messages dynamically after the run
            retrieved_messages_after_run = flexiai.retrieve_messages_dynamically(
                thread_id, order='asc', limit=20, retrieve_all=False, last_retrieved_id=last_retrieved_id
            )
            last_retrieved_id = retrieved_messages_after_run[-1].id if retrieved_messages_after_run else last_retrieved_id
            
            # Clear console and print the stored messages in the desired format
            HelperFunctions.clear_console()
            HelperFunctions.format_and_track_messages(all_messages, retrieved_messages_after_run, USER_ROLE_NAME, ASSISTANT_ROLE_NAME)
        except Exception as e:
            logging.error(f"Error running thread: {e}", exc_info=True)

if __name__ == "__main__":
    main()
```

### Steps to Run the Script

1. **Set up your environment**: Ensure you have followed the setup instructions in the [Setup Guide](setup.md).

2. **Save the script**: Save the above script as `chat.py` in your project directory.

3. **Run the script**: Execute the script using Python.

    ```bash
    python chat.py
    ```

4. **Interact with the assistant**: Enter your messages when prompted. Type 'exit' to end the interaction.

## Customizing the Script

You can customize the `chat.py` script to better suit your needs:

- **Assistant ID**: Replace `'asst_XXXXXXXXXXXXXXXXXXXXXXXXX'` with your actual assistant ID.
- **Role Names**: Change the `USER_ROLE_NAME` and `ASSISTANT_ROLE_NAME` variables to customize how the roles are displayed.
- **Logging**: Modify the `setup_logging()` function call to configure logging according to your preferences.

For more detailed usage examples and advanced functionalities, refer to the [Usage Guide](usage.md).


---
