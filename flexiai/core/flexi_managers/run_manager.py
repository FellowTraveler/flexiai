# flexiai/core/run_manager.py
import time
import json
from openai import OpenAIError

class RunManager:
    """
    RunManager handles the creation, monitoring, and management of runs in threads
    using specified assistants. It supports creating runs, advanced runs with user
    messages, and handling required actions.

    Attributes:
        client (OpenAI or AzureOpenAI): The client for interacting with OpenAI or Azure OpenAI services.
        logger (logging.Logger): The logger for logging information and errors.
        personal_function_mapping (dict): Mapping of function names to their personal function implementations.
        assistant_function_mapping (dict): Mapping of function names to their assistant function implementations.
        message_manager (MessageManager): Manages message operations within threads.
    """

    def __init__(self, client, logger, personal_function_mapping, assistant_function_mapping, message_manager):
        """
        Initializes the RunManager instance with the specified client, logger,
        function mappings, and message manager.

        Args:
            client (OpenAI or AzureOpenAI): The client for interacting with OpenAI or Azure OpenAI services.
            logger (logging.Logger): The logger for logging information and errors.
            personal_function_mapping (dict): Mapping of function names to their personal function implementations.
            assistant_function_mapping (dict): Mapping of function names to their assistant function implementations.
            message_manager (MessageManager): Manages message operations within threads.
        """
        self.client = client
        self.logger = logger
        self.personal_function_mapping = personal_function_mapping
        self.assistant_function_mapping = assistant_function_mapping
        self.message_manager = message_manager

    def create_run(self, assistant_id, thread_id):
        """
        Creates and runs a thread with the specified assistant, monitoring its status
        until completion or failure.

        Args:
            assistant_id (str): The ID of the assistant.
            thread_id (str): The ID of the thread.

        Returns:
            object: The run object if successful, None otherwise.

        Raises:
            OpenAIError: If any API call within this function fails.
            Exception: If an unexpected error occurs.
        """
        try:
            self.logger.info(f"Starting a new run for thread {thread_id} with assistant {assistant_id}")
            
            # Wait for any active run to complete
            self.wait_for_run_completion(thread_id)
            
            run = self.client.beta.threads.runs.create(
                thread_id=thread_id, assistant_id=assistant_id
            )

            # Monitor the status of the run
            while run.status in ['queued', 'in_progress', 'cancelling', 'requires_action']:
                self.logger.info(f"Run status: {run.status}")
                if run.status == 'requires_action':
                    self.handle_requires_action(run, assistant_id, thread_id)
                time.sleep(0.5)  # Wait for 0.5 second before checking again
                run = self.client.beta.threads.runs.retrieve(
                    thread_id=thread_id, run_id=run.id
                )

            # Check the final status of the run
            if run.status == 'completed':
                self.logger.info(f"Run {run.id} completed successfully for thread {thread_id}")
                return run
            else:
                self.logger.error(f"Run {run.id} failed with status: {run.status}")
                return None
        except OpenAIError as e:
            self.logger.error(f"An error occurred during thread run for thread {thread_id} with assistant {assistant_id}: {str(e)}", exc_info=True)
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during thread run for thread {thread_id} with assistant {assistant_id}: {str(e)}", exc_info=True)
            raise

    def create_advanced_run(self, assistant_id, thread_id, user_message):
        """
        Creates and runs a thread with the specified assistant and user message, 
        monitoring its status until completion or failure.

        Args:
            assistant_id (str): The ID of the assistant.
            thread_id (str): The ID of the thread.
            user_message (str): The user's message content.

        Returns:
            object: The run object if successful, None otherwise.

        Raises:
            OpenAIError: If any API call within this function fails.
            Exception: If an unexpected error occurs.
        """
        try:
            self.logger.info(f"Starting a new run for thread {thread_id} with assistant {assistant_id}")
            
            # Wait for any active run to complete
            self.wait_for_run_completion(thread_id)
            
            # Add the user's message to the thread
            self.message_manager.add_user_message(thread_id, user_message)
            
            run = self.client.beta.threads.runs.create(
                thread_id=thread_id, assistant_id=assistant_id
            )

            # Monitor the status of the run
            while run.status in ['queued', 'in_progress', 'cancelling', 'requires_action']:
                self.logger.info(f"Run status: {run.status}")
                if run.status == 'requires_action':
                    self.handle_requires_action(run, assistant_id, thread_id)
                time.sleep(1)  # Wait for 1 second before checking again
                run = self.client.beta.threads.runs.retrieve(
                    thread_id=thread_id, run_id=run.id
                )

            # Check the final status of the run
            if run.status == 'completed':
                self.logger.info(f"Run {run.id} completed successfully for thread {thread_id}")
            else:
                self.logger.error(f"Run {run.id} failed with status: {run.status}")

            return run
        except OpenAIError as e:
            self.logger.error(f"An error occurred during thread run for thread {thread_id} with assistant {assistant_id}: {str(e)}", exc_info=True)
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during thread run for thread {thread_id} with assistant {assistant_id}: {str(e)}", exc_info=True)
            raise

    def wait_for_run_completion(self, thread_id):
        """
        Waits for any active run in the thread to complete by continuously checking the
        run status until no active runs remain.

        Args:
            thread_id (str): The ID of the thread.

        Raises:
            OpenAIError: If the API call to retrieve thread runs fails.
            Exception: If an unexpected error occurs.
        """
        try:
            while True:
                self.logger.info(f"Checking for active runs in thread {thread_id}")
                runs = self.client.beta.threads.runs.list(thread_id=thread_id)
                active_runs = [run for run in runs if run.status in ["queued", "in_progress", "cancelling"]]
                if active_runs:
                    self.logger.info(f"Run {active_runs[0].id} is currently {active_runs[0].status}. Waiting for completion...")
                    time.sleep(1)
                else:
                    self.logger.info(f"No active run in thread {thread_id}. Proceeding...")
                    break
        except OpenAIError as e:
            self.logger.error(f"Failed to retrieve thread runs for thread {thread_id}: {str(e)}", exc_info=True)
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred while waiting for run completion in thread {thread_id}: {str(e)}", exc_info=True)
            raise

    def handle_requires_action(self, run, assistant_id, thread_id):
        """
        Handles required actions from a run, executing necessary functions and 
        submitting the outputs back to the API.

        Args:
            run (object): The run object requiring actions.
            assistant_id (str): The ID of the assistant.
            thread_id (str): The ID of the thread.

        Raises:
            OpenAIError: If an error occurs when interacting with the OpenAI API.
            Exception: If an unexpected error occurs during the process.
        """
        self.logger.info(f"Handling required action for run ID: {run.id} with assistant ID: {assistant_id}.")

        if run.status == "requires_action":
            tool_outputs = []

            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                self.logger.info(f"Function Name: {function_name}")
                self.logger.info(f"Arguments: {arguments}")

                action_type = self.determine_action_type(function_name)

                if action_type == "call_assistant":
                    self.logger.info(f"Calling another assistant with arguments: {arguments}")
                    status, message, result = self.call_assistant_with_arguments(function_name, **arguments)
                else:
                    self.logger.info(f"Executing personal function with arguments: {arguments}")
                    status, message, result = self.execute_personal_function_with_arguments(function_name, **arguments)

                tool_output = {
                    "tool_call_id": tool_call.id,
                    "output": json.dumps({"status": status, "message": message, "result": result})
                }
                self.logger.info(f"Tool output to be submitted: {tool_output}")
                tool_outputs.append(tool_output)

            try:
                self.client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
                self.logger.info(f"Successfully submitted tool outputs for run ID: {run.id}")
            except OpenAIError as e:
                self.logger.error(f"OpenAI API error when submitting tool outputs for run ID {run.id} in thread {thread_id} with assistant {assistant_id}: {str(e)}", exc_info=True)
                raise
            except Exception as e:
                self.logger.error(f"General error when submitting tool outputs for run ID {run.id} in thread {thread_id} with assistant {assistant_id}: {str(e)}", exc_info=True)
                raise
        else:
            self.logger.info(f"No required action for this run ID: {run.id}")

    def determine_action_type(self, function_name):
        """
        Determines the type of action required based on the function's name.

        Args:
            function_name (str): The name of the function.

        Returns:
            str: The type of action, either 'call_assistant' or 'personal_function'.
        """
        self.logger.info(f"Determining action type for function: {function_name}")
        if function_name.endswith("_assistant"):
            action_type = "call_assistant"
        else:
            action_type = "personal_function"
        self.logger.info(f"Action type for function {function_name}: {action_type}")
        return action_type

    def execute_personal_function_with_arguments(self, function_name, **arguments):
        """
        Executes a personal function based on the provided function name and arguments.

        Args:
            function_name (str): The name of the function to execute.
            **arguments: The arguments to pass to the function.

        Returns:
            tuple: A tuple containing the status (bool), message (str), and result (any).

        Raises:
            Exception: If the function execution fails.
        """
        self.logger.info(f"Attempting to execute function: {function_name} with arguments: {arguments}")
        func = self.personal_function_mapping.get(function_name, None)
        if callable(func):
            try:
                result = func(**arguments)
                self.logger.info(f"Personal Function {function_name} executed.")
                return True, "Action - Personal Function.", result
            except Exception as e:
                self.logger.error(f"Error executing {function_name}: {str(e)}", exc_info=True)
                return False, f"Error executing {function_name}: {str(e)}", None
        else:
            self.logger.warning(f"Function {function_name} not found in mapping.")
            return False, f"Function not found: {function_name}", None

    def call_assistant_with_arguments(self, function_name, **arguments):
        """
        Calls another assistant or internal function based on the provided function name and arguments.

        Args:
            function_name (str): The name of the function to call.
            **arguments: The arguments to pass to the function.

        Returns:
            tuple: A tuple containing the status (bool), message (str), and result (any).

        Raises:
            ValueError: If the function is not found.
            Exception: If the function execution fails.
        """
        self.logger.info(f"Attempting to dispatch an assistant using the function: {function_name} with arguments: {arguments}")
        func = self.assistant_function_mapping.get(function_name, None)
        if callable(func):
            try:
                result = func(**arguments)
                self.logger.info(f"Call Assistant Function {function_name} executed.")
                return True, "Action - Call Assistant.", result
            except Exception as e:
                self.logger.error(f"Error executing {function_name}: {str(e)}", exc_info=True)
                return False, f"Error executing {function_name}: {str(e)}", None
        else:
            error_message = f"Function {function_name} is not defined."
            self.logger.error(error_message)
            raise ValueError(error_message)
