# Recommendation System API for NIPs Dataset

## Description
* Apply Louvain algorithm for community detection
* Use ChromaDB to construct a vector database for enhanced querying within the API

## Tech Stack
* **Louvain Algorithm**: An algorithm for detecting the communities in a large network. More detail [here](https://en.wikipedia.org/wiki/Louvain_method)
* **NetworkX**: A libary for working with graph. Read the documentation [here](https://networkx.org/documentation/stable/tutorial.html)
* **FastAPI**:  A modern, fast, web framework for building APIs with Python. Read the documentation [here](https://fastapi.tiangolo.com/tutorial/)
* **ChromaDB**: A vector database, make it easy to apply LLMs in vector search. Read the documentation [here](https://docs.trychroma.com/)

## How to use
To use this API, you can follow some steps below

### Clone this repository
Go into the location you want to place this repository, then open the terminal and run this command:
```
git clone https://github.com/HuynhNguyenPhuc/SimpleRecSys.git
cd SimpleRecSys
```

### Install the necessary modules
Run this command
```
pip install -r requirement.txt
```

### Initialize the database (If needed)
I have initialized the database. You can change the dbInit.py file if needed and run it again.

### Start Chroma database server
Create a tab in the terminal and run this command
```
chroma run --path ./database/chroma --port 8080
```
The Chroma database server will run on *http://localhost:8080*

### Start FastAPI server
For development, run this command
```
uvicorn main:app --reload
```
The FastAPI server will run on *http://127.0.0.1:8000*

For production, run this command
```
uvicorn main:app --host <IP-address> --port <port-number>
```
After doing these above steps, you can use the APIs. Use some tools (like Postman) for testing.

## APIs
* GET /papers: Get information of all papers in the dataset
* POST /recommends, body: {"Sentence": str}: Get 5 recommended papers of the input paper.

## Future Plan
* Add UI for this project
* Update the embedding funtion of Chroma DB to get better performance

<h3 style="text-align:center; font-size:30px">Chill coding!!!</h3>
