# utils/markdown_converter.py
import pypandoc
import logging

logger = logging.getLogger(__name__)

def preprocess_markdown(markdown_text):
    """
    Preprocess markdown text to ensure LaTeX formulas are correctly formatted for Pandoc.
    """
    preprocessed_text = markdown_text.replace("\\[", "$$").replace("\\]", "$$")
    return preprocessed_text

def convert_markdown_to_html(markdown_text):
    """
    Convert markdown text to HTML using the pypandoc library.

    Args:
        markdown_text (str): The markdown text to convert.

    Returns:
        str: The converted HTML text. If conversion fails, returns the original markdown text.
    """
    try:
        preprocessed_text = preprocess_markdown(markdown_text)
        
        # Convert markdown to HTML using pypandoc
        html_output = pypandoc.convert_text(preprocessed_text, 'html', format='md', extra_args=['--mathjax'])
        
        return html_output
    except Exception as e:
        logger.error(f"Error converting markdown to HTML: {e}")
        return markdown_text




# # ============================================================================= #
# # The version using subprocess (you must have pandoc installed in your system   #
# # and to be on path to work correctly):                                         #
# # ============================================================================= #

# # utils/markdown_converter.py
# import subprocess
# import logging

# logger = logging.getLogger(__name__)


# def preprocess_markdown(markdown_text):
#     """
#     Preprocess markdown text to ensure LaTeX formulas are correctly formatted for Pandoc.
#     """
#     preprocessed_text = markdown_text.replace("\\[", "$$").replace("\\]", "$$")
#     return preprocessed_text


# def convert_markdown_to_html(markdown_text):
#     """
#     Convert markdown text to HTML using the Pandoc tool and ensure the output is properly handled.

#     Args:
#         markdown_text (str): The markdown text to convert.

#     Returns:
#         str: The converted HTML text. If conversion fails, returns the original markdown text.
#     """
#     try:
#         preprocessed_text = preprocess_markdown(markdown_text)

#         process = subprocess.Popen(['pandoc', '-f', 'markdown', '-t', 'html', '--mathjax'],
#                                    stdin=subprocess.PIPE,
#                                    stdout=subprocess.PIPE,
#                                    stderr=subprocess.PIPE)
#         stdout, stderr = process.communicate(input=preprocessed_text.encode('utf-8'))

#         if process.returncode != 0:
#             raise subprocess.CalledProcessError(process.returncode, stderr.decode('utf-8'))

#         html_output = stdout.decode('utf-8')

#         return html_output
#     except subprocess.CalledProcessError as e:
#         logger.error(f"Pandoc conversion failed: {e}")
#         return markdown_text
#     except Exception as e:
#         logger.error(f"Error converting markdown to HTML: {e}")
#         return markdown_text
