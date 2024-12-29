from langchain_ollama.embeddings import OllamaEmbeddings

phraseList = ["What's in the box?"]

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

phraseEmbeds = embeddings.embed_documents(phraseList)

embedding_size = len(phraseEmbeds[0])
print(f"Size: {embedding_size}")

formatted_first_embeddings = ", ".join(map(str, phraseEmbeds[0][:10]))
print(f"Embeddings: {formatted_first_embeddings}...")