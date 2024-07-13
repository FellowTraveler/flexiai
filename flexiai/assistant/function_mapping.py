# flexiai/assistant/function_mapping.py
import importlib
import logging
import os
import sys
import glob

logger = logging.getLogger(__name__)

class FunctionMapper:
    """
    Class to handle the function mappings for personal and assistant functions,
    including both internal and user-defined functions.
    """

    def __init__(self):
        """
        Initializes the FunctionMapper instance, automatically detecting the path to user-defined functions.
        """
        self.user_directory = self._detect_user_directory()

    def _detect_user_directory(self):
        """
        Detects the user directory path where user-defined functions are stored.

        Returns:
            str: The detected user directory path.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        user_directory = os.path.join(current_dir, '..', '..', 'user_flexiai_rag')
        return os.path.normpath(user_directory)

    def get_function_mappings(self):
        """
        Get the function mappings for personal and assistant functions, including both internal and user-defined functions.

        Returns:
            tuple: A tuple containing the personal function mappings and assistant function mappings.
        """
        personal_function_mapping = {}
        assistant_function_mapping = {}
        return personal_function_mapping, assistant_function_mapping

    def register_user_functions(self, personal_function_mapping, assistant_function_mapping):
        """
        Register user-defined functions by merging them with existing function mappings.

        Args:
            personal_function_mapping (dict): The personal function mappings to be updated.
            assistant_function_mapping (dict): The assistant function mappings to be updated.

        Returns:
            tuple: A tuple containing the updated personal function mappings and assistant function mappings.
        """
        try:
            user_modules = self._load_user_modules()
            for module in user_modules:
                if hasattr(module, 'register_user_tasks'):
                    user_personal_functions, user_assistant_functions = module.register_user_tasks()
                    personal_function_mapping.update(user_personal_functions)
                    assistant_function_mapping.update(user_assistant_functions)
                    logger.info(f"Successfully registered user functions from {module.__name__}")

        except Exception as e:
            logger.error(f"Failed to register user functions: {e}", exc_info=True)
            raise

        return personal_function_mapping, assistant_function_mapping

    def _load_user_modules(self):
        """
        Load user modules dynamically from the user directory.

        Returns:
            list: A list of loaded user modules.
        """
        sys.path.insert(0, self.user_directory)
        module_files = glob.glob(os.path.join(self.user_directory, "*.py"))
        modules = []
        for module_file in module_files:
            module_name = os.path.splitext(os.path.basename(module_file))[0]
            if module_name != "__init__":
                try:
                    module = importlib.import_module(module_name)
                    modules.append(module)
                except ImportError as e:
                    logger.warning(f"Failed to import module {module_name}: {e}")
        return modules






# # flexiai/assistant/function_mapping.py
# import logging

# logger = logging.getLogger(__name__)


# def get_function_mappings():
#     """
#     Get the function mappings for personal and assistant functions, including both internal and user-defined functions.

#     Returns:
#         tuple: A tuple containing the personal function mappings and assistant function mappings.
#     """
#     # Internal function mappings
#     personal_function_mapping = {}
#     assistant_function_mapping = {}

#     return personal_function_mapping, assistant_function_mapping


# def register_user_functions(personal_function_mapping, assistant_function_mapping):
#     """
#     Register user-defined functions by merging them with existing function mappings.

#     Args:
#         personal_function_mapping (dict): The personal function mappings to be updated.
#         assistant_function_mapping (dict): The assistant function mappings to be updated.

#     Returns:
#         tuple: A tuple containing the updated personal function mappings and assistant function mappings.
#     """
#     try:
#         from user_flexiai_rag.user_function_mapping import register_user_tasks

#         user_personal_functions, user_assistant_functions = register_user_tasks()
#         personal_function_mapping.update(user_personal_functions)
#         assistant_function_mapping.update(user_assistant_functions)
#         logger.info("Successfully registered user functions from user_flexiai_rag/user_function_mapping.py")

#     except ModuleNotFoundError:
#         logger.warning("The module user_flexiai_rag.user_function_mapping does not exist.")
#     except AttributeError:
#         logger.error("The module user_flexiai_rag.user_function_mapping does not have a 'register_user_tasks' function.")
#     except Exception as e:
#         logger.error(f"Failed to register user functions: {e}", exc_info=True)
#         raise

#     return personal_function_mapping, assistant_function_mapping
