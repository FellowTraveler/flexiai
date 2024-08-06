# Project Mapping

This document provides a comprehensive overview and mapping of the FlexiAI project structure. It is designed to help users navigate and understand the various components and files within the project.

## Table of Contents

1. [GitHub Repository Structure](#github-repository-structure)
2. [PyPI Build Structure](#pypi-build-structure)
3. [FlexiAI Basic Flask Chat Application Structure](#flexiai-basic-flask-chat-application-structure)
4. [FlexiAI RAG Extension Structure](#flexiai-rag-extension-structure)
5. [Other Files](#other-files)
6. [File Details](#file-details)

---

### GitHub Repository Structure

```plaintext
📦flexiai
 ┣ 📂.git
 ┃ ┗ ...
 ┣ 📂.github
 ┃ ┣ 📂ISSUE_TEMPLATE
 ┃ ┃ ┣ 📜bug_report.md
 ┃ ┃ ┗ 📜feature_request.md
 ┃ ┗ 📂workflows
 ┃ ┃ ┗ 📜workflow.yml
 ┣ 📂.vscode
 ┃ ┗ 📜extensions.json
 ┣ 📂assets
 ┃ ┣ 📜flexiai_framework_01.png
 ┃ ┣ 📜flexiai_framework_02.png
 ┃ ┗ 📜flexiai_framework_03.png
 ┣ 📂docs
 ┃ ┣ 📜api_reference.md
 ┃ ┣ 📜contributing.md
 ┃ ┣ 📜index.md
 ┃ ┣ 📜project_mapping.md
 ┃ ┣ 📜setup.md
 ┃ ┗ 📜usage.md
 ┣ 📂examples
 ┃ ┣ 📂Code examples
 ┃ ┃ ┣ 📜audio_manager.ipynb
 ┃ ┃ ┣ 📜basic_example_cli_chat.py
 ┃ ┃ ┣ 📜call_parallel_functions.ipynb
 ┃ ┃ ┣ 📜client_tests.ipynb
 ┃ ┃ ┣ 📜dynamic_msg_and_metadata.ipynb
 ┃ ┃ ┣ 📜embeddings_manager.ipynb
 ┃ ┃ ┣ 📜handle_requires_action.ipynb
 ┃ ┃ ┣ 📜images_manager.ipynb
 ┃ ┃ ┣ 📜thread_manager_tests.ipynb
 ┃ ┃ ┣ 📜usage_helpers.ipynb
 ┃ ┃ ┗ 📜vector_store.ipynb
 ┃ ┗ 📂Instructions and functions examples
 ┃ ┃ ┣ 📜MAS Alpha.md
 ┃ ┃ ┣ 📜MAS Beta One.md
 ┃ ┃ ┣ 📜MAS Beta Two.md
 ┃ ┃ ┣ 📜MAS Gamma.md
 ┃ ┃ ┣ 📜assistant_using_csv.md
 ┃ ┃ ┗ 📜assistant_with_search_youtube.md
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
 ┃ ┃ ┣ 📂flexi_managers
 ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┣ 📜audio_manager.py
 ┃ ┃ ┃ ┣ 📜embedding_manager.py
 ┃ ┃ ┃ ┣ 📜images_manager.py
 ┃ ┃ ┃ ┣ 📜message_manager.py
 ┃ ┃ ┃ ┣ 📜multi_agent_system.py
 ┃ ┃ ┃ ┣ 📜run_manager.py
 ┃ ┃ ┃ ┣ 📜session_manager.py
 ┃ ┃ ┃ ┣ 📜thread_manager.py
 ┃ ┃ ┃ ┗ 📜vector_store_manager.py
 ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┗ 📜helpers.py
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜flexiai_client.py
 ┃ ┣ 📂credentials
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜azure_openai_credential_strategy.py
 ┃ ┃ ┣ 📜credential_manager.py
 ┃ ┃ ┣ 📜credential_strategy.py
 ┃ ┃ ┗ 📜openai_credential_strategy.py
 ┃ ┣ 📂scripts
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜flexiai_basic_flask_app.py
 ┃ ┃ ┗ 📜flexiai_rag_extension.py
 ┃ ┣ 📂tests
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜test_assistant_youtube_search.py
 ┃ ┗ 📜__init__.py
 ┣ 📂logs
 ┃ ┗ 📜app.log
 ┣ 📂user_flexiai_flask_app
 ┃ ┣ 📂routes
 ┃ ┃ ┗ 📜api.py
 ┃ ┣ 📂static
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┗ 📜styles.css
 ┃ ┃ ┣ 📂images
 ┃ ┃ ┃ ┣ 📂other_images
 ┃ ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 161351.png
 ┃ ┃ ┃ ┃ ┣ 📜Screenshot 2024-07-12 161358.png
 ┃ ┃ ┃ ┃ ┗ ...
 ┃ ┃ ┃ ┣ 📜assistant.png
 ┃ ┃ ┃ ┗ 📜user.png
 ┃ ┃ ┣ 📂js
 ┃ ┃ ┃ ┗ 📜scripts.js
 ┃ ┃ ┗ 📜favicon.ico
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📜index.html
 ┃ ┣ 📂utils
 ┃ ┃ ┗ 📜markdown_converter.py
 ┃ ┗ 📜app.py
 ┣ 📂user_flexiai_rag
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📂audio
 ┃ ┃ ┃ ┣ 📜Travelers_of_the_Cosmos.mp3
 ┃ ┃ ┃ ┣ 📜output.mp3
 ┃ ┃ ┃ ┣ 📜output_hd.mp3
 ┃ ┃ ┃ ┗ 📜test_output.wav
 ┃ ┃ ┣ 📂csv
 ┃ ┃ ┃ ┣ 📜identify_person.csv
 ┃ ┃ ┃ ┗ 📜products.csv
 ┃ ┃ ┣ 📂images
 ┃ ┃ ┃ ┣ 📜generated_image_1bc706cc-85e5-4b53-b6f7-af3810d79177.png
 ┃ ┃ ┃ ┗ 📜generated_image_e0939e56-d9c2-4a0b-8ec2-366a50df918f.png
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜user_function_mapping.py
 ┃ ┣ 📜user_helpers.py
 ┃ ┗ 📜user_task_manager.py
 ┣ 📜.env
 ┣ 📜.env.template
 ┣ 📜.gitignore
 ┣ 📜CODE_OF_CONDUCT.md
 ┣ 📜LICENSE.txt
 ┣ 📜MANIFEST.in
 ┣ 📜README.md
 ┣ 📜TODO.md
 ┣ 📜chat.py
 ┣ 📜flexiai_basic_flask_app.py
 ┣ 📜flexiai_rag_extension.py
 ┣ 📜pyproject.toml
 ┣ 📜requirements.txt
 ┗ 📜setup.py
```

---

### PyPI Build Structure

```plaintext
📦flexiai
 ┣ 📂assistant
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜function_mapping.py
 ┃ ┗ 📜task_manager.py
 ┣ 📂config
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜config.py
 ┃ ┗ 📜logging_config.py
 ┣ 📂core
 ┃ ┣ 📂flexi_managers
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜audio_manager.py
 ┃ ┃ ┣ 📜embedding_manager.py
 ┃ ┃ ┣ 📜images_manager.py
 ┃ ┃ ┣ 📜message_manager.py
 ┃ ┃ ┣ 📜multi_agent_system.py
 ┃ ┃ ┣ 📜run_manager.py
 ┃ ┃ ┣ 📜session_manager.py
 ┃ ┃ ┣ 📜thread_manager.py
 ┃ ┃ ┗ 📜vector_store_manager.py
 ┃ ┣ 📂utils
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜helpers.py
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜flexiai_client.py
 ┣ 📂credentials
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜azure_openai_credential_strategy.py
 ┃ ┣ 📜credential_manager.py
 ┃ ┣ 📜credential_strategy.py
 ┃ ┗ 📜openai_credential_strategy.py
 ┣ 📂scripts
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜flexiai_basic_flask_app.py
 ┃ ┗ 📜flexiai_rag_extension.py
 ┣ 📂tests
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜test_assistant_youtube_search.py
 ┗ 📜__init__.py
```

---

### FlexiAI Basic Flask Chat Application Structure

```plaintext
📦user_flexiai_flask_app
 ┣ 📂logs
 ┣ 📂routes
 ┃ ┗ 📜api.py
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📜assistant.png
 ┃ ┃ ┗ 📜user.png
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js
 ┃ ┗ 📜favicon.ico
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┃ 📂utils
 ┃ ┗ 📜markdown_converter.py
 ┣ 📜.env
 ┣ 📜app.py
 ┗ 📜requirements.txt
```

---

### FlexiAI RAG Extension Structure

```plaintext
📦user_flexiai_rag
 ┣ 📂data
 ┃ ┣ 📂audio
 ┃ ┃ ┣ 📜Travelers_of_the_Cosmos.mp3
 ┃ ┃ ┣ 📜output.mp3
 ┃ ┃ ┣ 📜output_hd.mp3
 ┃ ┃ ┗ 📜test_output.wav
 ┃ ┣ 📂csv
 ┃ ┃ ┣ 📜identify_person.csv
 ┃ ┃ ┗ 📜products.csv
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📜generated_image_1bc706cc-85e5-4b53-b6f7-af3810d79177.png
 ┃ ┃ ┗ 📜generated_image_e0939e56-d9c2-4a0b-8ec2-366a50df918f.png
 ┣ 📜__init__.py
 ┣ 📜user_function_mapping.py
 ┣ 📜user_helpers.py
 ┗ 📜user_task_manager.py
```

---

### Other Files

- `.env`, `.env.template`, `.gitignore`, `CODE_OF_CONDUCT.md`, `LICENSE.txt`, `MANIFEST.in`, `README.md`, `TODO.md`, `chat.py`, `flexiai_basic_flask_app.py`, `flexiai_rag_extension.py`, `pyproject.toml`, `requirements.txt`, `setup.py`

---

### File Details

#### user\_flexiai\_rag Directory

*   **data**:
    *   Various subdirectories for storing audio, CSV, and image files.

*   **`__init__.py`**:
    - Empty file, used to mark the directory as a Python package.

*   **`user_function_mapping.py`**:
    - Contains the `register_user_tasks` function, which registers user-defined tasks with the FlexiAI framework. It initializes the `UserTaskManager` and sets up mappings for personal and assistant functions.

*   **`user_helpers.py`**:
    - Empty file, intended for the user to store helper functions.

*   **`user_task_manager.py`**:
    - Defines the `UserTaskManager` class, which handles user-defined tasks for AI assistants, enabling Retrieval-Augmented Generation (RAG) capabilities and interaction within the Multi-Agent System.
