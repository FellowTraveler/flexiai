# user_flexiai_rag/user_function_mapping.py
import logging
from user_flexiai_rag.user_task_manager import UserTaskManager

logger = logging.getLogger(__name__)

def register_user_tasks(multi_agent_system, run_manager):
    """
    Registers user-defined tasks with the FlexiAI framework.

    This function initializes the UserTaskManager and sets up mappings for personal and assistant functions.
    It logs the registration process and returns the function mappings.

    Args:
        multi_agent_system (MultiAgentSystemManager): The multi-agent system manager instance.
        run_manager (RunManager): The run manager instance.

    Returns:
        tuple: A tuple containing two dictionaries:
            - user_personal_functions (dict): Mapping of personal function names to their implementations.
            - user_assistant_functions (dict): Mapping of assistant function names to their implementations.
    """
    task_manager = UserTaskManager(multi_agent_system, run_manager)
    
    user_personal_functions = {
        # MAS functions for each agent:
        'save_processed_content': task_manager.save_processed_content,
        'load_processed_content': task_manager.load_processed_content,
        'initialize_agent': task_manager.initialize_agent,
        # Functions used by your assistants
        'search_youtube': task_manager.search_youtube,
    }
    
    user_assistant_functions = {
       'communicate_with_assistant': task_manager.continue_conversation_with_assistant,
       # Other designs for MAS or other assistants
    }

    logger.info("Registering user tasks")
    logger.debug(f"User personal functions: {list(user_personal_functions.keys())}")
    logger.debug(f"User assistant functions: {list(user_assistant_functions.keys())}")

    return user_personal_functions, user_assistant_functions
