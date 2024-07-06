# FlexiAI Documentation

Welcome to the FlexiAI documentation! This guide will help you understand how to set up, use, and contribute to the FlexiAI framework.

## Table of Contents

1. [Introduction](#introduction)
2. [Key Features](#key-features)
3. [Framework Structure](#framework-structure)
4. [Getting Started](#getting-started)
5. [Setup](docs/setup.md)
6. [Usage](docs/usage.md)
7. [API Reference](docs/api_reference.md)
8. [Contributing](docs/contributing.md)

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

### Getting Started

To get started with FlexiAI, follow the [Setup Guide](docs/setup.md) to install and configure the framework. Then, refer to the [Usage Guide](docs/usage.md) for examples of how to use FlexiAI in your projects.

For detailed information on the API methods and classes, see the [API Reference](docs/api_reference.md).

If you want to contribute to FlexiAI, please read the [Contributing Guide](docs/contributing.md) for guidelines on how to get involved.
