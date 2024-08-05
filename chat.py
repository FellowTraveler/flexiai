# chat.py
import logging
from flexiai.core.flexiai_client import FlexiAI
from flexiai.config.logging_config import setup_logging
from flexiai.core.utils.helpers import HelperFunctions


# Define global variables for role names
USER_ROLE_NAME = "You"
ASSISTANT_ROLE_NAME = "Assistant"


def main():
    # Set up logging using your custom configuration
    setup_logging()
    
    # Initialize FlexiAI
    flexiai = FlexiAI()

    # Use the given assistant ID
    assistant_id = 'asst_XXXXXXXXXXXXXXXXXXXX'  # Update with your Assistant ID

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

        # logging.info(f"User message: {user_message}")

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
    