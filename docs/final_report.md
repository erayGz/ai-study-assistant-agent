# Final Report – AI Study Assistant Agent

## Final System Description and Goal

AI Study Assistant Agent is a Python-based command-line application that helps users analyse study notes or text documents. The system receives a local `.txt` or `.md` file as input, processes the file content, and returns a meaningful result based on the selected task.

The main goal of the system is to support students or users who need a simple tool for analysing text documents. The system can generate a short summary, search for relevant sentences based on a query, and calculate basic document statistics.

The project follows an agent-based approach. A single intelligent agent controls the workflow by receiving the user request, loading the document, cleaning the text, selecting the correct tool, and returning the result.

## Final Explanation of Programming Concepts and Their Usage

The project uses the following programming concepts:

- **Classes**: The `StudyAssistantAgent` class represents the main agent of the system.
- **Functions**: Tool functions are separated into independent functions such as file reading, text cleaning, searching, summarisation, and statistics calculation.
- **File handling**: The system reads local `.txt` and `.md` files.
- **Lists**: Lists are used to store sentences, extracted keywords, and search results.
- **Dictionaries**: Dictionaries are used to return structured statistics such as word count, sentence count, and character count.
- **String processing**: Text is cleaned, split into sentences, and analysed using string operations.
- **Regular expressions**: Regular expressions are used for cleaning text, sentence splitting, and keyword extraction.
- **Conditional statements**: The agent selects the correct tool depending on the task type.
- **Exception handling**: The system handles missing files, unsupported file formats, and empty files.
- **Modular programming**: The code is divided into separate modules: `main.py`, `agent.py`, and `tools.py`.
- **Testing with pytest**: Automated tests are used to verify tool functions and the agent workflow.
- **Git version control**: Git and GitHub are used to show the development progress across the submission stages.

## Final Description of Tools and Their Role

The system uses several internal tools:

1. **File Reader Tool**  
   Reads the content of local `.txt` and `.md` files.

2. **Text Cleaning Tool**  
   Removes repeated spaces and unnecessary line breaks before processing.

3. **Search Tool**  
   Extracts keywords from the user query and finds relevant sentences from the document.

4. **Summarisation Tool**  
   Creates a short extractive summary by scoring sentences using keyword frequency.

5. **Statistics Tool**  
   Calculates word count, sentence count, and character count.

These tools are connected through the `StudyAssistantAgent`. The agent works as the controller that decides which tool should be used based on the user request.

## Final Testing Results and Conclusions

The system was tested using automated tests with `pytest`. The tests cover both individual tool functions and the complete agent workflow.

The final test result was:

```text
14 passed
