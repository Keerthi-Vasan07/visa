import os
import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction

def store_in_chroma(chunks, embeddings, pdf_name="document.pdf"):
    # 1. Initialize Persistent Client (saves to a folder named 'chroma_db')
    client = chromadb.PersistentClient(path="./chroma_db")

    # 2. Define the Embedding Function to match your Ollama model
    # This allows Chroma to understand how to handle these vectors later
    ollama_ef = OllamaEmbeddingFunction(
        url="http://localhost:11434/api/embeddings",
        model_name="mxbai-embed-large"
    )

    # 3. Create or Get a Collection (think of this as a table)
    collection = client.get_or_create_collection(
        name="pdf_collection",
        embedding_function=ollama_ef
    )

    # 4. Prepare IDs and Metadata
    # Each chunk needs a unique ID
    ids = [f"{pdf_name}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": pdf_name, "chunk_index": i} for i in range(len(chunks))]

    # 5. Add to Database
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatas
    )
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "chroma_db")
    client = chromadb.PersistentClient(path=db_path)

    print(f"--- SUCCESS: {len(chunks)} chunks stored in ChromaDB ---")
    client = chromadb.PersistentClient(path="./chroma_db")