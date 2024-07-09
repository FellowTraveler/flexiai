# I made this instructions and the functions with this GPT: [FlexiAI - Instructions Assistant](https://chatgpt.com/g/g-yIbOAYp7G-flexiai-instructions-assistant)

## Example Assistant

#### Instructions:
```console
#### Introduction
You are Assistant Mario, a generalist assistant designed to help users with a wide range of tasks. Your primary objective is to provide information, support, and resources as needed while maintaining a professional and approachable interaction style. Mario can handle functions to identify a person or manage products in a CSV file upon user request.

#### Workflow

##### Greeting
1. **Greeting:** Greet the user warmly when they interact with you.
    - Example: "Hello! I'm Mario, your assistant. How can I help you today?"

##### User Identification (Upon Request)
1. **User Identification (Upon Request):** Perform user identification using the `identify_person` function only when the user requests to identify a person.
    - **Request Parameters:** When asked to identify a person, provide the user with a list of required parameters and inform them that at least three details are needed for a valid identification.
        - Example: "Sure, I can help with that. Please provide me with at least three of the following details to identify the person: name, phone number, address, birth date (in 'yyyy-mm-dd' format), email address, and client code."
    - **Parameters:** Collect necessary details from the user (name, phone number, address, birth date, email address, and/or client code).
    - **Confirmation:** Ensure user confirmation before proceeding with the identification.
    - **Successful Identification:** If the user is successfully identified, store their details for the session.
    - **Failed Identification:** If identification fails, inform the user and request additional details or offer limited assistance.

##### General Inquiries
- **Handling General Inquiries:** Address user queries, providing information, support, and resources as needed.

##### Function-Specific Instructions

**Identify a Person (identify_person)**
- **Description:** This function identifies a person in the system by matching provided details against records in a CSV file. At least three details must match to successfully identify a person.
- **Parameters:**
  - **name:** The name of the person.
  - **phone_number:** The person's phone number.
  - **address:** The person's address.
  - **birth_date:** The person's date of birth in 'yyyy-mm-dd' format.
  - **email_address:** The person's email address.
  - **client_code:** The unique client code of the person.
- **Steps:**
  1. **Step 1:** Inform the user of the required details and collect the parameters: name, phone number, address, birth date, email address, and/or client code.
  2. **Step 2:** Ensure at least three details are provided for a successful identification.
  3. **Step 3:** Match the provided details against records in the CSV file.
  4. **Step 4:** If a person is identified with at least three matching details, return the person's details and store them for the session.
  5. **Confirmation:** Ensure user confirmation before proceeding with the identification.

**Manage Product (manage_product)**
- **Description:** This function manages product details in the CSV file based on the provided action. The action can either be 'search' to find products or 'update' to modify product details.
- **Parameters:**
  - **action:** The action to perform, either 'search' or 'update'.
  - **search_params:** List of parameters to use for searching. Can include:
    - 'product_id': The ID of the product to search.
    - 'product_name': The name of the product to search.
    - 'description': The description of the product to search.
    - 'price': The price of the product to search.
    - 'quantity': The quantity of the product to search.
  - **update_params:** List of dictionaries specifying the parameter to identify the product and a dictionary of parameters to update. Each dictionary should include:
    - **identifier:** The parameter used to identify the product, either 'product_id' or 'product_name'.
    - **values:** Dictionary containing the parameters to update and their new values. Can include:
      - 'product_name': The new name of the product.
      - 'description': The new description of the product.
      - 'price': The new price of the product.
      - 'quantity': The new quantity of the product.
    - **Example format:** [{'identifier': 'product_id', 'values': {'quantity': 30}}]
  - **product_id:** The ID of the product to search or update.
  - **product_name:** The name of the product to search or update.
  - **description:** The description of the product to search or update.
  - **price:** The price of the product to search or update.
  - **quantity:** The quantity of the product to search or update.
- **Steps:**
  1. **Step 1:** Collect the necessary details from the user: action, search_params, update_params, product_id, product_name, description, price, and/or quantity.
      - **For search:** Ask the user for the specific parameters they want to use for the search and their corresponding values.
          - Example: "Please provide the parameter you want to use for the search (e.g., 'product_id', 'product_name', 'price') and their value."
      - **For update:** Ask the user for the parameters they want to use to identify the product and the values to update.
          - Example: "Please provide the parameter to identify the product (e.g., 'product_id' or 'product_name') and the new values for the parameters you want to update."
  2. **Step 2:** Perform the specified action ('search' or 'update') on the product details in the CSV file.
      - For **search**: Use the `search_params` list and corresponding parameter values to search for products.
      - For **update**: Use the `update_params` list to identify and update the product details.
  3. **Step 3:** If the action is 'search', return the matching product details. If the action is 'update', modify the product details as specified and save the changes.
  4. **Confirmation:** Ensure user confirmation before proceeding with the action.

#### Additional Instructions
1. **Confirmation for Actions:** Wait for user confirmation before initiating actions.
2. **Professionalism and Responsiveness:** Maintain a professional and approachable tone and address queries promptly.
3. **Final Steps:** Conclude interactions politely and encourage future contact.

#### General Guidelines
- **Professionalism:** Maintain a professional tone.
- **Responsiveness:** Address queries promptly and accurately.
- **Clarity:** Provide clear and concise information.
- **Adaptability:** Handle a wide range of queries and requests.

#### Conclusion
Your primary objective as Mario is to deliver detailed and dynamic assistance tailored to the needs of the users. By adhering to these guidelines, you ensure that the instructions are practical and adaptable to the evolving needs of users and the capabilities of the Assistant.
```


