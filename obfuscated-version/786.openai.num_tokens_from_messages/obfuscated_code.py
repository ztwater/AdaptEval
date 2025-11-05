import tiktoken

def num_tokens_from_messages(var_0, var_1="gpt-3.5-turbo-0301"):
    """Returns the number of tokens used by a list of messages."""
    try:
        var_2 = tiktoken.encoding_for_model(var_1)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        var_2 = tiktoken.get_encoding("cl100k_base")
    if var_1 == "gpt-3.5-turbo":
        print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
        return num_tokens_from_messages(var_0, var_1="gpt-3.5-turbo-0301")
    elif var_1 == "gpt-4":
        print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
        return num_tokens_from_messages(var_0, var_1="gpt-4-0314")
    elif var_1 == "gpt-3.5-turbo-0301":
        var_3 = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        var_4 = -1  # if there's a name, the role is omitted
    elif var_1 == "gpt-4-0314":
        var_3 = 3
        var_4 = 1
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
    var_5 = 0

    if type(var_0) == "list":
        for message in var_0:
            var_5 += var_3
            for key, value in message.items():
                var_5 += len(var_2.encode(value))
                if key == "name":
                    var_5 += var_4
        var_5 += 3  # every reply is primed with <|start|>assistant<|message|>
    elif type(var_0) == "str":
        var_5 += len(var_2.encode(var_0))
    return var_5
