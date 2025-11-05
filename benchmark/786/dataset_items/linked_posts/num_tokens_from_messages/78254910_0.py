response = openai_client.embeddings.create(model= "text-embedding-3-large", input="test text", encoding_format="float")
if response.data:
    embedding = response.data[0].embedding
    
    total_tokens = response.usage.total_tokens
    print ("Total tokens: ", total_tokens)
