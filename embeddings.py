import torch
from transformers import AutoTokenizer, AutoModel

# Load the tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Function to generate embeddings for a list of text chunks
def generate_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        inputs = tokenizer(chunk, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            embed = model(**inputs).last_hidden_state.mean(dim=1).squeeze()
            embeddings.append(embed.numpy())
    return embeddings
