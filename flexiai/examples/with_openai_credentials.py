# examples/test_openai_credentials.py
import logging
import os
import platform
from flexiai.core.flexiai_client import FlexiAI
from flexiai.config.logging_config import setup_logging

def clear_console():
    """Clears the console depending on the operating system."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    # Set up logging using your custom configuration
    # Adjust the logging levels as per your requirements
    setup_logging(root_level=logging.DEBUG, file_level=logging.DEBUG, console_level=logging.ERROR)

    # Initialize FlexiAI
    flexiai = FlexiAI()

    # Use the given assistant ID
    assistant_id = 'asst_AWAVO511bAbTVEdOvLNWitoT' # Replace with the actual assistant ID           # Alina
    
    # Create a new thread
    try:
        thread = flexiai.create_thread()
        thread_id = thread.id
        logging.info(f"Created thread with ID: {thread_id}")
    except Exception as e:
        logging.error(f"Error creating thread: {e}")
        return

    # Variable to store all messages
    all_messages = []
    seen_message_ids = set()

    # Loop to continuously get user input and interact with the assistant
    while True:
        # Get user input
        user_message = input("You: ")

        # Exit the loop if the user types 'exit'
        if user_message.lower() == 'exit':
            print("Exiting...")
            break

        # Run the thread and handle required actions
        try:
            flexiai.create_advanced_run(assistant_id, thread_id, user_message)
            messages = flexiai.retrieve_messages(thread_id, limit=2)  
            
            # Store the extracted messages
            for msg in messages:
                if msg['message_id'] not in seen_message_ids:
                    all_messages.append(msg)
                    seen_message_ids.add(msg['message_id'])

            # Clear console and print the stored messages in the desired format
            clear_console()
            for msg in all_messages:
                role = "🤖 Assistant" if msg['role'] == "assistant" else "🧑 You"
                print(f"{role}: {msg['content']}")
        except Exception as e:
            logging.error(f"Error running thread: {e}")

if __name__ == "__main__":
    main()
