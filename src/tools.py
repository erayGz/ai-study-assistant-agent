import re
from pathlib import Path


SUPPORTED_EXTENSIONS = [".txt", ".md"]

STOP_WORDS = {
    "the", "is", "are", "a", "an", "and", "or", "of", "to", "in", "for",
    "with", "on", "by", "as", "that", "this", "it", "be", "can", "from"
}


def read_file(file_path: str) -> str:
    #Reads a local text or Markdown file and returns its content as a string.

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError("Unsupported file format. Only .txt and .md files are supported.")

    content = path.read_text(encoding="utf-8")

    if not content.strip():
        raise ValueError("The input file is empty.")

    return content


def clean_text(text: str) -> str:

    #Cleans text by removing repeated spaces and unnecessary line breaks.

    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def split_into_sentences(text: str) -> list[str]:
    
    #Splits text into sentences using simple punctuation-based sentence detection.

    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def extract_keywords(text: str) -> list[str]:

    #Extracts useful keywords from a user query or sentence.

    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    return [word for word in words if word not in STOP_WORDS]


def search_relevant_sentences(text: str, query: str, max_results: int = 3) -> list[str]:
    #Searches for sentences that are most relevant to the user's query.

    sentences = split_into_sentences(text)
    keywords = extract_keywords(query)

    if not keywords:
        return []

    scored_sentences = []

    for sentence in sentences:
        sentence_words = extract_keywords(sentence)
        score = len(set(keywords).intersection(set(sentence_words)))

        if score > 0:
            scored_sentences.append((score, sentence))

    scored_sentences.sort(key=lambda item: item[0], reverse=True)

    return [sentence for score, sentence in scored_sentences[:max_results]]


def summarize_text(text: str, max_sentences: int = 3) -> str:
    #Creates a simple extractive summary by selecting important sentences.

    sentences = split_into_sentences(text)

    if len(sentences) <= max_sentences:
        return " ".join(sentences)

    word_frequency = {}

    for sentence in sentences:
        for word in extract_keywords(sentence):
            word_frequency[word] = word_frequency.get(word, 0) + 1

    scored_sentences = []

    for index, sentence in enumerate(sentences):
        score = 0

        for word in extract_keywords(sentence):
            score += word_frequency.get(word, 0)

        scored_sentences.append((score, index, sentence))

    scored_sentences.sort(key=lambda item: item[0], reverse=True)

    selected = scored_sentences[:max_sentences]
    selected.sort(key=lambda item: item[1])

    return " ".join(sentence for score, index, sentence in selected)


def calculate_text_statistics(text: str) -> dict:
    #Calculates basic statistics about the document.
    sentences = split_into_sentences(text)
    words = text.split()

    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "character_count": len(text)
    }