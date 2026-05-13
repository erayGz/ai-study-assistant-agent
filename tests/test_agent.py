import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.append(str(SRC_PATH))

from agent import StudyAssistantAgent


def create_temp_text_file(tmp_path, content, filename="notes.txt"):
    file_path = tmp_path / filename
    file_path.write_text(content, encoding="utf-8")
    return file_path


def test_agent_summary_workflow(tmp_path):
    file_path = create_temp_text_file(
        tmp_path,
        (
            "Artificial intelligence helps students analyse information. "
            "Testing is important for software quality. "
            "Deployment prepares software for practical use."
        )
    )

    agent = StudyAssistantAgent(str(file_path))
    result = agent.handle_request("summary")

    assert "Summary:" in result
    assert "Artificial intelligence" in result


def test_agent_search_workflow(tmp_path):
    file_path = create_temp_text_file(
        tmp_path,
        (
            "Artificial intelligence helps users. "
            "Testing checks software quality. "
            "Deployment prepares software for users."
        )
    )

    agent = StudyAssistantAgent(str(file_path))
    result = agent.handle_request("search", "testing quality")

    assert "Relevant information:" in result
    assert "Testing checks software quality." in result


def test_agent_statistics_workflow(tmp_path):
    file_path = create_temp_text_file(
        tmp_path,
        "AI is useful. Testing is important."
    )

    agent = StudyAssistantAgent(str(file_path))
    result = agent.handle_request("stats")

    assert "Document statistics:" in result
    assert "Word count:" in result
    assert "Sentence count:" in result
    assert "Character count:" in result


def test_agent_empty_search_query(tmp_path):
    file_path = create_temp_text_file(
        tmp_path,
        "Testing is important for software quality."
    )

    agent = StudyAssistantAgent(str(file_path))
    result = agent.handle_request("search", "")

    assert result == "Error: Search query cannot be empty."


def test_agent_unknown_task_type(tmp_path):
    file_path = create_temp_text_file(
        tmp_path,
        "Testing is important."
    )

    agent = StudyAssistantAgent(str(file_path))
    result = agent.handle_request("translate")

    assert "Error: Unknown task type" in result


def test_agent_missing_file_error():
    agent = StudyAssistantAgent("missing_file.txt")

    with pytest.raises(FileNotFoundError):
        agent.handle_request("summary")


def test_agent_unsupported_file_type_error(tmp_path):
    file_path = create_temp_text_file(
        tmp_path,
        "This file type should not be accepted.",
        filename="notes.pdf"
    )

    agent = StudyAssistantAgent(str(file_path))

    with pytest.raises(ValueError):
        agent.handle_request("summary")


def test_agent_empty_file_error(tmp_path):
    file_path = create_temp_text_file(tmp_path, "", filename="empty.txt")

    agent = StudyAssistantAgent(str(file_path))

    with pytest.raises(ValueError):
        agent.handle_request("summary")