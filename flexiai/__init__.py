# flexiai/__init__.py
from flexiai.assistant.task_manager import TaskManager
from flexiai.assistant.function_mapping import get_function_mappings, register_user_functions

# Importing the configuration class
from flexiai.config.config import Config

# Importing the main FlexiAI client class
from flexiai.core.flexiai_client import FlexiAI

# Exporting these imports so they are available when the flexiai package is imported
__all__ = [
    'TaskManager',
    'get_function_mappings',
    'register_user_functions',
    'Config',
    'FlexiAI'
]
