from openai import OpenAI

client = OpenAI(default_headers={"OpenAI-Beta": "assistants=v1"})
vector_store = client.beta.vector_stores.create(name="USGA Rules")

with open("usga_rules.pdf", "rb") as f:
    file = client.beta.vector_stores.files.upload_and_poll(vector_store_id=vector_store.id, file=f)

assistant = client.beta.assistants.create(
  name="USGA Rules Assistant",
  instructions="You are an expert golf referee. Use what is provided in the USGA rules of golf to answer questions about golf rules.",
  model="gpt-3.5-turbo",
  tools=[{"type": "file_search"}],
)
client.beta.assistants.update(
  assistant_id=assistant.id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)