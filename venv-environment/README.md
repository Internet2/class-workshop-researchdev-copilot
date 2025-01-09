# Setting Up a Python Virtual Environment Using `venv`

This guide will help you set up a Python virtual environment using `venv` and the `requirements.txt` file provided in this GitHub repository.

## Prerequisites

1. **Install Python**
    
    Ensure you have Python 3.10 or newer installed. You can download Python from the [official Python website](https://www.python.org/downloads/).
   
      - [MacOS](https://www.python.org/downloads/macos/)
      - [Windows](https://www.python.org/downloads/windows/)
      - [Linux](https://www.python.org/downloads/source/) (or use your distribution's package manager)

2. **Clone the repository**

   Ensure you have cloned the repository by following the steps in the [Getting Started section of the main README](../README.md#getting-started) of this repo.

   Once you have cloned the repo, open up your terminal to navigate to the directory of the repo in your local machine.

   ```bash
   cd class-workshop-researchdev-copilot
   ```

## Steps

1. **Create the virtual environment**

   Create a new virtual environment in a directory named `gh-cp-venv`:

   ```bash
   python -m venv gh-cp-venv
   ```

2. **Activate the virtual environment**

   Activate the virtual environment using the appropriate command for your operating system:

   On Windows:
   ```bash
   gh-cp-venv\Scripts\activate
   ```

   On MacOS/Linux:
   ```bash
   source gh-cp-venv/bin/activate
   ```

3. **Install dependencies**

   Navigate to the `venv-environment` directory then run the `pip install` command:

   ```bash
   cd venv-environment
   pip install -r requirements.txt
   ```

4. **Verify the Installation**

    To ensure that all the packages are installed correctly, you can list the installed packages:

    ```bash
    pip list
    ```

4. **Complete**

    Now you should be ready to use your newly created virtual environment in VS Code!
    
    VS Code should automatically detect your virtual environment. You can select it as your Python interpreter by:
    1. Opening the Command Palette (Ctrl+Shift+P or Cmd+Shift+P)
    2. Typing "Python: Select Interpreter"
    3. Choosing the interpreter from the `gh-cp-venv` directory