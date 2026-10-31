from load_pdfs import load_all_pdfs
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    
    chunks=splitter.split_documents(documents)

    return chunks

if __name__=="__main__":

    documents=load_all_pdfs()

    chunks=split_documents(documents)

    print('total original pages',len(documents))

    print('Total chunks created',len(documents))

    print("\nExample chunk preview:\n")
    print(chunks[0].page_content[:500])


