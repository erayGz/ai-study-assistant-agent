from tools import (
    read_file,
    clean_text,
    search_relevant_sentences,
    summarize_text,
    calculate_text_statistics
)


class StudyAssistantAgent:
    """
    A simple intelligent agent that analyses study notes using tool functions.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.raw_text = ""
        self.cleaned_text = ""

    def load_document(self) -> None:
        """
        Loads and prepares the document before processing.
        """
        self.raw_text = read_file(self.file_path)
        self.cleaned_text = clean_text(self.raw_text)

    def handle_request(self, task_type: str, query: str = "") -> str:
        """
        Decides which tool should be used based on the user's request.
        """
        if not self.cleaned_text:
            self.load_document()

        task_type = task_type.lower().strip()

        if task_type == "summary":
            summary = summarize_text(self.cleaned_text)
            return f"Summary:\n{summary}"

        if task_type == "search":
            if not query.strip():
                return "Error: Search query cannot be empty."

            results = search_relevant_sentences(self.cleaned_text, query)

            if not results:
                return "No relevant information was found."

            formatted_results = "\n".join(f"- {sentence}" for sentence in results)
            return f"Relevant information:\n{formatted_results}"

        if task_type == "stats":
            stats = calculate_text_statistics(self.cleaned_text)

            return (
                "Document statistics:\n"
                f"- Word count: {stats['word_count']}\n"
                f"- Sentence count: {stats['sentence_count']}\n"
                f"- Character count: {stats['character_count']}"
            )

        return "Error: Unknown task type. Please use summary, search, or stats."