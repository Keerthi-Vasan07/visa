import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"

from pdfreader import read_pdf
from chunker import chunk_pages   
from embedder import embed_chunks
from vector import store_in_chroma
from typing import List

pdf_path = "oops.pdf"
def run():
    pages = read_pdf(pdf_path)

    chunks = chunk_pages(pages, chunk_size=1000, chunk_overlap=150  )

    embedded_chunks = embed_chunks(chunks)
    #print("first embedded chunk:", embedded_chunks[0])
    
    store_in_chroma(chunks, embedded_chunks)

if __name__ == "__main__":
    run()