# user_flexiai_rag/user_function_mapping.py
import logging
from flexiai.config.logging_config import setup_logging
from user_flexiai_rag.user_task_manager import UserTaskManager

# Set up logging using your custom configuration
setup_logging(root_level=logging.INFO, file_level=logging.INFO, console_level=logging.ERROR)

# Initialize logger
logger = logging.getLogger(__name__)

def register_user_tasks():
    """
    Register user-defined tasks with the FlexiAI framework.

    Returns:
        tuple: A tuple containing the personal function mappings and assistant function mappings.
    """
    task_manager = UserTaskManager()

    personal_function_mapping = {
        'search_youtube': task_manager.search_youtube,
        'identify_person': task_manager.identify_person,
        'manage_product': task_manager.manage_product
        # Add other functions that call assistant personal functions
    }

    assistant_function_mapping = {
        # Add other functions that call assistants here -> the functions must end with "_assistant"
    }

    logger.info("Registering user tasks")
    logger.info(f"USER RAG - Personal Function Mappings: {personal_function_mapping.keys()}")
    logger.info(f"USER RAG - Call Assistant Function Mappings: {assistant_function_mapping.keys()}")

    return personal_function_mapping, assistant_function_mapping
