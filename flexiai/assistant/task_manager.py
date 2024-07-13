# flexiai/assistant/task_manager.py
import logging
from concurrent.futures import ThreadPoolExecutor
import asyncio
from flexiai.assistant.function_mapping import FunctionMapper

class TaskManager:
    """
    TaskManager class handles tasks related to searching YouTube, searching products,
    and integrates user-defined tasks.
    """

    def __init__(self, max_workers=10):
        """
        Initializes the TaskManager instance, setting up the logger and user-defined tasks.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing TaskManager")
        self.function_mapper = FunctionMapper()
        self.load_user_tasks()
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    async def run_task_async(self, func, *args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self.executor, func, *args, **kwargs)

    def run_task(self, func, *args, **kwargs):
        future = self.executor.submit(func, *args, **kwargs)
        return future.result()

    def load_user_tasks(self):
        self.logger.info("Loading user-defined tasks")
        try:
            self.personal_function_mapping, self.assistant_function_mapping = self.function_mapper.get_function_mappings()
            self.personal_function_mapping, self.assistant_function_mapping = self.function_mapper.register_user_functions(
                self.personal_function_mapping, self.assistant_function_mapping
            )
            self.logger.info("User-defined tasks loaded successfully")
        except Exception as e:
            self.logger.error(f"Failed to load user-defined tasks: {str(e)}", exc_info=True)






# # flexiai/assistant/task_manager.py
# import logging
# from flexiai.config.logging_config import setup_logging

# # Set up logging using your custom configuration
# setup_logging(root_level=logging.INFO, file_level=logging.INFO, console_level=logging.ERROR)


# class TaskManager:
#     """
#     TaskManager class handles tasks related to searching YouTube, searching products,
#     and integrates user-defined tasks.
#     """

#     def __init__(self):
#         """
#         Initializes the TaskManager instance, setting up the logger and user-defined tasks.
#         """
#         self.logger = logging.getLogger(__name__)
#         self.logger.info("Initializing TaskManager")
#         self.load_user_tasks()

#     def load_user_tasks(self):
#         self.logger.info("Loading user-defined tasks")
#         try:
#             from flexiai.assistant.function_mapping import register_user_functions, get_function_mappings
#             self.personal_function_mapping, self.assistant_function_mapping = get_function_mappings()
#             self.personal_function_mapping, self.assistant_function_mapping = register_user_functions(
#                 self.personal_function_mapping, self.assistant_function_mapping
#             )
#             self.logger.info("User-defined tasks loaded successfully")
#         except Exception as e:
#             self.logger.error(f"Failed to load user-defined tasks: {str(e)}", exc_info=True)
