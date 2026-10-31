import os 
from langchain_community.document_loaders import PyPDFLoader
DATA_PATH="data"

def load_all_pdfs():
    documents=[]

    for file in os.listdir(DATA_PATH):

        if file.endswith(".pdf"):

            file_path=os.path.join(DATA_PATH,file)

            print(f"\nloading:{file}")

            loader=PyPDFLoader(file_path)

            docs=loader.load()

            print(f"pages loaded from dhruv ji ki file{file}:{len(docs)}")

            documents.extend(docs)


    return documents

if __name__=="__main__":
    docs=load_all_pdfs()
    print("\nTotal pages from all papers:", len(docs))

    print("\nPreview first 500 characters:\n")

    print(docs[0].page_content[:500])

