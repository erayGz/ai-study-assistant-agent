# Practical Task Journal

## Step 1 – Planned System and Goal

The proposed solution is an AI-enabled Study Assistant Agent developed using the Python language. The primary purpose of the system will be to assist users in analysing their study notes or text documents. In order to perform this function, the system will read the contents of the local text file and produce useful outputs like summaries, excerpts, or general document statistics.

The problem addressed by this system is the need for a simple mechanism to obtain useful information from lengthy texts or notes for analysis. This will be made possible by the use of tool-based text processing.

The system will take input from the user via the command line interface. Users will supply file paths and task types such as summarization, searches, or statistics.

## AI or Agent-Based Approach

The system will be implemented as a single intelligent agent. The agent will control the workflow of the application. It will receive the user request, decide which tool should be used, call the selected tool, and return the result to the user.

The agent-based approach is suitable because the system needs simple decision-making. For example, if the user asks for a summary, the agent will call the summarisation tool. If the user asks to search for a topic, the agent will call the search tool. If the user asks for document statistics, the agent will call the statistics tool.

The planned workflow is:

1. Receive user input.
2. Read the selected file.
3. Clean and prepare the text.
4. Select the correct tool based on the user request.
5. Process the text.
6. Return the result to the user.

## Planned Tools

The planned tools are:

1. File Reader Tool  
   This tool will read the content of a local `.txt` or `.md` file.

2. Text Cleaning Tool  
   This tool will remove unnecessary spaces and prepare the text for processing.

3. Search Tool  
   This tool will search for sentences related to the user's question or keyword.

4. Summarisation Tool  
   This tool will generate a short summary from the document.

5. Statistics Tool  
   This tool will calculate basic information such as word count, sentence count, and character count.

## Preliminary Programming Concepts

The project will require the following programming concepts:

- Functions for separating different tools and operations.
- Classes for implementing the agent structure.
- File handling for reading local text files.
- Lists for storing sentences and search results.
- Dictionaries for storing structured statistics.
- String processing for cleaning and analysing text.
- Conditional statements for selecting the correct tool.
- Error handling for invalid file paths or unsupported file formats.
- Basic testing with pytest.
- Git version control for tracking the development process.

## Current Step 1 Status

At this stage, the project structure has been created. The planned system, agent-based approach, required tools, and programming concepts have been defined. The next step will be to implement the first working version of the Python application.

## Step 2 – Updated System Description Based on Implementation Progress

The system has been implemented as a command-line Python application. The current version allows the user to provide a local `.txt` or `.md` file and select one of three task types: summary, search, or statistics. The agent reads the document, cleans the text, selects the correct tool, processes the content, and returns a meaningful result.

The current implementation follows the system idea described in Step 1. The main difference is that the planned tools have now been implemented as Python functions and connected through the agent workflow.

## Refined Programming Concepts Actually Used

The following programming concepts are used in the implemented system:

- Classes
- Functions
- File handling
- Lists
- Dictionaries
- String processing
- Regular expressions
- Conditional statements
- Exception handling
- Modular programming
- Basic unit testing with pytest
- Git version control

## How These Concepts Are Applied in the Project

The `StudyAssistantAgent` class is used to represent the main agent. This class stores the file path, loads the document, and decides which tool should be used based on the user's selected task.

Functions are used to separate the tools of the system. For example, `read_file()` is responsible for reading local files, `clean_text()` prepares the input text, `search_relevant_sentences()` finds relevant information, `summarize_text()` generates a short extractive summary, and `calculate_text_statistics()` returns basic document statistics.

Lists are used to store sentences and search results. Dictionaries are used to return structured statistics such as word count, sentence count, and character count. Regular expressions are used for text cleaning, sentence splitting, and keyword extraction. Conditional statements are used inside the agent to select the correct tool. Exception handling is used to manage missing files, unsupported file formats, and empty files.

## Tool Integration

The tools are integrated through the agent workflow. The user starts the program and provides a file path and task type. The agent first calls the File Reader Tool to read the document. Then it calls the Text Cleaning Tool to prepare the data. After that, the agent selects one of the task-specific tools:

- Summary Tool: creates a short extractive summary from the document.
- Search Tool: finds sentences related to the user's query.
- Statistics Tool: calculates word count, sentence count, and character count.

This structure makes the system modular because each tool has a separate responsibility. The agent works as the controller that connects user input, tool execution, and final output.

## Current Step 2 Status

At this stage, the first working version of the system has been implemented. The application can be launched from the command line, process a user-selected file, use different tools, and return results. Basic unit tests have also been added for the text-processing tools.

## Step 3 – Testing Process, Deployment Preparation, and Data Conversion

At this stage, the project was extended with automated testing, deployment preparation, and data conversion documentation. The main implementation from Step 2 was tested using both automated tests and manual command-line execution.

The purpose of Step 3 was to verify that the AI Study Assistant Agent works correctly, handles invalid input, and can be prepared for controlled local deployment.

## Testing Process

The testing process includes:

- tool testing,
- functional testing of the main workflow,
- input validation testing,
- error handling testing,
- agent workflow testing.

The project uses `pytest` for automated testing. The tests are stored in the `tests/` folder.

The tool tests verify that the individual text-processing functions work correctly. These tests cover text cleaning, sentence splitting, keyword extraction, search, summarisation, and statistics calculation.

The agent tests verify that the main system workflow works correctly when the user selects `summary`, `search`, or `stats`. These tests also check invalid input situations such as an empty search query, unknown task type, missing file, unsupported file type, and empty file.

## Test Scenarios

The main test scenarios are:

1. Text cleaning test – verifies that repeated spaces are removed.
2. Sentence splitting test – verifies that text is divided into separate sentences.
3. Keyword extraction test – verifies that useful keywords are extracted and common words are ignored.
4. Search tool test – verifies that relevant sentences are returned for a search query.
5. Summary tool test – verifies that a short summary is generated.
6. Statistics tool test – verifies that word count and sentence count are calculated.
7. Agent summary workflow test – verifies that the agent returns a summary for a valid file.
8. Agent search workflow test – verifies that the agent returns relevant information for a query.
9. Agent statistics workflow test – verifies that document statistics are returned.
10. Empty search query test – verifies input validation.
11. Unknown task type test – verifies task validation.
12. Missing file test – verifies error handling.
13. Unsupported file type test – verifies error handling.
14. Empty file test – verifies error handling.

The final automated test result for Step 3 was:

14 passed

## Final Submission – Completed System

In the final stage, the AI Study Assistant Agent was completed as a working Python-based command-line application. The system includes an agent-based workflow, tool functions, user input handling, automated testing, deployment preparation, and documentation.

The final version of the system can read local `.txt` and `.md` files, clean the input text, generate a short summary, search for relevant sentences, and calculate document statistics. The agent controls the workflow by receiving the user request, selecting the correct tool, and returning the result.

The final system includes the following main parts:

- `src/main.py` – command-line interface and user input handling,
- `src/agent.py` – agent workflow and task selection,
- `src/tools.py` – file reading, text cleaning, search, summary, and statistics tools,
- `tests/test_tools.py` – tests for tool functions,
- `tests/test_agent.py` – tests for the main agent workflow,
- `docs/test_plan.md` – testing process and test scenarios,
- `docs/deployment.md` – deployment preparation,
- `docs/data_conversion.md` – data conversion and processing explanation,
- `docs/final_report.md` – final project report.

The final testing result was:

14 passed
