from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import List, Union
from utils.type import Sentence
from copy import deepcopy

from utils.getter import papers, id_list, title_list, author_list, graph, partition_list, partition_mapping
from utils.db import chromaClient

# FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get chroma collection
collection = chromaClient.get_collection("NIPs-paper")

# API
@app.get("/papers", response_model=List[dict])
async def get_papers():
    paper_data = []
    for idx, paper_id in enumerate(papers["id"]):
        paper_info = {
            "id": paper_id,
            "year": papers.loc[idx, "year"].iloc[0],
            "title": papers.loc[idx, "title"].iloc[0],
            "event_type": papers.loc[idx, "event_type"].iloc[0],
            "authors": papers.loc[idx, "authors"].iloc[0]
        }
        paper_data.append(paper_info)
    return paper_data

@app.post("/recommends")
async def get_recommendations(input: Sentence):

    global collection

    result = collection.query(
        query_texts=[input.sentence],
        n_results=1
    )
    
    id = int(result["ids"][0][0])
    distance = result["distances"][0][0]

    if distance < 0.1:
        return {
            "status": 404
        }
    
    intList = [int(i) for i in id_list]

    paper_index = intList.index(id)

    partition_index = partition_mapping[id]
    
    neighbor_list = deepcopy(partition_list[partition_index])
    neighbor_list.remove(id)
    
    weight_list = [graph.get_edge_data(id, i)['weight'] if graph.has_edge(id, i) else 0 for i in neighbor_list]
    
    top_indices = sorted(range(len(weight_list)), key=lambda k: weight_list[k], reverse=True)[:min(5, len(weight_list))]
    
    top_recommendations = []
    for index in top_indices:
        neighbor_id = neighbor_list[index]
        neighbor_index = intList.index(neighbor_id)
        paper = {
            "title": title_list[neighbor_index],
            "author": author_list[neighbor_index]
        }
        top_recommendations.append(paper)
    return {
        "status": 200,
        "paper": {
            "title": title_list[paper_index],
            "author": author_list[paper_index]
        },
        "recommend": top_recommendations
    }

        