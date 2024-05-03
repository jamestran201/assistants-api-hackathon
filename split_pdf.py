from llmsherpa.readers import LayoutPDFReader

# This requires another service locally:
# docker run -p 5010:5001 ghcr.io/nlmatics/nlm-ingestor:latest
pdf_reader = LayoutPDFReader("http://127.0.0.1:5010/api/parseDocument?renderFormat=all")
doc = pdf_reader.read_pdf("usga_rules.pdf")

chunk_written = False
chunk_num = 0
parts = []
for i, chunk in enumerate(doc.chunks()):
    parts.append(f"{chunk.to_context_text()}\n")

    # This will create at most 20 files,
    # which is the max number of files that can be given to an Assistant
    if (i + 1) % 80 == 0:
        with open(f"pages/chunk_{chunk_num}.txt", "w") as f:
            f.writelines(parts)

        chunk_num += 1
        chunk_written = True
        parts = []
    else:
        chunk_written = False

if not chunk_written:
    with open(f"pages/chunk_{chunk_num}.txt", "w") as f:
        f.writelines(parts)