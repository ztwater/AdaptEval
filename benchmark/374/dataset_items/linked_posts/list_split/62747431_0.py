def chunk_array(array : List, n: int) -> List[List]:
    chunk_size = len(array) // n 
    chunks = []
    i = 0
    while i < len(array):
        # if less than chunk_size left add the remainder to last element
        if len(array) - (i + chunk_size + 1) < 0:
            chunks[-1].append(*array[i:i + chunk_size])
            break
        else:
            chunks.append(array[i:i + chunk_size])
            i += chunk_size
    return chunks
