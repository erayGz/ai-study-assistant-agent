# Step 3 Test Plan

## Testing Process

Testing was performed after the first working implementation of the AI Study Assistant Agent was completed. The goal of the testing process was to verify that the system can correctly read input files, process user requests, use the correct tool, and return meaningful results.

The testing process includes:

- Tool testing
- Functional testing of the main workflow
- Input validation testing
- Error handling testing
- Agent workflow testing

The project uses `pytest` for automated tests. The tests are stored in the `tests/` folder.

## Test Scenarios

| Test Scenario | Input | Expected Result | Test Type |
|---|---|---|---|
| Clean text test | Text with repeated spaces | Extra spaces are removed | Tool testing |
| Sentence splitting test | Text with multiple sentences | Text is split into separate sentences | Tool testing |
| Keyword extraction test | Text with common words and useful words | Stop words are removed and useful keywords remain | Tool testing |
| Search tool test | Query: `testing software` | Relevant sentence about testing is returned | Tool testing |
| Summary tool test | Multi-sentence text | Short summary is returned | Tool testing |
| Statistics tool test | Short text file | Word count and sentence count are calculated | Tool testing |
| Agent summary workflow | Valid file + `summary` task | Agent returns a summary | Functional testing |
| Agent search workflow | Valid file + `search` task | Agent returns relevant information | Functional testing |
| Agent statistics workflow | Valid file + `stats` task | Agent returns document statistics | Functional testing |
| Empty search query | Search task with empty query | Error message is returned | Input validation |
| Unknown task type | Invalid task name | Error message is returned | Input validation |
| Missing file | Non-existing file path | FileNotFoundError is raised | Error handling |
| Unsupported file type | `.pdf` file | ValueError is raised | Error handling |
| Empty file | Empty `.txt` file | ValueError is raised | Error handling |

## Test Result

The automated tests were executed using:

```bash
python -m pytest