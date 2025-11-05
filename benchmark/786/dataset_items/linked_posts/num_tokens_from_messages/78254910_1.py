def get_number_of_tokens(string: str) -> int:
    encoding = tiktoken.encoding_for_model("text-embedding-3-large")
    num_tokens = len(encoding.encode(string))
    return num_tokens

total_token = get_number_of_tokens('test text')
print total_token
