import chromadb
chroma_client = chromadb.PersistentClient()
# Create a collection with function
def create_collection(name):
    collection = chroma_client.get_or_create_collection(name=name, metadata={"hnsw:space": "cosine"} )
    return collection
