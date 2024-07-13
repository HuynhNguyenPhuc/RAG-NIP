from utils.getter import id_list, title_list
import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.api.types import EmbeddingFunction

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

class CustomEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input):
        return model.encode(input).tolist()

embedding_func = CustomEmbeddingFunction()

client = chromadb.PersistentClient(path="database/chroma")

try:
    client.delete_collection("NIPs-paper")
except ValueError:
    pass
finally:
    collection = client.get_or_create_collection(
        name="NIPs-paper",
        embedding_function=embedding_func,
        metadata={"hnsw:space": "cosine"}
    )

num_records = len(title_list)

batch_size = 4000
for i in range(0, num_records, batch_size):
    end_index = min(i + batch_size, num_records)
    collection.add(
        documents=title_list[i:end_index],
        ids=id_list[i:end_index]
    )