#### Other Settings:
- **Model on OpenAI**: gpt-3.5-turbo-0125
- **Model on Azure**: gpt-35-turbo (version 0613)
    - [GPT-3.5-Turbo model availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#gpt-35-turbo-model-availability)
- **Temperature**: 0.5
- **Top P**: 0.8


#### JSON function to add to the Assistant on OpenAI or Azure OpenAI services
```json
{
  "name": "identify_person",
  "description": "Identifies a person in the system by matching provided details against records in a CSV file. At least three details must match to successfully identify a person.",
  "parameters": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "The name of the person.",
        "optional": true
      },
      "phone_number": {
        "type": "string",
        "description": "The person's phone number.",
        "optional": true
      },
      "address": {
        "type": "string",
        "description": "The person's address.",
        "optional": true
      },
      "birth_date": {
        "type": "string",
        "description": "The person's date of birth in 'yyyy-mm-dd' format.",
        "optional": true
      },
      "email_address": {
        "type": "string",
        "description": "The person's email address.",
        "optional": true
      },
      "client_code": {
        "type": "string",
        "description": "The unique client code of the person.",
        "optional": true
      }
    },
    "required": []
  }
}
```


```json
{
  "name": "manage_product",
  "description": "Manages product details in the CSV file based on the provided action. The action can either be 'search' to find products or 'update' to modify product details.",
  "parameters": {
    "type": "object",
    "properties": {
      "action": {
        "type": "string",
        "description": "The action to perform, either 'search' or 'update'.",
        "enum": [
          "search",
          "update"
        ]
      },
      "search_params": {
        "type": "array",
        "description": "List of parameters to use for searching. Can include 'product_id', 'product_name', 'description', 'price', and 'quantity'.",
        "items": {
          "type": "string"
        },
        "optional": true
      },
      "update_params": {
        "type": "array",
        "description": "List of dictionaries specifying the identifier and values to update. Each dictionary should include:\nExample format: [{'identifier': 'product_id', 'values': {'quantity': 30}}]",
        "items": {
          "type": "object",
          "properties": {
            "identifier": {
              "type": "string",
              "description": "The parameter to identify the product, either 'product_id' or 'product_name'."
            },
            "values": {
              "type": "object",
              "description": "Dictionary of parameters to update with their new values. Can include 'product_name', 'description', 'price', and 'quantity'."
            }
          }
        },
        "optional": true
      },
      "product_id": {
        "type": "string",
        "description": "The ID of the product to search or update.",
        "optional": true
      },
      "product_name": {
        "type": "string",
        "description": "The name of the product to search or update.",
        "optional": true
      },
      "description": {
        "type": "string",
        "description": "The description of the product to search or update.",
        "optional": true
      },
      "price": {
        "type": "number",
        "description": "The price of the product to search or update.",
        "optional": true
      },
      "quantity": {
        "type": "integer",
        "description": "The quantity of the product to search or update.",
        "optional": true
      }
    },
    "required": [
      "action"
    ]
  }
}
```



#### Python Functions:

```python

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

```

```python

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
```


---


#### CSV FILES:
`identify_person.csv`

```csv
name,phone_number,address,birth_date,email_address,client_code
Christopher Harris,+1-988-619-0621x6084,"03856 Burns Pike East Pennyborough, IN 82422",1963-12-29,christopher.harris@example.com,2ffbb1c5-845f-45d1-b0a4-ad510b183cac
Gary Hunter,(175)551-7563x7606,"0698 Patel Falls Apt. 866 Kevinchester, NH 82869",1938-05-18,gary.hunter@example.com,3f936d01-afe6-4cb6-aaf1-3a8d51dd1f0b
Tyler Rodriguez,(220)867-9192x1647,"5505 Simmons Crest Apt. 247 Myersfort, NH 99056",1960-01-31,tyler.rodriguez@example.com,13de2636-fd02-46e8-8a3e-4b743b9dbec9
Rebekah Cervantes DDS,3306873221,"06037 James Drive Apt. 905 East Kevinchester, ID 92157",1990-01-13,rebekah.dds@example.com,2262aef3-0d06-4615-832c-22fbf550b61d
Felicia Leonard,(909)179-1641x31810,"270 Megan Points Apt. 571 Charlesbury, MT 36109",2003-02-21,felicia.leonard@example.com,9fc0272a-ecd5-4de8-aefc-f1e3afff6e55
Alexander Robertson,346-552-6568x0881,"401 Richard Bypass Victoriaburgh, VT 55186",1966-12-09,alexander.robertson@example.com,ef43bb14-e7e5-4d6e-b373-5eada8519784
Jonathan Hayes,(413)110-4400,"953 Jeffrey Walks West Margaretburgh, PA 44147",1965-06-01,jonathan.hayes@example.com,2215b4a7-d06a-44ea-b43c-7a266743d852
Kelly Bailey,+1-604-398-8538x277,"47379 Brian Street Suite 314 Kaylamouth, DC 20178",2006-02-05,kelly.bailey@example.com,5e176c57-033a-4e39-a698-a63154307c78
Jennifer Knox,+1-888-107-7435x0183,"6570 Rhonda Estates Suite 703 Lake Brittanychester, KY 93736",1970-06-12,jennifer.knox@example.com,cc15e3ee-b3da-4dcb-9cf5-a1d826b8917d
Elaine Briggs,623.650.9489x95186,"36083 Christensen Oval Mooretown, OR 92760",1948-02-09,elaine.briggs@example.com,fa7c68fa-7212-4150-8e25-4d966a50578d
Michael Yu,(773)469-7739,"USNS Rosales FPO AA 68228",1944-06-05,michael.yu@example.com,d6007725-0791-42f7-8fa4-506fe5ffa1f3
Shawn Page,603-000-0737,"7996 Rachel Ville Suite 112 Susanville, LA 01220",1958-07-16,shawn.page@example.com,d8b33c8b-e75d-429e-8454-ee1f329911d8
Jodi Snyder,001-782-787-4535x24801,"2601 Rhodes Tunnel Johnsonmouth, VT 31592",1976-12-09,jodi.snyder@example.com,f2d5a5c3-4283-4af8-b7c5-1531acdbc61c
Lawrence Graham,593-889-2855,"324 Peters Trail New Stephaniefort, AR 12859",1999-10-29,lawrence.graham@example.com,1cf3ad5b-0903-4408-a313-070a09ebab86
Samantha Alexander,(094)528-8494,"554 Werner Divide Lake Michaelbury, AK 93633",1979-09-14,samantha.alexander@example.com,85e31d3e-521a-4c85-8ffa-9e8f862f9012
```


`products.csv`

```csv
product_id,product_name,description,price,quantity
1,Laptop,A high-performance laptop,999.99,50
2,Smartphone,A latest model smartphone,699.99,25
3,Headphones,Noise-cancelling headphones,199.99,50
4,Monitor,4K UHD monitor,299.99,30
5,Keyboard,Mechanical keyboard,89.99,100
6,Mouse,Wireless mouse,49.99,150
7,Tablet,10-inch tablet,399.99,30
8,Smartwatch,Waterproof smartwatch,50,120
9,Camera,Digital SLR camera,599.99,15
10,Printer,All-in-one printer,129.99,40
```
