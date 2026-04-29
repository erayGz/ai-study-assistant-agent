# AI Study Assistant Agent

## Project Status

Current stage: Step 1 – Project planning and initial structure.

## Project Description

AI Study Assistant Agent is a planned Python-based command-line application. The system will help users analyse study notes or text documents by reading a local file and returning useful results such as summaries, relevant text fragments, or document statistics.

## Planned Agent-Based Approach

The project will use a single intelligent agent. The agent will receive the user's request, select the correct tool, process the input file, and return the result.

## Planned Tools

- File Reader Tool
- Text Cleaning Tool
- Search Tool
- Summarisation Tool
- Statistics Tool

## Planned Project Structure

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