
# FastAPI URL Parser and Query System

## Problem Statement
We are tasked with building a Python-based server using Uvicorn and FastAPI to develop two endpoints that interact with external URLs, process their content, and provide a queryable system based on vector embeddings.

### Main Functionalities
1. **URL Parsing and Embedding Generation**:
   - Accept a URL, extract the body text, split it into manageable chunks, and convert each chunk into vector embeddings using a Hugging Face model.
   - Store these embeddings in a vector database (e.g., ChromaDB).

2. **Query System**:
   - Accept a query string and search through the vector database for the most relevant text chunk.
   - Return the relevant text chunk or generate a detailed response using a Hugging Face model.

## Requirements
- **Server Framework**: FastAPI
- **Embeddings Model**: Hugging Face transformers
- **Text Generation Model**: Optional, for enhanced query responses
- **Vector Database**: ChromaDB for storing embeddings and querying
- **Error Handling**: For invalid URLs, missing data, etc.

## Solution Overview
We have built a FastAPI-based server with two endpoints:
1. **/url-parser**: Takes a URL, extracts and chunks the body text, generates vector embeddings for the chunks, and stores them in a vector database.
2. **/query**: Allows querying the stored embeddings and returns the most relevant text chunk based on the query.

The solution involves:
- Extracting text using BeautifulSoup from external URLs.
- Chunking large texts into smaller pieces.
- Generating vector embeddings for each chunk using a Hugging Face model.
- Storing embeddings in a vector database (ChromaDB).
- Querying the database to return the most relevant text chunk for a given query.

## Directory Structure
```bash
fastapi-url-parser/
├── app.py                # Main FastAPI app
├── embeddings.py         # Embedding generation functions
├── text_processing.py    # Text extraction and chunking
├── vector_db.py          # Vector database interaction
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

## Step-by-Step Instructions to Run the Solution

### 1. Clone the Repository and Set Up the Environment
```bash
git clone https://github.com/AbhishekA228/fastapi-url-parser.git
cd fastapi-url-parser
```

### 2. Install Dependencies
Ensure that you have Python 3.7 or later installed. Install the required dependencies using:
```bash
pip install -r requirements.txt
```
This will install FastAPI, Uvicorn, Hugging Face transformers, ChromaDB, BeautifulSoup, and other required libraries.

### 3. Run the FastAPI Application
To run the FastAPI app using Uvicorn:
```bash
uvicorn app:app --reload
```
The server will start at http://127.0.0.1:8000. The `--reload` flag ensures the server auto-reloads if any code changes are made.

### 4. Test the /url-parser Endpoint
To parse and store embeddings from a webpage, use the `/url-parser` endpoint. For example, you can use the following curl command:
```bash
curl -X POST "http://127.0.0.1:8000/url-parser" -H "Content-Type: application/json" -d "{"url": "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"}"
```

### 5. Test the /query Endpoint
After storing the embeddings, you can query them using the `/query` endpoint. For example:
```bash
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d "{"query": "Cr7 biography"}"
```

### 6. Using Postman or Any HTTP Client
You can also use tools like Postman to make POST requests to the endpoints:
- **POST to /url-parser**: Send a JSON body with the URL to extract and store text.
- **POST to /query**: Send a query string to retrieve the most relevant text chunk.

### 7. Shut Down the Server
To stop the server, press `CTRL+C` in the terminal where Uvicorn is running.

## Example of Using the Solution

### Parsing a URL:
```bash
curl -X POST "http://127.0.0.1:8000/url-parser" -H "Content-Type: application/json" -d "{"url": "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"}"
```
**Response**:
```json
{
  "status": "success",
  "message": "Embeddings stored successfully."
}
```

### Querying for Relevant Text:
```bash
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d "{"query": "Cr7 biography"}"
```
**Response**:
```json
{
  "status": "success",
  "relevant_text": ["Cristiano Ronaldo dos Santos Aveiro GOIH ComM (born 5 February 1985) is a Portuguese professional footballer..."]
}
```

## Key Concepts in the Code
1. **Text Extraction**: We use BeautifulSoup to parse HTML content and extract text from the body of the web page.
2. **Text Chunking**: The text is split into smaller chunks based on character limits to ensure each chunk is manageable for generating embeddings.
3. **Embedding Generation**: The Hugging Face model `sentence-transformers/all-MiniLM-L6-v2` is used to convert text chunks into vector embeddings.
4. **Vector Database**: We use ChromaDB to store and query the vector embeddings for efficient similarity search.

## Enhancements and Further Testing
- **Different Embedding Models**: You can experiment with other models from Hugging Face for better results.
- **Error Handling**: You can improve error handling for invalid URLs or queries.
- **Text Generation for Queries**: To enhance query responses, you can integrate Hugging Face models for generating full responses (e.g., GPT-2, T5).
- **Improving Query Responses**: You can further optimize how the query results are formatted and presented.
