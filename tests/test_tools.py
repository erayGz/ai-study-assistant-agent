import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.append(str(SRC_PATH))

from tools import (
    clean_text,
    split_into_sentences,
    extract_keywords,
    search_relevant_sentences,
    summarize_text,
    calculate_text_statistics
)


def test_clean_text_removes_extra_spaces():
    text = "  This   is     a test.  "
    result = clean_text(text)
    assert result == "This is a test."


def test_split_into_sentences():
    text = "AI is useful. Testing is important."
    result = split_into_sentences(text)
    assert len(result) == 2


def test_extract_keywords_removes_common_words():
    text = "This is a test about artificial intelligence."
    result = extract_keywords(text)
    assert "artificial" in result
    assert "intelligence" in result
    assert "this" not in result


def test_search_relevant_sentences():
    text = "AI helps users. Testing checks software quality. Deployment prepares software for users."
    result = search_relevant_sentences(text, "testing software")
    assert len(result) > 0
    assert "Testing" in result[0]


def test_summarize_text_returns_text():
    text = (
        "Artificial intelligence helps users. "
        "Testing is important for software quality. "
        "Deployment prepares the system for use. "
        "Agents can select tools."
    )
    result = summarize_text(text, max_sentences=2)
    assert isinstance(result, str)
    assert len(result) > 0


def test_calculate_text_statistics():
    text = "AI is useful. Testing is important."
    stats = calculate_text_statistics(text)
    assert stats["word_count"] == 6
    assert stats["sentence_count"] == 2