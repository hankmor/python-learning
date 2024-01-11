import os

from openai import OpenAI

# 获取key
key = os.getenv('OPENAI_API_KEY')
if key is None:
    print("Please set OPENAI_API_KEY environment variable first")
    exit(-1)

# 创建 client
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response.model_dump_json(indent=4))

# 输出：
# {
#     "id": "chatcmpl-8fShksjnmHHdFTsI8y2j2y012rlbC",
#     "choices": [
#         {
#             "finish_reason": "stop",
#             "index": 0,
#             "logprobs": null,
#             "message": {
#                 "content": "The 2020 World Series was played in Arlington, Texas. The games were held at the Globe Life Field, which is the home stadium for the Texas Rangers.",
#                 "role": "assistant",
#                 "function_call": null,
#                 "tool_calls": null
#             }
#         }
#     ],
#     "created": 1704892480,
#     "model": "gpt-3.5-turbo-0613",
#     "object": "chat.completion",
#     "system_fingerprint": null,
#     "usage": {
#         "completion_tokens": 33,
#         "prompt_tokens": 53,
#         "total_tokens": 86
#     }
# }
