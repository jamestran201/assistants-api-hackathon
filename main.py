import time
from openai import OpenAI

# TODO: Try with PG essay. Quoting works?? How come it doesn't work for other doc??

class Assistant:
    def __init__(self):
        self.client = OpenAI()
        self.assistant = self.client.beta.assistants.retrieve("asst_kjDDJcRZ9wkL4q0hnmhHE64z")
        self.thread = self.client.beta.threads.create()

    def ask(self, query):
        self.client.beta.threads.messages.create(self.thread.id, role="user", content=query)
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            instructions="You are a golf referee. Please answer any questions about golf rules using the USGA rulebook."
        )

        # Wait for the run to complete
        while run.status in ['queued', 'in_progress', 'cancelling']:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run.id)
            print(run.status)

        if run.status == 'completed':
            messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
            return messages
        # annotations = message_content.annotations
        # citations = []
        # for index, annotation in enumerate(annotations):
        #     message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        #     if file_citation := getattr(annotation, "file_citation", None):
        #         cited_file = self.client.files.retrieve(file_citation.file_id)
        #         citations.append(f"[{index}] {cited_file.filename}")

        # print(message_content.value)
        # print("\n".join(citations))
