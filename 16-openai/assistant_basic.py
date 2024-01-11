import json
import os
import time

from openai import OpenAI

# 获取key
key = os.getenv('OPENAI_API_KEY')
if key is None:
    print("Please set OPENAI_API_KEY environment variable first")
    exit(-1)

# 创建 client
client = OpenAI()

# 创建assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# 创建线程
thread = client.beta.threads.create()
# 向线程添加消息
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
# 查看线程中的消息
thread_messages = client.beta.threads.messages.list(thread.id)
print("thread_message:", thread_messages.data)
# 运行助手
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)
# 检查运行状态，需要定期检测是否时 completed 状态
while True:
    run = client.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id
    )
    print("run status:", run.status)
    if run.status == 'completed':
        break
    time.sleep(1)
# 输出响应
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)
print("messages:", messages.model_dump_json(indent=4))