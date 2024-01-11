"""
用chatgpt调用本地函数示例
"""
from openai import OpenAI
import json

client = OpenAI()


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
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


def run_conversation():
    # Step 1: 想模型发起对话，并定义函数信息放入 tools 数组
    messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,  # 定义的tools中包含函数，模型可以发起调用
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # Step 2: 检查模型是否愿意调用函数
    if tool_calls:
        # Step 3: 如果愿意，调用之
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        messages.append(response_message)  # extend conversation with assistant's reply

        # Step 4: 将每次函数调用和函数响应的信息发送给模型
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,  # 调用的tool id
                    "role": "tool",
                    "name": function_name,  # 函数名称
                    "content": function_response,  # 函数的调用结果作为请求的内容
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response
    else:
        return "chatgpt doesn't want to call tools"


print(run_conversation().model_dump_json())
# {"id":"chatcmpl-8foCYC8XuoQxUVUbgjgbF3yfdbBGa","choices":[{"finish_reason":"stop","index":0,"logprobs":null,"message":{"content":"The current weather in San Francisco is 72°C, in Tokyo it is 10°C, and in Paris it is 22°C.","role":"assistant","function_call":null,"tool_calls":null}}],"created":1704975114,"model":"gpt-3.5-turbo-1106","object":"chat.completion","system_fingerprint":"fp_cbe4fa03fe","usage":{"completion_tokens":28,"prompt_tokens":169,"total_tokens":197}}
