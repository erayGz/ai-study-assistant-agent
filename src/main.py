from agent import StudyAssistantAgent


def main():
    print("AI Study Assistant Agent")
    print("------------------------")
    print("Available tasks: summary, search, stats")
    print()

    file_path = input("Enter file path: ").strip()
    task_type = input("Choose task type: ").strip()

    query = ""

    if task_type.lower() == "search":
        query = input("Enter your question or keyword: ").strip()

    agent = StudyAssistantAgent(file_path)

    try:
        result = agent.handle_request(task_type, query)
        print("\nResult:")
        print(result)

    except Exception as error:
        print("\nApplication error:")
        print(error)


if __name__ == "__main__":
    main()