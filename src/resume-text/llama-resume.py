from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'How are you ?',
  },
])


print(response.message.content)