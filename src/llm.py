import json
import time
from tqdm import tqdm
# import openai

# Modify your own openai config
# client.api_base = os.environ["OPENAI_API_BASE"]
# client.api_version = os.environ["OPENAI_API_VERSION"]
# client.api_key = os.environ["OPENAI_API_KEY"]

from openai_api import client

# def connect_gpt4(message, prompt):
#     response = client.chat.completions.create(
#                     model="gpt-4o", 
#                     messages = [{"role":"system","content":f"{message}"}, #"You are a helpful assisant. Help the user to complete SQL and no explaination is needed."
#                                 {"role":"user", "content":f"{prompt}"}],
#                     temperature=0,
#                     max_tokens=800, #800
#                     top_p=1,
#                     frequency_penalty=0,
#                     presence_penalty=0,
#                     stop = None)
#     return response['choices'][0]['message']['content']


def collect_response(prompt, max_tokens = 800, stop = None):
    while 1:
            flag = 0
            try:
                response = client.chat.completions.create(
                    model="gpt-4o", 
                    messages = [{"role":"system","content":"You are an AI assistant that helps people find information."}, #"You are a helpful assisant. Help the user to complete SQL and no explaination is needed."
                                {"role":"user", "content":f"{prompt}"}],
                    temperature=0,
                    max_tokens=max_tokens, #800
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop = stop)
                response = json.loads(response.model_dump_json())
                response = response['choices'][0]['message']['content']
                flag = 1
                
            except Exception as e:
                print(e)
                time.sleep(1)
            if flag == 1:
                break
    return response

