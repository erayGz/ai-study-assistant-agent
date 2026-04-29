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