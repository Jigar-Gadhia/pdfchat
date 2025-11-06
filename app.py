from pdf_qa.query import ask_question

if __name__ == "__main__":
    print("📄 PDF Q&A Bot (Gemini + LangChain)")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("❓ Your question: ").strip()
        if question.lower() in ["quit", "exit", "q"]:
            break
        if not question:
            continue

        try:
            answer = ask_question(question)
            print(f"💡 Answer: {answer}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
