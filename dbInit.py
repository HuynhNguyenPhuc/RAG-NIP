from utils.getter import getPapers
import chromadb

client = chromadb.PersistentClient(path="./database")

papers = getPapers()
id_list = list(papers['id'].astype(str))
title_list = list(papers['title'])

try:
    client.delete_collection("NIPs-paper")
except ValueError:
    pass
finally:
    collection = client.get_or_create_collection("NIPs-paper")

collection.add(
    documents=title_list[:4000],
    ids=id_list[:4000]
)

collection.add(
    documents=title_list[4000:],
    ids=id_list[4000:]
)