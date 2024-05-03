# assistants-api-hackathon

The goal was to build a RAG app using OpenAI Assistant for a hackathon. But I couldn't get the Assistant API
to return the quotes/citations for the generated responses. Things I've tried:

- Upload the whole PDF of 209 pages
- Converted the PDF to docx and uploaded the whole thing
- Splitted the PDF into 20 chunks
- Parsed and chunked the PDF using [LLM Sherpa](https://github.com/nlmatics/llmsherpa), then wrote the chunks to plaintext files

Setting up the project:
- `pip install -r requirements.txt`
- Download the USGA rules to the project dir and name it `usga_rules.pdf`
- Start a docker container for LLM Sherpa: `docker run -p 5010:5001 ghcr.io/nlmatics/nlm-ingestor:latest`
- Run `python split_pdf.py` to split the PDF into plaintext files
- Create an OpenAI API key and set it as env var
- Run `python create_assistant.py` to upload the text files and create an assistant
- Copy the assistant ID and paste it into the `main.py` file
- In a Python console, import `main` and use the `Assistant` class to query the model

Clean up:
- Run `cleanup_uploaded_files.py` to delete all uploaded files
- Manually delete the vector stores and assistants through the OpenAI UI