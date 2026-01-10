import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"

from jsonreader import read_json
from chunker import chunk_pages   
from embedder import embed_chunks
from vector import store_in_chroma
from typing import List

json_path = "data.json"
def run():
    pages = read_json(json_path)

    chunks = chunk_pages(pages, chunk_size=1000, chunk_overlap=150)

    embedded_chunks = embed_chunks(chunks)
    
    store_in_chroma(chunks, embedded_chunks, document_name=json_path)

if __name__ == "__main__":
    run()