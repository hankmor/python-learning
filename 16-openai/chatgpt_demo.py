import os

from openai import OpenAI

# 获取key
key = os.getenv('OPENAI_API_KEY')
if key is None:
    print("Please set OPENAI_API_KEY environment variable first")
    exit(-1)

# 创建 client
client = OpenAI()

# 创建 stream
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

# 获取数据
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
