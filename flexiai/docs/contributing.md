# Contributing to FlexiAI

We welcome contributions to the FlexiAI framework! Please read the following guidelines to get started.

## How to Contribute

1. **Fork the repository**: Click the 'Fork' button on the top right corner of the repository page to create a copy of the repository in your own GitHub account.

2. **Clone your fork**: Clone your forked repository to your local machine.

    ```bash
    git clone https://github.com/SavinRazvan/flexiai.git
    cd flexiai
    ```

3. **Create a branch**: Create a new branch for your feature or bugfix.

    ```bash
    git checkout -b my-feature-branch
    ```

4. **Make changes**: Make your changes to the codebase. Ensure that your code follows the project's coding standards.

5. **Add tests**: If you added new functionality, make sure to add tests for it in the `tests/` directory.

6. **Commit your changes**: Commit your changes with a clear and concise commit message.

    ```bash
    git add .
    git commit -m "Add new feature"
    ```

7. **Push to your fork**: Push your changes to your forked repository.

    ```bash
    git push origin my-feature-branch
    ```

8. **Open a pull request**: Go to the original repository and open a pull request. Provide a clear description of your changes and any related issues.

## Code of Conduct

Please adhere to the [Code of Conduct](https://github.com/SavinRazvan/flexiai/blob/main/CODE_OF_CONDUCT.md) when contributing to this project.

## Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Write clear and concise commit messages.
- Ensure your code is well-documented with comments and docstrings.

## Reporting Issues

If you encounter any issues, please open an issue on GitHub with detailed information about the problem.

## Pull Request Process

1. Ensure your code is well-documented.
2. Ensure that your code follows the project's coding standards.
3. Ensure that all tests pass.
4. Describe your pull request in detail, including what problem it solves and why this solution is necessary.

## Testing

To ensure the quality and reliability of the FlexiAI framework, we require that all contributions include tests where applicable.

### Running Tests

You can run the tests using the following commands:

```bash
# Activate your virtual environment
source venv/bin/activate  # For Linux/WSL
venv\Scripts\activate  # For Windows

# Install the test dependencies
pip install -r requirements.txt

# Run the tests
pytest tests/
```

### Writing Tests

Please write tests for any new functionality you add. Place your tests in the `tests/` directory.

Ensure your tests cover the following:

- Unit tests for individual functions and methods
- Integration tests for larger components or workflows

We use [pytest](https://pytest.org/) as our testing framework. Here are some example tests for the `search_youtube` function:

#### Example Tests

These tests ensure that the `search_youtube` function in `TaskManager` works as expected under various scenarios.

```python
# tests/test_assistant_youtube_search.py
import pytest
import subprocess
from assistant.task_manager import TaskManager

@pytest.fixture
def task_manager():
    return TaskManager()

def test_search_youtube_with_valid_query(task_manager, mocker):
    mock_subprocess_run = mocker.patch('subprocess.run')
    query = "Python tutorials"
    result = task_manager.search_youtube(query)
    print("test_search_youtube_with_valid_query result:", result)
    assert result['status'] == True
    assert result['result'] == "https://www.youtube.com/results?search_query=Python%2Btutorials"
    assert result['message'] == "YouTube search page opened successfully."
    mock_subprocess_run.assert_called_once()

def test_search_youtube_with_empty_query(task_manager):
    query = ""
    result = task_manager.search_youtube(query)
    print("test_search_youtube_with_empty_query result:", result)
    assert result['status'] == False
    assert result['result'] is None
    assert result['message'] == "Query cannot be empty."

def test_search_youtube_with_subprocess_error(task_manager, mocker):
    mock_subprocess_run = mocker.patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'cmd'))
    query = "Python tutorials"
    result = task_manager.search_youtube(query)
    print("test_search_youtube_with_subprocess_error result:", result)
    assert result['status'] == False
    assert result['result'] is None
    assert "Subprocess error" in result['message']
    mock_subprocess_run.assert_called_once()

def test_search_youtube_with_exception(task_manager, mocker):
    mock_subprocess_run = mocker.patch('subprocess.run', side_effect=Exception("Unexpected error"))
    query = "Python tutorials"
    result = task_manager.search_youtube(query)
    print("test_search_youtube_with_exception result:", result)
    assert result['status'] == False
    assert result['result'] is None
    assert "Failed to open YouTube search for query" in result['message']
    mock_subprocess_run.assert_called_once()

if __name__ == "__main__":
    pytest.main()
```

These tests cover the following scenarios:
- A valid query that successfully opens a YouTube search page.
- An empty query that returns an error message.
- A subprocess error that is properly handled.
- A generic exception that is properly handled.

## Community

Join our community to stay updated on the latest developments, share your ideas, and collaborate with other contributors.

- [Join the discussion on GitHub Issues](https://github.com/SavinRazvan/flexiai/issues)

Thank you for contributing to FlexiAI!
