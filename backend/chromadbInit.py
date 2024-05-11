from utils.getter import id_list, title_list
import chromadb

client = chromadb.PersistentClient(path="./database/chroma")

try:
    client.delete_collection("NIPs-paper")
except ValueError:
    pass
finally:
    collection = client.get_or_create_collection(
        name = "NIPs-paper",
        metadata={"hnsw:space": "cosine"}
    )

collection.add(
    documents=title_list[:4000],
    ids=id_list[:4000]
)

collection.add(
    documents=title_list[4000:],
    ids=id_list[4000:]
)