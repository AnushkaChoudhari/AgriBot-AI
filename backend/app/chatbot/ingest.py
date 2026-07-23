from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


from langchain_community.document_loaders import PyPDFLoader
from app.config.settings import DOCS_PATH


def load_documents():
    documents = []

    pdf_files = list(DOCS_PATH.glob("*.pdf"))

    if not pdf_files:
        print("❌ No PDF files found in docs/")
        return []

    for pdf in pdf_files:
        print(f"📄 Loading {pdf.name}")

        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    print(f"\n✅ Loaded {len(documents)} pages.")

    return documents


if __name__ == "__main__":
    docs = load_documents()

    if docs:
        print("\nFirst 500 characters:\n")

        for i in range(min(5, len(docs))):
            print(f"\n------ Page {i+1} ------")
            print(repr(docs[i].page_content[:300]))