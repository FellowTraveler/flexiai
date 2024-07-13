# user_flexiai_rag/user_function_mapping.py
import logging
from user_flexiai_rag.user_task_manager import UserTaskManager

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
        # Add other functions that call assistant personal functions
    }

    assistant_function_mapping = {
        # Add other functions that call assistants here -> the functions must end with "_assistant"
    }

    logger.info("Registering user tasks")
    logger.info(f"USER RAG - Personal Function Mappings: {personal_function_mapping.keys()}")
    logger.info(f"USER RAG - Call Assistant Function Mappings: {assistant_function_mapping.keys()}")

    return personal_function_mapping, assistant_function_mapping
