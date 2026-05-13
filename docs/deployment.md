# Deployment Preparation

## Deployment Type

The current version of the AI Study Assistant Agent is prepared as a local command-line application. It does not require a web server or cloud platform. This deployment type is suitable for the current project because the system works with local text files and can be executed in a controlled environment.

## Requirements

The project requires:

- Python 3.10 or newer
- pip
- pytest for testing

Dependencies are listed in:

```text
requirements.txt
```

## Deployment Steps

The system can be deployed locally by following these steps:

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests to verify the installation:
   ```bash
   python -m pytest
   ```

5. Use the application:
   ```bash
   python -m src.app <filename> <task_type> [optional_arguments]
   ```

## Infrastructure Requirements

The system requires:

- Operating System: Windows, Linux, or macOS
- Disk Space: ~50 MB for the application files
- RAM: Minimum 2 GB
- Python: Version 3.10 or higher

No special hardware or cloud infrastructure is required for local deployment.