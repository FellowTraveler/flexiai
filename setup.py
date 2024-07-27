# setup.py
from setuptools import setup, find_packages

def read_readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

setup(
    name='flexiai',
    version='1.0.9',
    packages=find_packages(include=['flexiai', 'flexiai.*']),
    include_package_data=True,
    package_data={
        'flexiai': [
            'assistant/*.py',
            'config/*.py',
            'core/*.py',
            'core/flexi_managers/*.py',
            'core/utils/*.py',
            'credentials/*.py',
            'scripts/*.py',
            'tests/*.py'
        ],
    },
    install_requires=[
        'annotated-types==0.7.0',
        'anyio==4.4.0',
        'azure-common==1.1.28',
        'azure-core==1.30.2',
        'azure-identity==1.17.1',
        'azure-mgmt-core==1.4.0',
        'azure-mgmt-resource==23.1.1',
        'blinker==1.8.2',
        'certifi==2024.7.4',
        'cffi==1.16.0',
        'charset-normalizer==3.3.2',
        'click==8.1.7',
        'cryptography==43.0.0',
        'distro==1.9.0',
        'Flask==3.0.3',
        'glob2==0.7',
        'h11==0.14.0',
        'httpcore==1.0.5',
        'httpx==0.27.0',
        'idna==3.7',
        'iniconfig==2.0.0',
        'isodate==0.6.1',
        'itsdangerous==2.2.0',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'msal==1.30.0',
        'msal-extensions==1.2.0',
        'nest-asyncio==1.6.0',
        'openai==1.35.0',
        'packaging==24.1',
        'platformdirs==3.7.0',
        'pluggy==1.5.0',
        'portalocker==2.10.1',
        'pycparser==2.22',
        'pydantic==2.7.4',
        'pydantic-settings==2.3.3',
        'pydantic_core==2.18.4',
        'PyJWT==2.8.0',
        'pytest==8.3.1',
        'python-dotenv==1.0.1',
        'requests==2.32.3',
        'six==1.16.0',
        'sniffio==1.3.1',
        'tqdm==4.66.4',
        'typing_extensions==4.12.2',
        'urllib3==2.2.2',
        'Werkzeug==3.0.3',
    ],
    entry_points={
        'console_scripts': [
            # To track and fix path
            'setup-flexiai-rag=flexiai.scripts.flexiai_rag_extension:setup_project',
            'setup-flexiai-flask-app=flexiai.scripts.flexiai_basic_flask_app:setup_project',
        ],
    },
    author='Savin Ionut Razvan',
    author_email='razvan.i.savin@gmail.com',
    description="FlexiAI: A dynamic and modular AI framework leveraging Multi-Agent Systems and Retrieval Augmented Generation (RAG) for seamless integration with OpenAI and Azure OpenAI services.",
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/SavinRazvan/flexiai',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
    ],
    python_requires='>=3.10.14',
    project_urls={
        'Bug Reports': 'https://github.com/SavinRazvan/flexiai/issues',
        'Source': 'https://github.com/SavinRazvan/flexiai',
    },
    license='MIT',
)
