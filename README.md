# AI Study Assistant Agent

## Project Status

Current stage: Final Submission – Completed version.

## Project Description

AI Study Assistant Agent is a Python-based command-line application that helps users analyse study notes or text documents. The system can read a local `.txt` or `.md` file and return a summary, relevant information based on a search query, or basic document statistics.

The project is implemented as a simple agent-based system. The agent receives user input, decides which tool should be used, processes the document, and returns a meaningful result.

## Features

- Read local `.txt` and `.md` files
- Clean and prepare text
- Search for relevant sentences
- Generate a short extractive summary
- Calculate document statistics
- Handle invalid input and basic errors
- Include automated tests with pytest
- Include testing, deployment, data conversion, and final report documentation

## Agent-Based Approach

The system uses a single intelligent agent called `StudyAssistantAgent`. The agent controls the workflow of the application:

1. Receive the file path and task type from the user.
2. Load the selected document.
3. Clean and prepare the text.
4. Select the correct tool based on the task.
5. Return the final result to the user.

The agent can select one of the following task types:

- `summary`
- `search`
- `stats`

## Tools Used

The system uses the following tools:

- **File Reader Tool** – reads local `.txt` and `.md` files.
- **Text Cleaning Tool** – removes repeated spaces and prepares text for processing.
- **Search Tool** – finds sentences related to the user's query.
- **Summarisation Tool** – generates a short extractive summary.
- **Statistics Tool** – calculates word count, sentence count, and character count.

## Project Structure

```text
src/
  main.py
  agent.py
  tools.py
  utils.py

tests/
  test_tools.py
  test_agent.py

data/
  sample_notes.txt

docs/
  journal.md
  test_plan.md
  deployment.md
  data_conversion.md
  final_report.md

README.md
requirements.txt
