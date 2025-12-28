import ollama
from typing import List


# Make sure to run 'ollama pull mxbai-embed-large' in your terminal first
EMBEDDING_MODEL = "mxbai-embed-large"

def embed_chunks(chunks: List[str]) -> List[List[float]]:
    embeddings = []
    print(f"Generating embeddings for {len(chunks)} chunks using {EMBEDDING_MODEL}...")
    
    for chunk in chunks:
        # Call local Ollama instance
        response = ollama.embed(model=EMBEDDING_MODEL, input=chunk)
        
        # Extract the vector from the response
        embedding_vector = response['embeddings'][0]
        embeddings.append(embedding_vector)
        
    return embeddings