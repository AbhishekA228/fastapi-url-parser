from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from text_processing import extract_text_from_url, chunk_text
from embeddings import generate_embeddings
from vector_db import add_embeddings_to_db, query_vector_db

app = FastAPI()

# Request model for URL parsing
class URLRequest(BaseModel):
    url: str

# Request model for querying
class QueryRequest(BaseModel):
    query: str

# Endpoint to parse the URL, chunk the text, generate embeddings, and store them
@app.post("/url-parser")
async def parse_url(request: URLRequest):
    url = request.url
    try:
        # Extract text from URL and chunk it
        body_text = extract_text_from_url(url)
        text_chunks = chunk_text(body_text)

        # Generate embeddings for the text chunks
        embeddings = generate_embeddings(text_chunks)

        # Store the embeddings in the vector database
        add_embeddings_to_db(url, text_chunks, embeddings)

        return {"status": "success", "message": "Embeddings stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing URL: {str(e)}")

# Endpoint to query the vector database
@app.post("/query")
async def query_db(request: QueryRequest):
    query = request.query
    try:
        # Query the vector database and retrieve the most relevant result
        result = query_vector_db(query)
        return {"status": "success", "relevant_text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing query: {str(e)}")
