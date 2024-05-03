from openai import OpenAI
import os

client = OpenAI()

files = os.listdir('./pages')
file_ids = []
for file in files:
  with open(f"pages/{file}", "rb") as f:
      file = client.files.create(file=f, purpose="assistants")
      file_ids.append(file.id)

assistant = client.beta.assistants.create(
  name="USGA Rules Assistant",
  instructions="You are an assistant that answers questions about Paul Graham.",
  model="gpt-4-turbo-preview",
  tools=[{"type": "retrieval"}],
  file_ids=file_ids
)
print(f"Assistant ID: {assistant.id}")