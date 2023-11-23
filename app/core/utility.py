def divide_chunks(l:list, n:int) -> list[list]: 
    """Divide a list into chunks.
    
    Args:
        l (list): the list to divide
        n (int): the size of chunks to break data into
    Return:
        list[list]: a list of lists with max size of n
    """
    chunks = []
    
    # Create chunked list of lists
    for i in range(0, len(l), n):  
        chunks.append( l[i:i + n] )
    
    # Return chunks
    return chunks