import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
import ollama

def process_query_user(user_query: str):
    # 1. Connect to your local ChromaDB
    client = chromadb.PersistentClient(path="./chroma_db")

    # 2. Re-initialize the same embedding function used during storage
    # This ensures the user's query is converted into the same 1024-dimension space
    ollama_ef = OllamaEmbeddingFunction(
        url="http://localhost:11434/api/embeddings",
        model_name="mxbai-embed-large"
    )

    # 3. Access your collection
    collection = client.get_collection(
        name="pdf_collection", 
        embedding_function=ollama_ef
    )

    # 4. RETRIEVAL: Search for relevant chunks
    # Chroma embeds the query_texts automatically using the ollama_ef
    results = collection.query(
        query_texts=[user_query],
        n_results=3  # Retrieve the top 3 matching chunks
    )

    # Combine the retrieved text chunks into a single context string
    retrieved_docs = results['documents'][0]
    context = "\n\n".join(retrieved_docs)

    print(f"--- Context retrieved from {len(retrieved_docs)} chunks ---")

    # 5. GENERATION: Send query + context to the LLM
    # We use llama3.2 (or your preferred local model) to generate the answer
    prompt = f"""
    You are a helpful assistant. Use the provided context to answer the user's question.
    If the answer is not in the context, say you don't know.
    
    CONTEXT:
    {context}
    
    USER QUESTION: 
    {user_query}
    
    ANSWER:
    """

    response = ollama.generate(
        model="llama3.2", 
        prompt=prompt
    )

    return response['response']

if __name__ == "__main__":
    query = input("Enter your question: ")
    answer = process_query_user(query)
    print("\n--- LLM RESPONSE ---")
    print(answer)