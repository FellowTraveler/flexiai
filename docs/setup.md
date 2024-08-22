# Setup Guide

This guide will help you set up FlexiAI in your project, including installation steps, environment setup, and post-installation setup.

### Table of Contents

- [Installation](#installation)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install FlexiAI with pip](#install-flexiai-with-pip)
  - [Install Pandoc](#install-pandoc-on-different-platforms)
- [Environment Setup](#environment-setup)
  - [Create and Configure .env File](#create-and-configure-env-file)
  - [Example .env File](#example-env-file)
- [Post-Installation Setup](#post-installation-setup)
  - [Enable Retrieval-Augmented Generation (RAG)](#enable-retrieval-augmented-generation-rag)
  - [FlexiAI Basic Flask Chat Application](#flexiai-basic-flask-chat-application)
  - [Install Requirements](#install-requirements)

---

## Installation

### Create a Virtual Environment

Creating a virtual environment helps manage dependencies and avoid conflicts. Choose either PowerShell or Conda to create your virtual environment.

#### Using PowerShell

```powershell
python -m venv .flexi_env
source .flexi_env/bin/activate
```

#### Using Conda

```powershell
conda create --name flexi_env
conda activate flexi_env
```

### Install FlexiAI with pip

To install the FlexiAI framework using pip, run:

```powershell
pip install flexiai
```

### Install Pandoc on Different Platforms

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt-get install pandoc
```

#### **macOS (using Homebrew):**
```bash
brew install pandoc
```

#### **Windows (using PowerShell with Chocolatey):**
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')); choco install pandoc
```

---

## Environment Setup

Before proceeding with post-installation steps, you need to create and configure a `.env` file in your project. This file will store your API keys and configuration settings.

### Create and Configure .env File

1. Create a `.env` file in the root of your project directory.
2. Add the following content to the `.env` file, replacing placeholder values with your actual API keys and settings.

### Example .env File

```bash
# ============================================================================================ #
#                                      OpenAI Configuration                                    #
# ============================================================================================ #
# Replace 'your_openai_api_key_here' with your actual OpenAI API key. 
# This key allows FlexiAI to authenticate and communicate with the OpenAI API.
OPENAI_API_KEY=your_openai_api_key_here

# Replace 'your_openai_api_version_here' with the version of the OpenAI API you're using. 
# Example for OpenAI: 2020-11-07. Ensure that it corresponds to the API features you want to use.
OPENAI_API_VERSION=your_openai_api_version_here

# Replace 'your_openai_organization_id_here' with your OpenAI Organization ID.
# This is required if your OpenAI account belongs to an organization. Otherwise, leave it blank.
OPENAI_ORGANIZATION_ID=your_openai_organization_id_here

# Replace 'your_openai_project_id_here' with your OpenAI Project ID.
# This helps FlexiAI link its API requests to the correct project under your OpenAI account.
OPENAI_PROJECT_ID=your_openai_project_id_here

# Replace 'your_openai_assistant_version_here' with the version of the OpenAI Assistant you are using.
# Example: v1 or v2. Make sure this matches the version you are working with for proper functionality.
OPENAI_ASSISTANT_VERSION=your_openai_assistant_version_here


# ============================================================================================ #
#                                      Azure OpenAI Configuration                              #
# ============================================================================================ #
# Replace 'your_azure_openai_api_key_here' with your actual Azure OpenAI API key.
# This key is necessary to authenticate FlexiAI with Azure's OpenAI services.
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here

# Replace 'your_azure_openai_endpoint_here' with your Azure OpenAI endpoint URL.
# This URL typically looks like 'https://<your-endpoint>.openai.azure.com/' and is used to make requests to the Azure OpenAI service.
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here

# Replace 'your_azure_openai_api_version_here' with the version of the Azure OpenAI API you're using.
# Example: 2024-05-01-preview. Ensure this matches the API version that corresponds with the Azure services you're utilizing.
AZURE_OPENAI_API_VERSION=your_azure_openai_api_version_here


# ============================================================================================ #
#                                      General Configuration                                   #
# ============================================================================================ #
# Set this to 'openai' if you are using OpenAI's services, or 'azure' if you are using Azure OpenAI.
# This helps FlexiAI determine which platform to interact with.
CREDENTIAL_TYPE=openai


# ============================================================================================ #
#                                      User Project Configuration                              #
# ============================================================================================ #
# Define the root directory of your project where custom functions and scripts for FlexiAI will reside.
# This path should point to the main folder where FlexiAI will look for user-defined content.
USER_PROJECT_ROOT_DIR=/your/path/to_your/project_root_directory
```

---

## Post-Installation Setup

After the environment has been set up and the `.env` file has been configured, follow the steps below for post-installation:

### 1. Enable Retrieval-Augmented Generation (RAG)

To set up the RAG module, run the following command in your terminal or command prompt:

```bash
setup-flexiai-rag
```

This command generates the necessary folder structure and starter files for integrating Retrieval-Augmented Generation (RAG) capabilities into your project. Below is the folder structure that is created by this command:

```plaintext
📦your_project
 ┣ 📂logs                            # Directory to store application logs.
 ┣ 📂user_flexiai_rag
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📂audio                       # Directory to store audio files related to RAG.
 ┃ ┃ ┣ 📂csv                         # Directory to store CSV files used in RAG.
 ┃ ┃ ┣ 📂images                      # Directory to store image files for RAG.
 ┃ ┃ ┗ 📂vectors_store               # Directory to store vector files for RAG.
 ┃ ┣ 📜__init__.py                   # Initialization file for the RAG module.
 ┃ ┣ 📜user_functions_mapping.py     # File to map user-defined functions to FlexiAI.
 ┃ ┣ 📜user_functions_manager.py     # Manager for user-defined functions, handling RAG tasks.
 ┣ 📜.env                            # Environment variables configuration file.
 ┣ 📜requirements.txt                # File listing all necessary dependencies for the project.
```

#### Key Files

- **`user_flexiai_rag/__init__.py`**: Initialization file for the `user_flexiai_rag` module.
- **`user_flexiai_rag/user_functions_mapping.py`**: This file contains the logic to map user-defined functions to FlexiAI, allowing for customization of assistant capabilities.
- **`user_flexiai_rag/user_functions_manager.py`**: This file defines the `FunctionsManager` class, which handles user-defined tasks such as interacting with external services (e.g., searching YouTube).

### 2. FlexiAI Basic Flask Chat Application

To set up the basic Flask chat application, run the following command:

```bash
setup-flexiai-flask-app
```

This command generates a basic Flask application structure for FlexiAI, including folders and starter files for routes, templates, and static assets. Below is the folder structure that is created by this command:

```plaintext
📦your_project
 ┣ 📂logs
 ┣ 📂routes
 ┃ ┗ 📜api.py                 # API routes for handling chat messages, including session and thread management.
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜styles.css           # Base styles for the chat application.
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📜assistant.png        # Assistant avatar
 ┃ ┃ ┗ 📜user.png             # User avatar
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js           # JavaScript to handle chat interactions and message input.
 ┃ ┗ 📜favicon.ico            # Website icon
 ┣ 📂templates
 ┃ ┗ 📜index.html             # HTML template for the chat application UI.
 ┣ 📂utils
 ┃ ┗ 📜markdown_converter.py  # Utility to convert markdown to HTML, used for rendering chat messages.
 ┣ 📜app.py                   # Main Flask application that configures routing, session management, and logging.
```

#### Key Files

- **`routes/api.py`**: Handles API routes for processing user messages and interacting with the FlexiAI assistant.
- **`static/css/styles.css`**: Contains the styles for the chat application's UI, including message bubbles and layout.
- **`static/js/scripts.js`**: Handles the front-end logic for sending messages, receiving responses, and updating the UI dynamically.
- **`templates/index.html`**: The HTML structure for the chat interface

, including the input box and message display area.
- **`utils/markdown_converter.py`**: Converts markdown content to HTML using Pandoc, ensuring messages are displayed correctly with markdown formatting.

### 3. Install Requirements

After running the previous commands, install the required dependencies using the `requirements.txt` file that was created.

```powershell
pip install -r requirements.txt
```

### **Update the Assistant ID**

  Open the `routes/api.py` file and replace the Assistant ID with your main assistant ID.
  > Should look like this: assistant_id = 'asst_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Update with your Assistant ID

  ```python
  assistant_id = 'your_main_assistant_id'
  ```

###  **Add Images**

  In the `static` folder:
  - Add an `favicon.ico` image.
  - In the `static/images` folder, add `assistant.png` and `user.png` for the chat avatars.

  This ensures that your chat application has the necessary visual elements.

This will install all the necessary packages required for FlexiAI to function properly.
