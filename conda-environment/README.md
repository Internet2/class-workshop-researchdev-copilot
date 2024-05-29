# Setting Up a Conda Environment Using `environment.yml`

This guide will help you set up a Conda environment using the `environment.yml` file provided in this GitHub repository.

## Prerequisites

1. **Install Conda**
    
    Ensure you have [Conda](https://docs.anaconda.com/free/anaconda/install/) installed.

2. **Clone the repository**

   First, clone the repository containing the `environment.yml` file to your local machine and navigate to the directory where the repository is cloned.

   ```bash
   git clone https://github.com/Internet2/class-workshop-researchdev-copilot.git
   cd class-workshop-researchdev-copilot
   ```

## Steps

1. **Create the Conda environment**

   Create a new Conda environment using the `environment.yml` file.

   ```bash
   conda env create -f ./conda-environment/environment.yml
    ```
   This command reads the dependencies listed in the environment.yml file and creates a new Conda environment with those specifications.

2. **Activate the Conda environment**

   Once the environment is created, activate it using the following command:

   ```bash
   conda activate githubcopilotworkshop
   ```

3. **Verify the Installation**

    To ensure that all the packages are installed correctly, you can list the installed packages:

    ```bash
    conda list
    ```

4. **Complete**

    Now you should be ready to use your newly created conda environment in VS Code!

    ![conda-in-vscode.png](./conda-in-vscode.png)
