# FlexiAI Usage Guide

Welcome to the FlexiAI usage guide! This document will help you understand how to set up, use, and contribute to the FlexiAI framework.

## Table of Contents

1. [Introduction](#introduction)
2. [Key Features](#key-features)
3. [Framework Structure](#framework-structure)
4. [Installation](#installation)
5. [Getting Started](#getting-started)
6. [Retrieval-Augmented Generation (RAG)](#retrieval-augmented-generation-rag)
    1. [Implementing RAG in FlexiAI](#implementing-rag-in-flexiai)
    2. [Example Workflow](#example-workflow)
    3. [Project Structure for RAG](#project-structure-for-rag)

We hope you find this documentation helpful!

### Introduction

FlexiAI is a flexible AI framework designed to integrate with various AI services like OpenAI and Azure OpenAI. It allows you to create and manage AI assistants, handle user interactions, and leverage tools and resources seamlessly.

### Key Features

**Multi-Platform Support**  
FlexiAI seamlessly integrates with both OpenAI and Azure OpenAI services, ensuring flexibility and broad compatibility for various use cases and deployment scenarios.

**Configurable and Extensible**  
FlexiAI offers an easily configurable and highly extensible framework, allowing developers to customize and scale the solution to meet specific project needs and organizational requirements.

**Robust Logging**  
The framework incorporates comprehensive logging capabilities, facilitating effective debugging and monitoring. This ensures a smooth development and operational experience, allowing for quick issue resolution and performance tracking.

**Task Management**  
FlexiAI efficiently manages and executes a wide range of tasks, ensuring streamlined operations and enhanced productivity. This feature helps in organizing and automating workflows, reducing manual intervention.

**Retrieval-Augmented Generation (RAG)**  
The framework empowers AI assistants to dynamically call external functions or services, enabling real-time retrieval of information. This capability allows the assistant to handle complex operations efficiently, making the solution more versatile and powerful.

**Examples and Tests**  
FlexiAI provides a rich set of example scripts and comprehensive tests, enabling quick onboarding and ensuring reliable performance from the outset. This helps developers understand the framework better and deploy it with confidence.

**Secure and Scalable**  
Designed with security and scalability in mind, FlexiAI is suitable for both small projects and large enterprise applications. It ensures that the framework can grow with your needs while maintaining high security standards.

**Community-Driven**  
FlexiAI is actively maintained and supported by a community of developers. This ensures continuous improvement, up-to-date features, and a reliable support system, making it a robust and evolving solution.

### Framework Structure

Here's an overview of the FlexiAI framework structure:

```python
📦flexiai
 ┣ 📂.github
 ┃ ┗ 📂workflows
 ┃   ┗ 📜workflow.yml
 ┣ 📂flexiai
 ┃ ┣ 📂assistant
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜function_mapping.py
 ┃ ┃ ┗ 📜task_manager.py
 ┃ ┣ 📂config
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜config.py
 ┃ ┃ ┗ 📜logging_config.py
 ┃ ┣ 📂core
 ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┗ 📜helpers.py
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜credentials.py
 ┃ ┃ ┣ 📜flexiai_client.py
 ┃ ┃ ┗ 📜threads_manager.py
 ┃ ┣ 📂docs
 ┃ ┃ ┣ 📜api_reference.md
 ┃ ┃ ┣ 📜contributing.md
 ┃ ┃ ┣ 📜example_assistant.md
 ┃ ┃ ┣ 📜index.md
 ┃ ┃ ┣ 📜setup.md
 ┃ ┃ ┗ 📜usage.md
 ┃ ┣ 📂examples
 ┃ ┃ ┣ 📜handle_requires_action.ipynb
 ┃ ┃ ┣ 📜usage_helpers.ipynb
 ┃ ┃ ┣ 📜with_azure_credentials.py
 ┃ ┃ ┗ 📜with_openai_credentials.py
 ┃ ┣ 📂logs
 ┃ ┃ ┗ 📜app.log
 ┃ ┣ 📂tests
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜test_assistant_search_product.py
 ┃ ┃ ┗ 📜test_assistant_youtube_search.py
 ┃ ┣ 📂user_flexiai_rag
 ┃ ┃ ┣ 📂data
 ┃ ┃ ┃ ┗ 📜products.csv
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜user_function_mapping.py
 ┃ ┃ ┣ 📜user_helpers.py
 ┃ ┃ ┗ 📜user_task_manager.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜.env.template
 ┣ 📜.gitignore
 ┣ 📜CODE_OF_CONDUCT.md
 ┣ 📜LICENSE.txt
 ┣ 📜MANIFEST.in
 ┣ 📜README.md
 ┣ 📜post_install.py
 ┣ 📜pyproject.toml
 ┣ 📜requirements.txt
 ┗ 📜setup.py
```

Each folder and file in the framework serves a specific purpose:

- **assistant/**: Contains modules for managing AI assistants, including function mappings and task management.
- **config/**: Contains configuration files, including environment variable settings and logging configuration.
- **core/**: Core functionalities of the framework, including client initialization and credential management.
- **docs/**: Documentation files for the framework.
- **examples/**: Example scripts demonstrating how to use the framework with different credentials and configurations.
- **logs/**: Log files generated by the framework.
- **tests/**: Unit and integration tests for the framework.
- **user_flexiai_rag/**: Contains user-defined task management and function mapping files to extend the functionality of FlexiAI.

### Installation

To install the FlexiAI framework using `pip`, simply run:

```bash
pip install flexiai
```

After installing, create a `.env` file in your project root directory with the following template:

```bash
# Your OpenAI API key
OPENAI_API_KEY='your_openai_api_key_here'
# Your Azure OpenAI API key
AZURE_OPENAI_API_KEY='your_azure_openai_api_key_here'
# Your Azure OpenAI endpoint
AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint_here'
# Azure OpenAI API version
AZURE_OPENAI_API_VERSION='2024-05-01-preview'
# Credential type (either 'openai' or 'azure')
CREDENTIAL_TYPE='openai'
```

### Getting Started

To get started with FlexiAI, follow the [Setup Guide](setup.md) to install and configure the framework. Then, refer to the [Usage Guide](usage.md) for examples of how to use FlexiAI in your projects.

For detailed information on the API methods and classes, see the [API Reference](api_reference.md).

### Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is a powerful feature of FlexiAI that allows the assistant to dynamically call external functions or services to retrieve information that is not readily available in its static data. This is particularly useful for tasks that require up-to-date information or complex operations.

#### Implementing RAG in FlexiAI

1. **TaskManager (`assistant/task_manager.py`)**:
    - Manages tasks related to searching YouTube and products.
    - Provides methods like `search_youtube` and `search_products`, which can be mapped to functions in `function_mapping.py`.

    Users should add their custom functions in the `TaskManager` class that mirror the JSON functions defined in the Assistant on OpenAI or Azure AI Studio. These functions handle the business logic required to perform specific tasks.

2. **Function Mapping (`assistant/function_mapping.py`)**:
    - Maps function names to the actual functions in the `TaskManager`.
    - Distinguishes between personal functions and assistant functions.

    The `get_function_mappings` function in `function_mapping.py` is responsible for mapping the function names used by the assistant to the actual Python functions defined in the `TaskManager`. This mapping allows the assistant to call the appropriate function and perform the required action.

3. **Using `handle_requires_action`**:
    - Ensures that when a run requires action, it uses the function mappings to execute the appropriate task.
    - Submits the results of these tasks back to the OpenAI API to continue the run.

    The `handle_requires_action` method leverages the function mappings to dynamically call the required functions. It uses the function name provided by the assistant, looks it up in the mapping, and then calls the corresponding function in the `TaskManager` with the provided arguments. The results are then formatted and submitted back to the OpenAI API.

#### Example Workflow

1. **Define User-Defined Functions in `UserTaskManager`**:
    Define the user-defined functions in the `UserTaskManager` class for the tasks you want to perform.

    ```python
    # user_flexiai_rag/user_task_manager.py

    class UserTaskManager:
        def search_youtube(self, query):
            # Implementation of search_youtube method
            pass

        def search_products(self, **kwargs):
            # Implementation of search_products method
            pass
    ```

2. **Map Functions in `user_function_mapping.py`**:
    Map the function names to the functions defined in `UserTaskManager`.

    ```python
    # user_flexiai_rag/user_function_mapping.py
    from flexiai.user_flexiai_rag.user_task_manager import UserTaskManager

    def register_user_tasks():
        """
        Register user-defined tasks/functions with the FlexiAI framework.

        Returns:
            tuple: A tuple containing the personal function mappings and assistant function mappings.
        """
        task_manager = UserTaskManager()

        personal_function_mapping = {
            'search_youtube': task_manager.search_youtube,
            'search_products': task_manager.search_products,
            # Add other personal functions here
        }

        assistant_function_mapping = {
            # Add other functions that call assistants here
            # 'call_example_assistant': task_manager.call_example_assistant,
        }

        return personal_function_mapping, assistant_function_mapping
    ```

3. **Map Functions in `function_mapping.py`**:
    Integrate user-defined functions into the main function mapping.

    ```python
    # assistant/function_mapping.py
    from flexiai.user_flexiai_rag.user_function_mapping import register_user_tasks

    def get_function_mappings(task_manager):
        """
        Get the function mappings for personal and assistant functions, including both internal and user-defined functions.

        Args:
            task_manager (TaskManager): The task manager instance containing internal tasks.

        Returns:
            tuple: A tuple containing the personal function mappings and assistant function mappings.
        """
        # FlexiAI's internal function mappings

        personal_function_mapping = {
            # Internal personal assistant functions here
        }

        assistant_function_mapping = {
            # Internal calling assistants here
        }

        # Register user-defined tasks
        user_personal_functions, user_assistant_functions = register_user_tasks()
        
        # Merge the user-defined functions with the internal ones
        personal_function_mapping.update(user_personal_functions)
        assistant_function_mapping.update(user_assistant_functions)

        return personal_function_mapping, assistant_function_mapping
    ```

4. **Handle Required Actions**:
    Use `handle_requires_action` to process the required actions by calling the mapped functions and submitting the results.

    ```python
    # assistant/task_manager.py

    def handle_requires_action(self, run, assistant_id, thread_id):
        """
        Handle required actions from a run.

        This method processes the required actions for a given run. It executes the necessary functions
        and submits the outputs back to the OpenAI API or Azure OpenAI.

        Args:
            run (object): The run object requiring actions.
            assistant_id (str): The ID of the assistant.
            thread_id (str): The ID of the thread.

        Raises:
            OpenAIError: If an error occurs when interacting with the OpenAI API.
            Exception: If an unexpected error occurs during the process.
        """
        self.logger.info(f"Handling required action for run ID: {run.id} with assistant ID: {assistant_id}.")
        
        # Check if the run status indicates that actions are required
        if run.status == "requires_action":
            tool_outputs = []
            
            # Iterate over each tool call that requires an output submission
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                
                self.logger.debug(f"Function Name: {function_name}")
                self.logger.debug(f"Arguments: {arguments}")
                
                # Determine the type of action to perform
                action_type = self.determine_action_type(function_name)
                
                # Execute the appropriate function based on the action type
                if action_type == "call_assistant":
                    self.logger.debug(f"Calling another assistant with arguments: {arguments}")
                    status, message, result = self.call_assistant_with_arguments(function_name, **arguments)
                else:
                    self.logger.debug(f"Executing personal function with arguments: {arguments}")
                    status, message, result = self.execute_personal_function_with_arguments(function_name, **arguments)
                
                # Prepare the tool output for submission
                tool_output = {
                    "tool_call_id": tool_call.id,
                    "output": json.dumps({"status": status, "message": message, "result": result})
                }
                self.logger.debug(f"Tool output to be submitted: {tool_output}")
                tool_outputs.append(tool_output)
            
            # Submit the tool outputs to the OpenAI API
            try:
                self.client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
                self.logger.info(f"Successfully submitted tool outputs for run ID: {run.id}")
            except OpenAIError as e:
                self.logger.error(f"OpenAI API error when submitting tool outputs: {e}")
                raise
            except Exception as e:
                self.logger.error(f"General error when submitting tool outputs: {e}")
                raise
        else:
            self.logger.info(f"No required action for this run ID: {run.id}")
    ```

5. **Example Script for Testing OpenAI Credentials**:
    FlexiAI can integrate with the OpenAI Assistants API to enhance its capabilities. Here is an example script for testing the integration with OpenAI credentials.

    ```python
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
        setup_logging(root_level=logging.INFO, file_level=logging.DEBUG, console_level=logging.ERROR)

        # Initialize FlexiAI
        flexiai = FlexiAI()

        # Use the given assistant ID
        assistant_id = 'asst_XXXXXXXXXXXXXXXXXXXXXXXXX' # Replace with the actual assistant ID
        
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
                # Using the new retrieve_messages function
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
    ```

### Project Structure for RAG

To enable RAG (Retrieval-Augmented Generation) in your project, you need to create a specific folder structure and the necessary files. Below is the structure and the details of each file:

```js
📦your_project
 ┣ 📂user_flexiai_rag
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📜products.csv
 ┃ ┃ ┗ 📜other files or folders.(e.g., more data files, configurations, etc.)
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜user_function_mapping.py
 ┃ ┣ 📜user_helpers.py
 ┃ ┗ 📜user_task_manager.py
 ┣ 📂logs
 ┣ 📜requirements.txt
 ┗ 📜.env
```

#### `user_function_mapping.py`

```python
from flexiai.user_flexiai_rag.user_task_manager import UserTaskManager

def register_user_tasks():
    """
    Register user-defined tasks with the FlexiAI framework.

    Returns:
        tuple: A tuple containing the personal function mappings and assistant function mappings.
    """
    # Initialize UserTaskManager to access user-defined tasks
    task_manager = UserTaskManager()

    personal_function_mapping = {
        'search_youtube': task_manager.search_youtube,
        'search_products': task_manager.search_products,
        # Add other personal functions here
        # 'my_custom_task': task_manager.my_custom_task
    }

    assistant_function_mapping = {
        # Add other functions that call assistants here -> the functions must end with "_assistant"
        # 'call_example_assistant': task_manager.call_example_assistant,
    }

    return personal_function_mapping, assistant_function_mapping
```

#### `user_helpers.py`

```python
import subprocess
import logging

def wsl_to_windows_path(wsl_path):
    """
    Converts a WSL path to a Windows path.

    Args:
        wsl_path (str): The WSL path to convert.

    Returns:
        str: The converted Windows path, or None if an error occurs.
    """
    try:
        windows_path = subprocess.check_output(['wslpath', '-w', wsl_path]).strip().decode('utf-8')
        return windows_path
    except subprocess.CalledProcessError as e:
        logging.error(f"Error converting WSL path to Windows path: {e}")
        return None

def format_product(product):
    """
    Formats product details into a readable string.

    Args:
        product (dict): A dictionary containing product details. Expected keys are 'product_id',

 
                        'product_name', 'brand', 'price', 'stock', 'rating', 'warranty_years', 
                        'category', 'release_date', and 'customer_reviews'.

    Returns:
        str: A formatted string containing the product details.
    """
    return (
        f"Product ID: {product['product_id']}\n"
        f"Product Name: {product['product_name']}\n"
        f"Brand: {product['brand']}\n"
        f"Price: ${product['price']}\n"
        f"Stock: {product['stock']}\n"
        f"Rating: {product['rating']}\n"
        f"Warranty Years: {product['warranty_years']}\n"
        f"Category: {product['category']}\n"
        f"Release Date: {product['release_date']}\n"
        f"Customer Reviews: {product['customer_reviews']}\n\n"
    )
```

#### `user_task_manager.py`

```python
import logging
import subprocess
import urllib.parse
import pandas as pd
from flexiai.config.logging_config import setup_logging
from flexiai.user_flexiai_rag.user_helpers import format_product

# Set up logging using your custom configuration
# Adjust the logging levels as per your requirements
setup_logging(root_level=logging.INFO, file_level=logging.DEBUG, console_level=logging.ERROR)

class UserTaskManager:
    """
    UserTaskManager class handles user-defined tasks.
    """

    def __init__(self):
        """
        Initializes the UserTaskManager instance, setting up the logger.
        """
        self.logger = logging.getLogger(__name__)

    def search_youtube(self, query):
        """
        Searches YouTube for the given query and opens the search results page
        in the default web browser.

        Args:
            query (str): The search query string.

        Returns:
            dict: A dictionary containing the status, message, and result (URL)
        """
        if not query:
            return {
                "status": False,
                "message": "Query cannot be empty.",
                "result": None
            }

        try:
            # Normalize spaces to ensure consistent encoding
            query_normalized = query.replace(" ", "+")
            query_encoded = urllib.parse.quote(query_normalized)
            youtube_search_url = (
                f"https://www.youtube.com/results?search_query={query_encoded}"
            )
            self.logger.info(f"Opening YouTube search for query: {query}")

            # subprocess.run(['cmd.exe', '/c', 'start', '', youtube_search_url], check=True)

            # Use PowerShell to open the URL
            subprocess.run(
                ['powershell.exe', '-Command', 'Start-Process', youtube_search_url],
                check=True
            )

            self.logger.info("YouTube search page opened successfully.")
            return {
                "status": True,
                "message": "YouTube search page opened successfully.",
                "result": youtube_search_url
            }
        except subprocess.CalledProcessError as e:
            error_message = f"Subprocess error: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }
        except Exception as e:
            error_message = f"Failed to open YouTube search for query: {query}. Error: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }

    def search_products(self, product_id=None, product_name=None, brand=None, price_range=None, stock=None, rating_range=None, 
                        warranty_years=None, category=None, release_date=None, customer_reviews=None):
        """
        Searches for products in the products CSV file based on the given criteria.

        Args:
            product_id (int, optional): The ID of the product.
            product_name (str, optional): The name of the product.
            brand (str or list, optional): The brand of the product or a list of brands.
            price_range (tuple, optional): The price range as a tuple (min_price, max_price).
            stock (int, optional): The stock quantity.
            rating_range (tuple, optional): The rating range as a tuple (min_rating, max_rating).
            warranty_years (int, optional): The number of warranty years.
            category (str, optional): The category of the product.
            release_date (str, optional): The release date of the product.
            customer_reviews (str, optional): A substring to search for in customer reviews.

        Returns:
            dict: A dictionary containing the status, message, and result (formatted product list or None).
        """
        try:
            # Load the CSV file
            df = pd.read_csv('user_flexiai_rag/data/products.csv')

            # Apply filters based on the provided arguments
            if product_id is not None:
                df = df[df['product_id'] == product_id]
            if product_name is not None:
                df = df[df['product_name'].str.contains(product_name, case=False, na=False)]
            if brand is not None:
                if isinstance(brand, list):
                    df = df[df['brand'].isin(brand)]
                else:
                    df = df[df['brand'].str.contains(brand, case=False, na=False)]
            if price_range is not None:
                if isinstance(price_range, tuple) and len(price_range) == 2:
                    df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]
                else:
                    error_message = "Invalid price range. Provide a tuple with (min_price, max_price)."
                    self.logger.error(error_message)
                    return {
                        "status": False,
                        "message": error_message,
                        "result": None
                    }
            if stock is not None:
                df = df[df['stock'] == stock]
            if rating_range is not None:
                if isinstance(rating_range, tuple) and len(rating_range) == 2:
                    df = df[(df['rating'] >= rating_range[0]) & (df['rating'] <= rating_range[1])]
                else:
                    error_message = "Invalid rating range. Provide a tuple with (min_rating, max_rating)."
                    self.logger.error(error_message)
                    return {
                        "status": False,
                        "message": error_message,
                        "result": None
                    }
            if warranty_years is not None:
                df = df[df['warranty_years'] == warranty_years]
            if category is not None:
                df = df[df['category'].str.contains(category, case=False, na=False)]
            if release_date is not None:
                df = df[df['release_date'] == release_date]
            if customer_reviews is not None:
                df = df[df['customer_reviews'].str.contains(customer_reviews, case=False, na=False)]

            # Check if any results are found
            if df.empty:
                return {
                    "status": False,
                    "message": "No products found matching the criteria.",
                    "result": None
                }

            # Convert the filtered DataFrame to a list of dictionaries
            results = df.to_dict(orient='records')
            # Format each product using the format_product function
            formatted_results = [format_product(product) for product in results]
            return {
                "status": True,
                "message": f"Found {len(formatted_results)} product(s) matching the criteria.",
                "result": formatted_results
            }
        except FileNotFoundError:
            error_message = "The products.csv file was not found."
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }
        except pd.errors.EmptyDataError:
            error_message = "The products.csv file is empty."
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }
        except Exception as e:
            error_message = f"An error occurred while searching for products: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }

    # User can add more custom tasks (assistant personal functions or functions to call other assistants)
```

### `.env` file template

```bash
# ========================== #
# Example .env file template #
# ========================== #

# Your OpenAI API key
OPENAI_API_KEY='your_openai_api_key_here'
# Your Azure OpenAI API key
AZURE_OPENAI_API_KEY='your_azure_openai_api_key_here'
# Your Azure OpenAI endpoint
AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint_here'
# Azure OpenAI API version
AZURE_OPENAI_API_VERSION='2024-05-01-preview'
# Credential type (either 'openai' or 'azure')
CREDENTIAL_TYPE='openai'
```

### `requirements.txt` content:

```js
annotated-types==0.7.0
anyio==4.4.0
asttokens==2.1.0
azure-common==1.1.28
azure-core==1.30.2
azure-identity==1.17.1
azure-mgmt-core==1.4.0
azure-mgmt-resource==23.1.1
backports.tarfile==1.2.0
blinker==1.8.2
certifi==2024.6.2
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
comm==0.1.3
cryptography==42.0.8
debugpy==1.6.5
decorator==5.1.1
distro==1.9.0
docutils==0.21.2
exceptiongroup==1.1.0
executing==1.2.0
Flask==3.0.3
h11==0.14.0
httpcore==1.0.5
httpx==0.27.0
idna==3.7
importlib_metadata==6.8.0
iniconfig==2.0.0
ipykernel==6.24.0
ipython==8.14.0
ipywidgets==8.1.3
isodate==0.6.1
itsdangerous==2.2.0
jaraco.classes==3.4.0
jaraco.context==5.3.0
jaraco.functools==4.0.1
jedi==0.19.0
jeepney==0.8.0
Jinja2==3.1.4
jupyter_client==8.3.0
jupyter_core==5.2.0
jupyterlab_widgets==3.0.11
keyring==25.2.1
markdown-it-py==3.0.0
MarkupSafe==2.1.5
matplotlib-inline==0.1.6
mdurl==0.1.2
more-itertools==10.3.0
msal==1.29.0
msal-extensions==1.2.0
nest_asyncio==1.5.7
nh3==0.2.17
numpy==2.0.0
openai==1.35.0
packaging==23.1
pandas==2.2.2
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
pkginfo==1.10.0
platformdirs==3.7.0
pluggy==1.5.0
portalocker==2.10.0
prompt_toolkit==3.0.39
psutil==5.9.5
ptyprocess==0.7.0
pure-eval==0.2.2
pycparser==2.22
pydantic==2.7.4
pydantic-settings==2.3.3
pydantic_core==2.18.4
Pygments==2.15.1
PyJWT==2.8.0
pytest==8.2.2
pytest-mock==3.14.0
python-dateutil==2.8.2
python-dotenv==1.0.1
pytz==2024.1
pyzmq==25.1.0
readme_renderer==43.0
requests==2.32.3
requests-toolbelt==1.0.0
rfc3986==2.0.0
rich==13.7.1
SecretStorage==3.3.3
six==1.16.0
sniffio==1.3.1
stack-data==0.6.3
tomli==2.0.1
tornado==6.3.2
tqdm==4.66.4
traitlets==5.10.1
twine==5.1.1
typing_extensions==4.7.1
tzdata==2024.1
urllib3==2.2.2
wcwidth==0.2.6
Werkzeug==3.0.3
widgetsnbextension==4.0.11
zipp==3.17.0
setuptools==70.2.0
```


1. **Install `pip-audit`**:
   ```bash
   pip install pip-audit
   ```

2. **Run `pip-audit` to check if there are vulnerabilities**:
   ```bash
   pip-audit
   ```

By following these instructions and creating the necessary files and folders, you can enable RAG in your project and use FlexiAI to its full potential.
