from utils.getter import id_list, title_list
import chromadb

embedding_func = chromadb.utils.embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-mpnet-base-v2"
)

client = chromadb.PersistentClient(path="database/chroma")

try:
    client.delete_collection("NIPs-paper")
except ValueError:
    pass
finally:
    collection = client.get_or_create_collection(
        name = "NIPs-paper",
        embedding_function= embedding_func,
        metadata={"hnsw:space": "cosine"}
    )

num_records = len(title_list)

for i in range(0, num_records, 4000): 
    collection.add(
        documents=title_list[i:(i + 4000) if (i + 4000) < num_records else num_records],
        ids=id_list[i:(i + 4000) if (i + 4000) < num_records else num_records]
    )