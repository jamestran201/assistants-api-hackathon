from openai import OpenAI

client = OpenAI(default_headers={"OpenAI-Beta": "assistants=v1"})
vector_store = client.beta.vector_stores.create(name="USGA Rules")
 
with open("usga_rules.pdf", "rb") as f:
    file = client.beta.vector_stores.files.upload_and_poll(vector_store_id=vector_store.id, file=f)
 
print(file.status)