import pandas as pd
import networkx as nx
import pickle

papers = pd.read_csv("data/papers.csv")

id_list = list(papers['id'].astype(str))
title_list = list(papers['title'])
author_list = list(papers['authors'])

with open('data/graph.pkl', 'rb') as file:
    graph = pickle.load(file)
graph = nx.Graph(graph)

with open('data/partition_list.pkl', 'rb') as file:
    partition_list = pickle.load(file)

with open('data/partition_mapping.pkl', 'rb') as file:
    partition_mapping = pickle.load(file)
