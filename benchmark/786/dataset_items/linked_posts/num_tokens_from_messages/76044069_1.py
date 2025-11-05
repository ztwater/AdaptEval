import openai

result = []

for chunk in openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ], # this is prompt_tokens ex) prompt_tokens=num_tokens_from_messages(messages)
    stream=True
):
    content = chunk["choices"][0].get("delta", {}).get("content")
    if content:
        result.append(content)


# Usage of completion_tokens
completion_tokens = num_tokens_from_messages("".join(result))
