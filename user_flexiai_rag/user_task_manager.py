# user_flexiai_rag/user_task_manager.py
import csv
import os
import logging
import subprocess
import urllib.parse


class UserTaskManager:
    """
    UserTaskManager class handles user-defined tasks.
    """

    def __init__(self):
        """
        Initializes the UserTaskManager instance, setting up the logger.
        """
        self.logger = logging.getLogger(__name__)

    def log_function_call(self, func_name):
        """
        Logs the function call.
        
        Args:
            func_name (str): The name of the function being called.
        """
        self.logger.info(f"Function called: {func_name}")

    def search_youtube(self, query):
        """
        Searches YouTube for the given query and opens the search results page
        in the default web browser.

        Args:
            query (str): The search query string.

        Returns:
            dict: A dictionary containing the status, message, and result (URL)
        """
        self.log_function_call(__name__)

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

    def identify_person(self, name=None, phone_number=None, address=None, birth_date=None, email_address=None, client_code=None):
        """
        Identifies a person in the system by matching provided details against records in a CSV file.
        At least three details must match to successfully identify a person.

        Parameters:
        - name (str, optional): The name of the person.
        - phone_number (str, optional): The person's phone number.
        - address (str, optional): The person's address.
        - birth_date (str, optional): The person's date of birth in 'yyyy-mm-dd' format.
        - email_address (str, optional): The person's email address.
        - client_code (str, optional): The unique client code of the person.

        Returns:
        - dict: A dictionary containing the status, message, and result.
            - status (bool): True if the identification was successful, False otherwise.
            - message (str): A message detailing the result of the identification process.
            - result (dict or None): The identified person's details if successful, None otherwise.
        """
        self.log_function_call(__name__)

        file_path = os.path.join(os.path.dirname(__file__), 'data', 'csv', 'identify_person.csv')
        
        if not os.path.exists(file_path):
            return {
                "status": False,
                "message": f"File not found: {file_path}",
                "result": None
            }
        
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                if not reader.fieldnames:
                    return {
                        "status": False,
                        "message": "CSV file has no header or is empty.",
                        "result": None
                    }
                
                rows = list(reader)
                if not rows:
                    return {
                        "status": False,
                        "message": "CSV file has no header or is empty.",
                        "result": None
                    }

                for row in rows:
                    matched_details = sum(1 for detail, value in [
                        ('name', name),
                        ('phone_number', phone_number),
                        ('address', address),
                        ('birth_date', birth_date),
                        ('email_address', email_address),
                        ('client_code', client_code)
                    ] if value is not None and row.get(detail) == value)
                    
                    if matched_details >= 3:
                        return {
                            "status": True,
                            "message": f"Person {row['name']} has been successfully identified in the system.",
                            "result": row
                        }
            
            return {
                "status": False,
                "message": "No person matched the provided details.",
                "result": None
            }
        except FileNotFoundError:
            return {
                "status": False,
                "message": f"CSV file not found at path: {file_path}",
                "result": None
            }
        except csv.Error as e:
            return {
                "status": False,
                "message": f"Error reading CSV file: {str(e)}",
                "result": None
            }
        except Exception as e:
            return {
                "status": False,
                "message": f"An unexpected error occurred: {str(e)}",
                "result": None
            }

    def manage_product(self, action, search_params=None, update_params=None, product_id=None, product_name=None, 
                       description=None, price=None, quantity=None):
        """
        Manages product details in the CSV file based on the provided action.

        Parameters:
        - action: The action to perform, either 'search' to find products or 'update' to modify product details.
        - search_params: List of parameters to use for searching. Can include 'product_id', 'product_name', 'description', 'price', and 'quantity'.
        - update_params: List of dictionaries specifying the identifier and values to update. Each dictionary should include:
            - 'identifier': The parameter to identify the product, either 'product_id' or 'product_name'.
            - 'values': Dictionary of parameters to update with their new values.
            Example format: [{'identifier': 'product_id', 'values': {'quantity': 30}}]
        - product_id: The ID of the product to search or update.
        - product_name: The name of the product to search or update.
        - description: The description of the product to search or update.
        - price: The price of the product to search or update.
        - quantity: The quantity of the product to search or update.

        Returns:
        - dict: A dictionary containing the status, message, and result.
            - status (bool): True if the operation was successful, False otherwise.
            - message (str): A message detailing the result of the operation.
            - result (dict or list or None): The product details if found or updated, None otherwise.
        """
        self.log_function_call(__name__)

        file_path = os.path.join(os.path.dirname(__file__), 'data', 'csv', 'products.csv')
        
        self.logger.info(f"CSV file path: {file_path}")

        if not os.path.exists(file_path):
            self.logger.error(f"File not found: {file_path}")
            return {
                "status": False,
                "message": f"File not found: {file_path}",
                "result": None
            }

        try:
            products = []
            matched_products = []
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                if not reader.fieldnames:
                    self.logger.error("CSV file has no header or is empty.")
                    return {
                        "status": False,
                        "message": "CSV file has no header or is empty.",
                        "result": None
                    }

                for row in reader:
                    self.logger.debug(f"Processing row: {row}")
                    match = True
                    if search_params:
                        for param in search_params:
                            if param == 'product_id' and product_id and row['product_id'].strip() != product_id.strip():
                                match = False
                            if param == 'product_name' and product_name and row['product_name'].strip().lower() != product_name.strip().lower():
                                match = False
                            if param == 'description' and description and row['description'].strip() != description.strip():
                                match = False
                            if param == 'price' and price is not None and float(row['price']) != float(price):
                                match = False
                            if param == 'quantity' and quantity is not None and int(row['quantity']) != int(quantity):
                                match = False
                    
                    if match:
                        self.logger.info(f"Match found: {row}")
                        matched_products.append(row)
                        if action == 'update' and update_params:
                            for update in update_params:
                                identifier = update['identifier']
                                if identifier == 'product_id' and product_id and row['product_id'].strip() == product_id.strip():
                                    self.logger.debug(f"Updating product by ID: {row['product_id']}")
                                    for key, value in update['values'].items():
                                        if key in row:
                                            row[key] = str(value)
                                    self.logger.info(f"Product {row['product_id']} has been successfully updated.")
                                    break
                                elif identifier == 'product_name' and product_name and row['product_name'].strip().lower() == product_name.strip().lower():
                                    self.logger.debug(f"Updating product by name: {row['product_name']}")
                                    for key, value in update['values'].items():
                                        if key in row:
                                            row[key] = str(value)
                                    self.logger.info(f"Product {row['product_id']} has been successfully updated.")
                                    break
                    
                    products.append(row)
                
                if action == 'search':
                    if not matched_products:
                        self.logger.warning("No products matched the provided details.")
                        return {
                            "status": False,
                            "message": "No products matched the provided details.",
                            "result": None
                        }
                    self.logger.info(f"Products matching criteria: {matched_products}")
                    return {
                        "status": True,
                        "message": "Products matching criteria found.",
                        "result": matched_products
                    }
                
                if action == 'update':
                    with open(file_path, mode='w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                        writer.writeheader()
                        writer.writerows(products)
                    if matched_products:
                        self.logger.info("CSV file updated successfully.")
                        return {
                            "status": True,
                            "message": "Product has been successfully updated.",
                            "result": matched_products[0]
                        }
                    else:
                        self.logger.warning(f"No product found with the provided details.")
                        return {
                            "status": False,
                            "message": f"No product found with the provided details.",
                            "result": None
                        }
                
            return {
                "status": False,
                "message": f"Invalid action: {action}",
                "result": None
            }
            
        except FileNotFoundError:
            self.logger.error(f"CSV file not found at path: {file_path}")
            return {
                "status": False,
                "message": f"CSV file not found at path: {file_path}",
                "result": None
            }
        except csv.Error as e:
            self.logger.error(f"Error reading or writing CSV file: {str(e)}")
            return {
                "status": False,
                "message": f"Error reading or writing CSV file: {str(e)}",
                "result": None
            }
        except ValueError as e:
            self.logger.error(f"Value error occurred: {str(e)}")
            return {
                "status": False,
                "message": f"Value error occurred: {str(e)}",
                "result": None
            }
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {str(e)}")
            return {
                "status": False,
                "message": f"An unexpected error occurred: {str(e)}",
                "result": None
            }
