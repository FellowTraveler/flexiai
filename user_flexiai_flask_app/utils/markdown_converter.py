# utils/markdown_converter.py
import subprocess
import logging


# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def preprocess_markdown(markdown_text):
    """
    Preprocess markdown text to ensure LaTeX formulas are correctly formatted for Pandoc.

    Args:
        markdown_text (str): The markdown text to preprocess.

    Returns:
        str: The preprocessed markdown text.
    """
    # Ensure LaTeX formulas are correctly formatted
    preprocessed_text = markdown_text.replace("\\[", "$$").replace("\\]", "$$")
    return preprocessed_text


def convert_markdown_to_html(markdown_text):
    """
    Convert markdown text to HTML using the Pandoc tool and ensure the output is properly handled.

    Args:
        markdown_text (str): The markdown text to convert.

    Returns:
        str: The converted HTML text. If conversion fails, returns the original markdown text.
    """
    # logger.debug(f"Converting markdown text: {markdown_text}")
    try:
        # Preprocess markdown to ensure LaTeX formulas are recognized
        preprocessed_text = preprocess_markdown(markdown_text)
        # logger.debug(f"Preprocessed markdown text: {preprocessed_text}")

        # Execute the Pandoc command to convert markdown to HTML with LaTeX support
        process = subprocess.Popen(['pandoc', '-f', 'markdown', '-t', 'html', '--mathjax'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=preprocessed_text.encode('utf-8'))

        # Check if the Pandoc command executed successfully
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, stderr.decode('utf-8'))

        # Decode the output from bytes to string
        html_output = stdout.decode('utf-8')
        # logger.debug(f"Pandoc conversion output: {html_output}")

        return html_output
    except subprocess.CalledProcessError as e:
        logger.error(f"Pandoc conversion failed: {e}")
        return markdown_text
    except Exception as e:
        logger.error(f"Error converting markdown to HTML: {e}")
        return markdown_text
    