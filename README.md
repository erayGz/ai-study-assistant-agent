# AI Study Assistant Agent

## Project Status

Current stage: Step 2 – First working implementation and tool integration.

## Project Description

AI Study Assistant Agent is a Python-based command-line application that helps users analyse study notes or text documents. The system can read a local `.txt` or `.md` file and return a summary, relevant information based on a search query, or basic document statistics.

The project is implemented as a simple agent-based system. The agent receives user input, decides which tool should be used, processes the document, and returns a meaningful result.

## Features

- Read local `.txt` and `.md` files
- Clean and prepare text
- Search for relevant sentences
- Generate a short extractive summary
- Calculate document statistics
- Handle basic user input errors
- Include basic unit tests with pytest

## Agent-Based Approach

The system uses a single intelligent agent called `StudyAssistantAgent`. The agent controls the workflow of the application:

1. Receive the file path and task type from the user.
2. Load the selected document.
3. Clean and prepare the text.
4. Select the correct tool based on the task.
5. Return the final result to the user.

## Tools Used

The system uses the following tools:

- File Reader Tool
- Text Cleaning Tool
- Search Tool
- Summarisation Tool
- Statistics Tool

## Project Structure

```text
src/
  main.py
  agent.py
  tools.py
  utils.py

tests/
  test_tools.py

data/
  sample_notes.txt

docs/
  journal.md