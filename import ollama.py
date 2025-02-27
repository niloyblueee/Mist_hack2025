import ollama
print(ollama.chat(model='llama2', messages=[{'role': 'user', 'content': 'Hello!'}]))