from ollama import Client

client=Client()
chat_history=[]

print("chat with gemma else enter quit")

while True:
    prompt = input("\nyou: ")
    if prompt.lower() == "quit":
        break
    chat_history.append({"role": "user", "content": prompt})

    response=client.chat(
        model='tinyllama',
       messages=chat_history
    )

    reply = response['message']['content']
    print("\ntinyllama:", reply)
    chat_history.append({"role":"assistant", "content":reply})

    


