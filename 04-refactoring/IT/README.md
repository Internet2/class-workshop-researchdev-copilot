# AI-Assisted Code Refactoring Workshop: Server Monitoring System

## Workshop Overview
This workshop demonstrates how AI coding assistants can help improve error handling and code maintainability in IT systems. Using a server monitoring system as our example, we'll explore common code quality issues and learn how AI can assist in identifying and fixing them.

## Learning Objectives
- Understand how AI can assist in identifying code quality issues
- Learn to translate theoretical best practices into practical improvements
- Experience real-world error handling scenarios
- Bridge the gap between development and IT operations

## The Scenario
We're working with a server monitoring system that represents a common situation in IT:
- A robust third-party tool or API (`mock_ping.py`) that we can't modify
- Our own integration code (`server_availability.py`) that needs improvement
- Real-world challenges like unclear error messages, poor logging, and lost context

### Understanding mock_ping.py
In our workshop, `mock_ping.py` represents third-party APIs or tools that IT teams commonly work with, such as:
- Cloud provider APIs (AWS, Azure, GCP)
- Monitoring tool APIs (Nagios, Zabbix, SolarWinds)
- Network infrastructure APIs (Cisco, F5, etc.)

This file serves as our "API documentation" for the AI, similar to how you might provide AWS documentation when asking AI to help with AWS integrations.

## Project Structure
```
IT
├── server_availability_hints.py            # Initial version of the server availability checker with comments on potential improvements
├── server_availability.py                  # Unrefactored implementation of the server availability checker
├── server_availability_refactored.py       # Refactored version of the server availability checker with enhanced error handling and maintainability
├── mock_ping.py                            # Mock implementation of a ping function which represents a third-party API/tool
├── test-for-intial-code-notebook.ipynb     # Notebook testing the unrefactored server availability checker
├── test-for-refactored-code-notebook.ipynb # Notebook validating the improvements in the refactored server availability checker
└── README.md                               # This file
```

## Workshop Flow
1. **Review Current State**
   - Examine the current `server_availability.py`
   - Identify common issues in error handling and logging
   - Run test scenarios via `test-for-intial-code-notebook.ipynb` to see problematic outputs

2. **Understanding the Context**
   - Learn how `mock_ping.py` represents real-world APIs
   - See how error information gets lost in our integration
   - Identify where improvements are needed

3. **AI-Assisted Refactoring**
   - Use AI to help identify improvements
   - Implement better error handling
   - Add proper logging and resource management
   - Maintain better error context

4. **Validation**
   - Run the same test scenarios via `test-for-refactored-code-notebook.ipynb`
   - Compare output quality
   - Understand the improvements



## Workshop Materials
- `mock_ping.py`: Simulates a third-party API with rich error types
- `server_availability.py`: Starting point with common issues
- `server-test-notebook.ipynb`: Test scenarios for before/after comparison

## Expected Outcomes
After this workshop, participants will:
- Better understand how to work with third-party APIs
- Know how to use AI to improve error handling
- Be able to identify and fix common code quality issues
- Understand how to maintain error context
- Have practical experience with code refactoring