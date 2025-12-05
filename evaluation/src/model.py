import openai
import time
from openai import OpenAI
import tiktoken
import re
from random import choice


class Model:
    def __init__(self, model_str, temperature):
        gpt_keys = ["sk-gptkeys"]
        dps_keys = ["sk-dpskeys"]
        default_keys = ['sk-defaultkeys']
        # self.keys = self.get_api_keys()
        self.model_str = model_str
        if "gpt" in model_str:
            self.url = "https://api.openai.com/v1"
            self.keys = gpt_keys
        elif "deepseek" in model_str:
            self.url = "https://api.deepseek.com"
            self.keys = dps_keys
        else:
            self.url = "https://localhost:1234/v1"
            self.keys = default_keys
        self.temperature = temperature

    @staticmethod
    def get_api_keys():
        with open("api_key.txt", encoding='utf-8') as file:
            api_keys = file.readlines()
            api_keys = [key.strip() for key in api_keys]  # remove the '\n' at the end of each line
        return api_keys

    def send_request(self, message_history):
        tmp_key = choice(self.keys)
        client = OpenAI(
            base_url=self.url,
            api_key=tmp_key  # os.environ.get("OPENAI_API_KEY")
        )
        prompt_string = ''.join([m['content'] for m in message_history if m['role'] != 'system'])
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        num_tokens = len(encoding.encode(prompt_string))
        print(f"Prompt token count: {num_tokens}")

        max_retries = len(self.keys)
        retry_count = 0
        while retry_count < max_retries:
            try:
                response = client.chat.completions.create(
                    model=self.model_str,
                    messages=message_history,
                    temperature=self.temperature
                )
                break
            except openai.RateLimitError as e:
                self.handle_gpt_rate_limit(tmp_key, e)
                retry_count += 1
            except Exception as e:
                print(e)
                retry_count += 1
            print(f"Retry count: {retry_count}")
        else:
            raise Exception("All keys are used up or an unknown exception exists, please check the output.")
        # print(response)
        if self.model_str == "deepseek-r1-250120":
            return response.choices[0].message.content, response.choices[0].message.reasoning_content
        elif self.model_str == "qwq":
            content = response.choices[0].message.content
            pattern = r'<think>(.*?)</think>(.*)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                cot = match.group(1).strip()  # Content within <think>...</think>
                output = match.group(2).strip()  # Content after </think>
                return output, cot
            else:
                raise Exception("No thinking process found.")
        else:
            return response.choices[0].message.content

    def run_prompts(self, prompts):
        message_history = [{"role": "system", "content": "You are a helpful assistant."}]
        reasoning_history = []
        for prompt in prompts:
            message_history.append({"role": "user", "content": prompt})
            output = self.send_request(message_history)
            if isinstance(output, tuple):
                message_history.append({"role": "assistant", "content": output[0]})
                reasoning_history.append(output[1])
            else:
                message_history.append({"role": "assistant", "content": output})
        return message_history, reasoning_history

    def handle_gpt_rate_limit(self, tmp_key, e):
        if 'requests per day' in str(e):
            self.keys.remove(tmp_key)
            tmp_key = choice(self.keys)
            print(f"Daily rate limit error with {openai.api_key}. Change to {tmp_key}.")
            openai.api_key = tmp_key
        elif 'requests per min' in str(e) or 'tokens per min' in str(e):
            print(f"Minute rate limit error with {openai.api_key}, wait 60s.")
            time.sleep(60)
        elif 'exceeded your current quota' in str(e):
            self.keys.remove(tmp_key)
            tmp_key = choice(self.keys)
            print(f"Quota exceeded with {openai.api_key}. Change to {tmp_key}.")
            openai.api_key = tmp_key
        else:
            print("Unknown rate limit error.")
            raise e
