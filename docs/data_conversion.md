# Data Porting and Conversion

## Input Format

The system accepts local text-based files. The supported file formats are:

- `.txt`
- `.md`

The user provides the file path through the command-line interface.

## Data Processing Flow

The data is processed in the following order:

1. The user enters a file path.
2. The File Reader Tool reads the file content as plain text.
3. The Text Cleaning Tool removes repeated spaces and unnecessary line breaks.
4. The cleaned text is passed to the agent.
5. The agent selects the correct tool depending on the user request.
6. The selected tool returns the final result.

## Data Conversion Details

The original input file is converted into a plain text string. After that, the text is cleaned and split into sentences when needed.

For the search function, the system extracts keywords from the user query and from document sentences. Then it compares the keywords and returns the most relevant sentences.

For the summary function, the system extracts keywords, calculates simple word frequency, scores sentences, and returns selected sentences as a summary.

For the statistics function, the system counts words, sentences, and characters.

## Correctness and Consistency

The system preserves correctness by:

- accepting only supported file formats,
- rejecting empty files,
- cleaning the text before processing,
- using the same cleaned text for all tools,
- returning error messages for invalid input.

This keeps the data flow consistent between the file reader, text cleaner, agent, and task-specific tools.