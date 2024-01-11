"""
使用assistant api处理文件数据可视化
"""
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

# 上传一个csv文件
file = client.files.create(
    file=open("chat_basic.py", "rb"),
    purpose='assistants'  # 必须指定，表示上传文件给助手
)
# 创建assistant, 每个助手最多可以附加 20 个文件，每个文件最多 512 MB, 组织所有文件不超过 100 G.
assistant = client.beta.assistants.create(
    name="Data visualizer",
    description="You are great at creating beautiful data visualizations. You analyze data present in .csv files, understand trends, and come up with data visualizations relevant to those trends. You also share a brief text summary of the trends observed.",
    model="gpt-4-1106-preview",
    tools=[{"type": "code_interpreter"}],
    file_ids=[file.id]
)

# 创建线程, 带有初始消息
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "Create 3 data visualizations based on the trends in this file.",
            "file_ids": [file.id]
        }
    ]
)
# 查看线程中的消息
thread_messages = client.beta.threads.messages.list(thread.id)
print("thread_message:", thread_messages.data)
# 运行助手
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    # instructions="Please address the user as Jane Doe. The user has a premium account."
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
# 输出：{
#     "data": [
#         {
#             "id": "msg_RBdimu3u3cPGVq1QCMcN9N3l",
#             "assistant_id": "asst_RPa7XVfmFgFe0VoqPWSUeUVw",
#             "content": [
#                 {
#                     "text": {
#                         "annotations": [],
#                         "value": "The script seems to interact with the OpenAI API using the `openai` Python package, which likely means it is designed to communicate with an AI model such as GPT-3.5. The code initializes an OpenAI client, sends a series of messages as prompts to the chat completion endpoint, and prints out the response from the model.\n\nFrom the content provided, the data is related to the interaction with the AI model. However, this is not typical tabular data and it does not contain any inherent \"trends\" that we would analyze directly. Visualizations would typically be based on the analysis of structured data, such as numerical or categorical information over time or across categories.\n\nTo create visualizations, we would need to extract information such as the following:\n1. Frequencies of specific responses from the API\n2. Patterns in interaction, like common questions or answers\n3. Performance metrics, if any, like response times or accuracy rates\n\nIf the script includes a data collection mechanism over multiple interactions with the OpenAI API, we could visualize these aspects. Otherwise, the only \"trend\" present is the scripted conversation with predefined prompts and responses. We could simulate AI responses and visualize the simulated interactions, if that would meet your needs. However, if you are looking for a trend analysis based on historical data, this file does not seem to contain that information.\n\nPlease let me know how you'd like to proceed, or if there's specific information in the script that you believe we can visualize."
#                     },
#                     "type": "text"
#                 }
#             ],
#             "created_at": 1704968745,
#             "file_ids": [],
#             "metadata": {},
#             "object": "thread.message",
#             "role": "assistant",
#             "run_id": "run_HQJYD1GLqjUlkkMRjvNPo55i",
#             "thread_id": "thread_9G4aFFhcpzzs2ofMhxzoaZ0H"
#         },
#         {
#             "id": "msg_BemeeR8k6X5dNkrtweW36yVp",
#             "assistant_id": "asst_RPa7XVfmFgFe0VoqPWSUeUVw",
#             "content": [
#                 {
#                     "text": {
#                         "annotations": [],
#                         "value": "The file starts with what looks like the beginning of a Python script. It imports the `os` module and `OpenAI` from `openai`, and contains comments in Chinese that translate to \"get key\". It seems to be retrieving an OpenAI API key from the environment.\n\nConsidering that this is a Python script, it is not a data file that I can simply load and analyze. Instead, it appears to be code intended for execution.\n\nTo continue with the task of creating data visualizations based on \"trends\" in this file, we need to find the sections of the script that handle data. I will now proceed to read the entire file and look for parts of the code that indicate data processing or data generation, which could be used for visualization purposes. Let's read the entire file now."
#                     },
#                     "type": "text"
#                 }
#             ],
#             "created_at": 1704968726,
#             "file_ids": [],
#             "metadata": {},
#             "object": "thread.message",
#             "role": "assistant",
#             "run_id": "run_HQJYD1GLqjUlkkMRjvNPo55i",
#             "thread_id": "thread_9G4aFFhcpzzs2ofMhxzoaZ0H"
#         },
#         {
#             "id": "msg_gW62DTqOVKtYtJlwGcieHkcK",
#             "assistant_id": "asst_RPa7XVfmFgFe0VoqPWSUeUVw",
#             "content": [
#                 {
#                     "text": {
#                         "annotations": [],
#                         "value": "The file begins with what appears to be Python code (`import os\\n`). It seems likely that the file might be a Python script, rather than a data file.\n\nTo further investigate, let's read the first few lines of the file as a text file and inspect its contents more thoroughly. If it is indeed Python code or another kind of script, we'll see the structure of the script and decide how to proceed from there."
#                     },
#                     "type": "text"
#                 }
#             ],
#             "created_at": 1704968714,
#             "file_ids": [],
#             "metadata": {},
#             "object": "thread.message",
#             "role": "assistant",
#             "run_id": "run_HQJYD1GLqjUlkkMRjvNPo55i",
#             "thread_id": "thread_9G4aFFhcpzzs2ofMhxzoaZ0H"
#         },
#         {
#             "id": "msg_nUCFcHuJXSkaHMsevUiMaAfZ",
#             "assistant_id": "asst_RPa7XVfmFgFe0VoqPWSUeUVw",
#             "content": [
#                 {
#                     "text": {
#                         "annotations": [],
#                         "value": "It appears that the file could not be read directly as either a CSV or an Excel file. This could be due to several reasons, such as the file being in a different format or containing irregular formatting that does not conform to standard CSV or Excel structures.\n\nTo proceed, I'll attempt a few more strategies to accurately identify and read the file's contents:\n\n1. Inspect the first few bytes of the file for magic numbers that could indicate the file type.\n2. Open the file in text mode and read the first few lines to get a sense of its structure.\n\nLet's start with inspecting the first few bytes of the file."
#                     },
#                     "type": "text"
#                 }
#             ],
#             "created_at": 1704968703,
#             "file_ids": [],
#             "metadata": {},
#             "object": "thread.message",
#             "role": "assistant",
#             "run_id": "run_HQJYD1GLqjUlkkMRjvNPo55i",
#             "thread_id": "thread_9G4aFFhcpzzs2ofMhxzoaZ0H"
#         },
#         {
#             "id": "msg_6CLeOGBVDT17APrlpHPfHWSj",
#             "assistant_id": "asst_RPa7XVfmFgFe0VoqPWSUeUVw",
#             "content": [
#                 {
#                     "text": {
#                         "annotations": [],
#                         "value": "To start, I will examine the contents of the file to determine what kind of data it contains. This will help me identify potential trends and decide on appropriate types of visualizations. Let me first identify the file type and then load the data accordingly."
#                     },
#                     "type": "text"
#                 }
#             ],
#             "created_at": 1704968684,
#             "file_ids": [],
#             "metadata": {},
#             "object": "thread.message",
#             "role": "assistant",
#             "run_id": "run_HQJYD1GLqjUlkkMRjvNPo55i",
#             "thread_id": "thread_9G4aFFhcpzzs2ofMhxzoaZ0H"
#         },
#         {
#             "id": "msg_4Lp3GNSQNRhu5lvcuqWl7C0T",
#             "assistant_id": null,
#             "content": [
#                 {
#                     "text": {
#                         "annotations": [],
#                         "value": "Create 3 data visualizations based on the trends in this file."
#                     },
#                     "type": "text"
#                 }
#             ],
#             "created_at": 1704968682,
#             "file_ids": [
#                 "file-E7MMpZ2o0XfYwECP6urmII5Z"
#             ],
#             "metadata": {},
#             "object": "thread.message",
#             "role": "user",
#             "run_id": null,
#             "thread_id": "thread_9G4aFFhcpzzs2ofMhxzoaZ0H"
#         }
#     ],
#     "object": "list",
#     "first_id": "msg_RBdimu3u3cPGVq1QCMcN9N3l",
#     "last_id": "msg_4Lp3GNSQNRhu5lvcuqWl7C0T",
#     "has_more": false
# }
