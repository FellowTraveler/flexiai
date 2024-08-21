# user_flexiai_rag/user_functions_mapping.py
import logging
from user_flexiai_rag.user_functions_manager import FunctionsManager

logger = logging.getLogger(__name__)

async def map_user_functions():
    """
    Maps user-defined functions to FlexiAI asynchronously and efficiently, ready for future calls.
    
    This function should be awaited when called by the FunctionMapping class.
    """
    logger.info("Mapping user-defined functions...")

    # Initialize the FunctionsManager without run_manager
    user_functions_manager = FunctionsManager()

    # Map user-defined personal and assistant functions
    user_personal_functions = {
        'search_youtube': user_functions_manager.search_youtube,
    }

    user_assistant_functions = {
        #  Functions to call other assistants, must end with '_assistant'
    }

    logger.info(f"User personal functions are: {list(user_personal_functions.keys())}")
    logger.info(f"User assistant functions are: {list(user_assistant_functions.keys())}")

    # Return the mappings
    return user_personal_functions, user_assistant_functions
