'''
是否开启流式输出
'''
import ollama

client = ollama.Client(host='http://127.0.0.1:11434')

def ollama_chat(query):
    result = client.chat(
        model='qwen2.5:7b',
        messages=[
            {'role':'user','content':query}
        ],
        stream=True,        # 开启流式输出
    )

    for chunk in result:
        if not chunk.message.content:
            print(chunk.message.thinking, end='')
        else:
            print(chunk.message.content, end='')

ollama_chat('你能干嘛')
