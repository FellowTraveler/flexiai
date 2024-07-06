# Setup Guide

Follow these steps to set up the FlexiAI framework.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
   - [Option 1: Using Virtual Environment (Recommended)](#option-1-using-virtual-environment-recommended)
   - [Option 2: Using Conda Environment](#option-2-using-conda-environment)
   - [Option 3: Install with pip](#option-3-install-with-pip)
3. [Setting Up on Ubuntu in WSL on Windows 11](#setting-up-on-ubuntu-in-wsl-on-windows-11)
4. [Troubleshooting](#troubleshooting)
5. [Additional Configuration](#additional-configuration)

## Prerequisites

- Python 3.10.14
- Pip package manager
- Git

## Installation

### Option 1: Using Virtual Environment (Recommended)

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SavinRazvan/flexiai.git
    cd flexiai
    ```

2. **Create and activate a virtual environment:**

    **Linux/WSL:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    **Option A: Using a `.env` file**

    Create a `.env` file in the root directory with the following content:

    ```bash
    # Your OpenAI API key
    OPENAI_API_KEY='your_openai_api_key'
    # Your Azure OpenAI API key
    AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    # Your Azure OpenAI endpoint
    AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    # Azure OpenAI API version
    AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    # Credential type (either 'openai' or 'azure')
    CREDENTIAL_TYPE='openai'
    ```

    **Option B: Setting environment variables manually**

    **Linux/WSL:**

    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    export AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    export AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    export AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    export CREDENTIAL_TYPE='openai'  # or 'azure'
    ```

    **Windows:**

    ```bash
    set OPENAI_API_KEY='your_openai_api_key'
    set AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    set AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    set AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    set CREDENTIAL_TYPE='openai'  # or 'azure'
    ```

5. **Run the example script to ensure everything is set up correctly:**

    ```bash
    python examples/with_openai_credentials.py
    ```

You are now ready to use FlexiAI!

### Option 2: Using Conda Environment

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SavinRazvan/flexiai.git
    cd flexiai
    ```

2. **Create and activate a conda environment:**

    ```bash
    conda create --name flexiai_env python=3.10.14
    conda activate flexiai_env
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    **Option A: Using a `.env` file**

    Create a `.env` file in the root directory with the following content:

    ```bash
    # Your OpenAI API key
    OPENAI_API_KEY='your_openai_api_key'
    # Your Azure OpenAI API key
    AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    # Your Azure OpenAI endpoint
    AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    # Azure OpenAI API version
    AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    # Credential type (either 'openai' or 'azure')
    CREDENTIAL_TYPE='openai'
    ```

    **Option B: Setting environment variables manually**

    **Linux/WSL:**

    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    export AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    export AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    export AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    export CREDENTIAL_TYPE='openai'  # or 'azure'
    ```

    **Windows:**

    ```bash
    set OPENAI_API_KEY='your_openai_api_key'
    set AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    set AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    set AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    set CREDENTIAL_TYPE='openai'  # or 'azure'
    ```

5. **Run the example script to ensure everything is set up correctly:**

    ```bash
    python examples/with_openai_credentials.py
    ```

You are now ready to use FlexiAI!

### Option 3: Install with pip

1. **Install FlexiAI with pip:**

    ```bash
    pip install flexiai
    ```

2. **Set up environment variables:**

    **Option A: Using a `.env` file**

    Create a `.env` file in the root directory with the following content:

    ```bash
    # Your OpenAI API key
    OPENAI_API_KEY='your_openai_api_key'
    # Your Azure OpenAI API key
    AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    # Your Azure OpenAI endpoint
    AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    # Azure OpenAI API version
    AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    # Credential type (either 'openai' or 'azure')
    CREDENTIAL_TYPE='openai'
    ```

    **Option B: Setting environment variables manually**

    **Linux/WSL:**

    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    export AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    export AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    export AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    export CREDENTIAL_TYPE='openai'  # or 'azure'
    ```

    **Windows:**

    ```bash
    set OPENAI_API_KEY='your_openai_api_key'
    set AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    set AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    set AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    set CREDENTIAL_TYPE='openai'  # or 'azure'
    ```

3. **Run the example script to ensure everything is set up correctly:**

    ```bash
    python examples/with_openai_credentials.py
    ```

You are now ready to use FlexiAI!

## Setting Up on Ubuntu in WSL on Windows 11

1. **Install WSL and Ubuntu:**

    Follow the official Microsoft guide to [install WSL](https://docs.microsoft.com/en-us/windows/wsl/install) and set up Ubuntu on your Windows 11 machine.

2. **Open Ubuntu in WSL:**

    Open a terminal window and run Ubuntu.

3. **Clone the repository:**

    ```bash
    git clone https://github.com/SavinRazvan/flexiai.git
    cd flexiai
    ```

4. **Install Python and Pip (if not already installed):**

    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv
    ```

5. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

6. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

7. **Set up environment variables:**

    **Option A: Using a `.env` file**

    Create a `.env` file in the root directory with the following content:

    ```bash
    # Your OpenAI API key
    OPENAI_API_KEY='your_openai_api_key'
    # Your Azure OpenAI API key
    AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    # Your Azure OpenAI endpoint
    AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    # Azure OpenAI API version
    AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    # Credential type (either 'openai' or 'azure')
    CREDENTIAL_TYPE='openai'
    ```

    **Option B: Setting environment variables manually**

    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    export AZURE_OPENAI_API_KEY='your_azure_openai_api_key'
    export AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint'
    export AZURE_OPENAI_API_VERSION='2024-05-01-preview'
    export CREDENTIAL_TYPE='openai'  # or 'azure'
    ```

8. **Run the example script to ensure everything is set up correctly:**

    ```bash
    python examples/with_openai_credentials.py
    ```

You are now ready to use FlexiAI on Ubuntu in WSL on Windows 11!

## Troubleshooting

If you encounter any issues during the setup, here are some common solutions:

- **Ensure Python and Pip are installed correctly.** Check the versions:

    ```bash
    python --version
    pip --version
    ```

- **Ensure your virtual environment is activated before running the setup commands.**

- **If using WSL, ensure you have set up WSL correctly and installed Python and Pip in your WSL environment.**

- **If environment variables are not being recognized, double-check your `.env` file or manual setup steps.**

## Additional Configuration

If you need to add additional configuration settings, modify the `config/config.py` file accordingly. You can add new environment variables and update the configuration class to include new settings as needed.

```python
# config/config.py 
import logging
from pydantic_settings import BaseSettings
from pydantic import ValidationError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(BaseSettings):
    OPENAI_API_KEY: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_VERSION: str
    CREDENTIAL_TYPE: str
            
    class Config:
        env_file = ".env"

# Initialize logger
logger = logging.getLogger(__name__)

try:
    # Attempt to load the configuration
    config = Config()
    logger.info("Configuration loaded successfully.")
except ValidationError as e:
    # Log and raise an error if configuration validation fails
    logger.error("Configuration validation error: %s", e)
    raise RuntimeError("Environment variable validation failed. Please check your .env file and ensure all variables are set correctly.") from e
```

By following these setup options, you should be able to configure and run the FlexiAI framework on various environments including Linux, WSL on Windows 11, and Windows. Let me know if you need further assistance!
