# Troubleshooting Guide for VS Code and Conda Issues

This document provides solutions for common issues encountered while using GitHub Copilot, Conda environments, and Visual Studio Code (VS Code). The troubleshooting steps include restarting VS Code, modifying settings, and utilizing command-line instructions. References to relevant discussions and documentation are provided for further assistance.

## Issue: GitHub Copilot Won't Complete Prompts

**Solution 1:**
- Restart VS Code.

**Solution 2:**
- Check if `"editor.inlineSuggest.enabled": false` in your settings.
  - If it is set to `false`, set it to `true` and GitHub Copilot should be back up again.
  - Reference: [Stack Overflow](https://stackoverflow.com/questions/76396755/github-copilot-does-not-suggest-anything-anymore-after-i-fiddled-around-with-vsc)

## Issue: Conda Env Won't Show Up in VS Code Under Kernel Selection

**Solution:**
- Restart VS Code.

## Issue: Conda Env Won't Show Up in VS Code Terminal

**Solution 1:**
- Open your terminal in VS Code.
- Then within the terminal, type: `conda init`.
- Close and reopen the terminal.
- Use Conda normally.
  - Reference: [Stack Overflow](https://stackoverflow.com/questions/61986052/visual-studio-code-terminal-doesnt-activate-conda-environment)

**Solution 2:**
- Open up your terminal.
- Activate the environment by running the command: `conda activate githubcopilotworkshop`.
- Start Visual Studio Code from the Anaconda/Miniconda terminal: `code`.
  - Reference: [Stack Overflow](https://stackoverflow.com/questions/65064740/error-when-trying-to-use-conda-on-visual-studio-code-conda-the-term-conda)

## Issue: SSL Connection Errors

**Solution:**
- Refer to the [Conda documentation on SSL connection errors](https://docs.conda.io/projects/conda/en/latest/user-guide/troubleshooting.html#the-system-cannot-find-the-path-specified-on-windows:~:text=library%20load%20failed-,SSL%20connection%20errors,-Permission%20denied%20errors).

## Issue: Shell Commands Open from the Wrong Location

**Solution:**
- Refer to the [Conda documentation on shell command issues](https://docs.conda.io/projects/conda/en/latest/user-guide/troubleshooting.html#shell-commands-open-from-the-wrong-location).

## Issue: The System Cannot Find the Path Specified on Windows

**Solution:**
- Refer to the [Conda documentation on path issues](https://docs.conda.io/projects/conda/en/latest/user-guide/troubleshooting.html#the-system-cannot-find-the-path-specified-on-windows).

## More Troubleshooting Guides for Conda

- Visit the [Conda troubleshooting documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/troubleshooting.html) for more guides.