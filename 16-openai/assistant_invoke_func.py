"""
使用助手调用函数
"""
import json
import os
import time

from openai import OpenAI


# 一个硬编码用于测试的返回天气的示例函数
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})


# 一个用于获取城市昵称的测试函数
def get_nickname(location, **kwargs):
    if "san francisco" in location.lower():
        return "CA"
    return "unknown"


# 获取key
key = os.getenv('OPENAI_API_KEY')
if key is None:
    print("Please set OPENAI_API_KEY environment variable first")
    exit(-1)

client = OpenAI()

# 创建助手并传递函数描述信息
assistant = client.beta.assistants.create(
    instructions="You are a weather bot. Use the provided functions to answer questions.",
    model="gpt-4-1106-preview",
    tools=[{
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the weather in location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city and state e.g. San Francisco, CA"},
                    "unit": {"type": "string", "enum": ["c", "f"]}
                },
                "required": ["location"]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "get_nickname",
            "description": "Get the nickname of a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city, e.g. San Francisco"},
                },
                "required": ["location"]
            }
        }
    }]
)

# TODO 这里的消息为什么只会有一个？
# 创建thread
thread = client.beta.threads.create()
# 创建message到threads
weather_msg = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What's the weather like in San Francisco, Tokyo, and Paris?"
)
nickname_msg = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What's the nickname of San Francisco, Tokyo, and Paris?"
)

# 查询线程中的消息
thread_messages = client.beta.threads.messages.list(thread.id)
print("thread_message:", thread_messages.data)

# 运行助手
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    tools=[{"type": "code_interpreter"}]
)

# 检查运行状态，启动时进入 pendding 状态, 完成后为 requires_action 状态
while True:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    print("run status:", run.status)
    if run.status == 'requires_action':
        break
    time.sleep(1)

# 组装函数调用的结果，然提交输出结果给模型
tool_outputs = []
available_functions = {
    "get_current_weather": get_current_weather,
    "get_nickname": get_nickname,
}
if run.required_action.submit_tool_outputs.tool_calls:
    for call in run.required_action.submit_tool_outputs.tool_calls:
        print("function name:", call.function.name)
        function_to_call = available_functions[call.function.name]
        function_args = json.loads(call.function.arguments)
        function_response = function_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )
        tool_outputs.append({
            "tool_call_id": call.id,
            "output": function_response,
        })

    # 状态变为 requires_action 后，现在可以提交输出，此时 run 变为 queued 状态
    run = client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread.id,
        run_id=run.id,
        tool_outputs=tool_outputs
    )

    # 检查运行状态，run 执行时进入 queued 状态, 完成后为 completed 状态
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
    print("messages:", messages.model_dump_json())
else:
    print("No tools to call")
