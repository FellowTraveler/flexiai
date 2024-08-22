# Setup Guide

This guide will help you set up FlexiAI in your project, including installation steps, virtual environment creation, and post-installation setup.

### Table of Contents

- [Installation](#installation)
  - [Create a Virtual Environment](#create-a-virtual-environment)
    - [Using PowerShell](#using-powershell)
    - [Using Conda](#using-conda)
  - [Install FlexiAI with pip](#install-flexiai-with-pip)
  - [Install Pandoc](#install-pandoc-on-different-platforms)
  - [Post-Installation Setup](#post-installation-setup)
    - [Enable Retrieval-Augmented Generation (RAG)](#enable-retrieval-augmented-generation-rag)
    - [FlexiAI Basic Flask Chat Application](#flexiai-basic-flask-chat-application)
- [Environment Setup](#environment-setup)
  - [Example .env File](#example-env-file)

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

#### **macOS (using PowerShell with Homebrew):**
```powershell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install pandoc
```

#### **Windows (using Command Prompt with Chocolatey):**
```cmd
choco install pandoc
```

#### **Windows (using PowerShell with Chocolatey):**
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')); choco install pandoc
``` 

### Post-Installation Setup

After installing FlexiAI, there are two post-installation setup commands you can run to enable key functionality.

#### Enable Retrieval-Augmented Generation (RAG)

To set up the RAG module, run the following command in your terminal or command prompt:

```bash
setup-flexiai-rag
```

This will automatically create the necessary folder structure and files for RAG in your project, including data storage and utility scripts for user-defined functions.

#### FlexiAI Basic Flask Chat Application

To set up the basic Flask chat application, run the following command in your terminal or command prompt:

```bash
setup-flexiai-flask-app
```

This will automatically create the necessary folder structure and files for a basic Flask chat application, including static files (CSS, JS, images), routes, and templates.


### Enable Retrieval-Augmented Generation (RAG)

Here's an overview of the created structure for the RAG extension (some files are as examples, will receive empty folders to set your files):

```plaintext
📦your_project
 ┃ 
 ┣ 📂user_flexiai_rag
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📂audio
 ┃ ┃ ┃ ┣ 📜Travelers_of_the_Cosmos.mp3
 ┃ ┃ ┃ ┣ 📜output.mp3
 ┃ ┃ ┃ ┣ 📜output_hd.mp3
 ┃ ┃ ┃ ┗ 📜test_output.wav
 ┃ ┃ ┣ 📂corpus
 ┃ ┃ ┃ ┣ 📂another_folder
 ┃ ┃ ┃ ┃ ┣ 📜probability.txt
 ┃ ┃ ┃ ┃ ┗ 📜python.txt
 ┃ ┃ ┃ ┣ 📜artificial_intelligence.txt
 ┃ ┃ ┃ ┣ 📜machine_learning.txt
 ┃ ┃ ┃ ┣ 📜natural_language_processing.txt
 ┃ ┃ ┃ ┗ 📜neural_network.txt
 ┃ ┃ ┣ 📂csv
 ┃ ┃ ┃ ┣ 📜identify_person.csv
 ┃ ┃ ┃ ┗ 📜products.csv
 ┃ ┃ ┣ 📂images
 ┃ ┃ ┃ ┣ 📜generated_image_1aec1dd8-b386-43d1-9a6c-ae6a7d5aeb21.png
 ┃ ┃ ┃ ┗ 📜generated_image_1bc706cc-85e5-4b53-b6f7-af3810d79177.png
 ┃ ┃ ┗ 📂vectors_store
 ┃ ┃ ┃ ┣ 📜updated_vector_store_after_replacement.index
 ┃ ┃ ┃ ┣ 📜updated_vector_store_after_replacement.index.meta
 ┃ ┃ ┃ ┣ 📜vector_store.index
 ┃ ┃ ┃ ┗ 📜vector_store.index.meta
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜user_function_mapping.py                  
 ┃ ┣ 📜user_helpers.py
 ┃ ┗ 📜user_task_manager.py
 ┣ 📂logs
 ┣ 📜requirements.txt
 ┣ 📜.env
 ┃
 ┗ ...
```

### FlexiAI Basic Flask Chat Application

Here's an overview of the created structure for the Flask app:

```plaintext
📦your_project
 ┃
 ┣ 📂logs
 ┃ ┗ 📜app.log
 ┣ 📂routes
 ┃ ┗ 📜api.py
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📂other_images
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 161351.png
 ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 161358.png
 ┃ ┃ ┃ ┣ 📜...
 ┃ ┃ ┃ ┗ 📜Screenshot 2024-07-12 165558.png
 ┃ ┃ ┣ 📜assistant.png
 ┃ ┃ ┗ 📜user.png
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js
 ┃ ┗ 📜favicon.ico
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📂utils
 ┃ ┗ 📜markdown_converter.py
 ┣ 📜app.py
 ┃
 ┗ ...
```

2. **Install Requirements**

    Install the required dependencies using `pip`.

    ```powershell
    pip install -r requirements.txt
    ```

3. **Update the Assistant ID**

    Open the `routes/api.py` file and replace the placeholder assistant ID with your main assistant ID.

    ```python
    assistant_id = 'your_main_assistant_id'
    ```

4. **Add Images**

    In the `static` folder:
    - Add an `favicon.ico` image.
    - In the `static/images` folder, add `assistant.png` and `user.png` for the chat avatars.

    This ensures that your chat application has the necessary visual elements.

---

## Environment Setup

Before using FlexiAI, set up your environment variables. The `setup-flexiai-rag` command will create a `.env` file in your project root directory with the following template:

### Example .env File

```bash
# ============================================================================================ #
#                                      OpenAI Configuration                                    #
# ============================================================================================ #
# Replace 'your_openai_api_key_here' with your actual OpenAI API key.
OPENAI_API_KEY=your_openai_api_key_here

# Replace 'your_openai_api_version_here' with your actual OpenAI API version.
# Example for OpenAI: 2020-11-07
OPENAI_API_VERSION=your_openai_api_version_here

# Replace 'your_openai_organization_id_here' with your actual OpenAI Organization ID.
OPENAI_ORGANIZATION_ID=your_openai_organization_id_here

# Replace 'your_openai_project_id_here' with your actual OpenAI Project ID.
OPENAI_PROJECT_ID=your_openai_project_id_here

# Replace 'your_openai_assistant_version_here' with your actual OpenAI Assistant version.
# Example for Assistant: v1 or v2
OPENAI_ASSISTANT_VERSION=your_openai_assistant_version_here


# ============================================================================================ #
#                                      Azure OpenAI Configuration                              #
# ============================================================================================ #
# Replace 'your_azure_openai_api_key_here' with your actual Azure OpenAI API key.
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here

# Replace 'your_azure_openai_endpoint_here' with your actual Azure OpenAI endpoint.
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here

# Replace 'your_azure_openai_api_version_here' with your actual Azure OpenAI API version.
# Example for Azure: 2024-05-01-preview
AZURE_OPENAI_API_VERSION=your_azure_openai_api_version_here


# ============================================================================================ #
#                                      General Configuration                                   #
# ============================================================================================ #
# Set this to 'openai' if you are using OpenAI, or 'azure' if you are using Azure OpenAI.
CREDENTIAL_TYPE=openai


# ============================================================================================ #
#                                      User Project Configuration                              #
# ============================================================================================ #
# Define the root directory of the user's project to integrate custom functions into FlexiAI.
USER_PROJECT_ROOT_DIR=/your/path/to_your/project_root_directory

```
