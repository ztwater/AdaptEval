def chunkify(lst, size):
    """Split a list into equally-sized chunks."""
    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i+size])
    return chunks
