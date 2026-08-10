def chunk_text(text, chunk_size=800, overlap=100):
    """
    Membagi teks menjadi beberapa chunk dengan overlap.
    """

    if not text:
        return []

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks