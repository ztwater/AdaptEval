from langchain.callbacks import get_openai_callback

        with get_openai_callback() as cb:
            response = qa({"question": prompt, "chat_history": chat_history})

            print(f"Prompt Tokens: {cb.prompt_tokens}")
            print(f"Completion Tokens: {cb.completion_tokens}")
            print(f"Total Cost (USD): ${cb.total_cost}")
