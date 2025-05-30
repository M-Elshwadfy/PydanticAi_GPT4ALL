from gpt4all import GPT4All

model = GPT4All("mistral-7b-openorca.gguf2.Q4_0.gguf") 
with model.chat_session():
    print(model.generate("Tell me a joke about Ai", max_tokens=1024))