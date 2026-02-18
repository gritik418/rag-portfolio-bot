from langchain_text_splitters import CharacterTextSplitter

def split_documents(documents,chunk_size=400, chunk_overlap=60):
    splitter = CharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents=documents)

    return chunks

