import chromadb

# Initialize ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection("url_text_embeddings")

# Function to add embeddings and associated text chunks to the database
def add_embeddings_to_db(url, text_chunks, embeddings):
    for idx, embedding in enumerate(embeddings):
        collection.add([f"{url}_chunk_{idx}"], [embedding], documents=[text_chunks[idx]])

# Function to query the vector database using a query embedding
def query_vector_db(query_text):
    from embeddings import generate_embeddings
    query_embedding = generate_embeddings([query_text])[0]

    # Query the vector database and retrieve the most relevant document
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    most_relevant = results["documents"][0]
    return most_relevant
