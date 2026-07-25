from app.chatbot.retriever import get_retriever

retriever = get_retriever()


def search_documents(question: str):

    docs = retriever.invoke(question)

    print("\n========== RETRIEVED DOCUMENTS ==========\n")

    if not docs:
        print("No documents retrieved.")
    else:
        for i, doc in enumerate(docs, start=1):
            print(f"\n----- Document {i} -----")
            print(doc.page_content[:500])

    context = "\n\n".join(doc.page_content for doc in docs)

    return context

if __name__ == "__main__":

    context = search_documents("What is grape black rot?")

    print("\n========== CONTEXT ==========\n")

    print(context[:1000])