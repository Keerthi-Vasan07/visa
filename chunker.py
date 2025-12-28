from typing import List

def chunk_pages(pages: List[str], chunk_size: int = 1000, chunk_overlap: int = 150) -> List[str]:
    chunks : List[str] = []

    full_text = " ".join(pages)
    text_length = len(full_text)

    if text_length == 0:
        return chunks
    start = 0
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = full_text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == text_length:
            break

        start += chunk_size - chunk_overlap
        print("start:", start)
    return chunks