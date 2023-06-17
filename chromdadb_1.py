import chromadb
client = chromadb.Client()
collection = client.create_collection('test')
collection.add(
    documents=["This is a test document", "This is another test document"],
    metadatas={"name": "Test Document", "type": "test"},
    ids=["test1", "test2"]
)

results=collection.query(
    query_texts=["test1"],
    n_results=2
)
