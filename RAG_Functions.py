import chromadb
chroma_client = chromadb.PersistentClient()
from openai import OpenAI
client = OpenAI()

# Create a collection with function
def create_collection(name):
    collection = chroma_client.get_or_create_collection(name=name, metadata={"hnsw:space": "cosine"} )
    return collection

def create_vectors(input_text, model):
    response = client.embeddings.create(input = input_text, model=model)
    vectors= response.data[0].embedding
    return vectors

def Search_listings(collection, vectors, max_results):
    response = collection.query(vectors, n_results=max_results)
    return response

def get_propery_description(collection, property_id,Doc_Type):
    response = collection.get(
        where = { 
            "$and": [ 
                {"property_ID": property_id},
                {"Doc_type": Doc_Type}
            ]
        }
    )
    return response
