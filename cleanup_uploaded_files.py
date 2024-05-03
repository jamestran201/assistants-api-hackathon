
from openai import OpenAI

client = OpenAI()
files = client.files.list()
for f in files:
    client.files.delete(f.id)