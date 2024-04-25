# Recommendation System API for NIPs Dataset

## Description
* Apply Louvain algorithm for community detection
* Use chromadb to construct a vector database for enhanced querying within the API

## Tech Stack
* Louvain Algorithm: An algorithm for detecting the communities in a large network. More detail [here](https://en.wikipedia.org/wiki/Louvain_method)
* NetworkX
* FastAPI
* ChromaDB

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

### Start Chroma database server
Create a tab in the terminal and run this command
```
chroma run --path ./database --port 8080
```
The Chroma database server will run on ...

### Start FastAPI server
Create another tab in the terminal and run this command
```
uvicorn main:app --reload
```
The FastAPI server will run on ...

After doing these above steps, you can use the APIs. Use some tools (like Postman) for testing.

## APIs

## Future Plan
* Add UI for this project
* Update the embedding funtion of Chroma DB to get better performance

Chill coding!!!