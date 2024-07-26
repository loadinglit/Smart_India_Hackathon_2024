# RAG

A package to create your own custom RAG system based on your data built by Scogo.

## Installation

To set up the package locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/om-scogo/rag.git
```
2. Navigate to the folder:
```bash
cd rag
```
3. Activate your virtual environment (if any)
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
5. Install the package locally:
```bash
pip install -e .
```

## Example Usage
### Load documents from directory:
```python
from rag.document_loaders import DocumentLoader

# document types supported: .pdf, .txt, .md, .docx, .doc
docs = DocumentLoader.load_documents_from_directory(directory_path)
```
### Load documents from s3:
```python
from rag.document_loaders import DocumentLoader

# document types supported: .pdf, .txt, .md, .docx, .doc
docs = DocumentLoader.load_documents_from_s3(bucket_name, directory)
```
### Create a vector index:
```python
from rag.secrets import Secrets
from rag.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector_index = vector.create_vector_store_index(vector_index)
```
### Store documents into MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING
vector.create_vector_store(db_name, collection_name, index_name, documents)
```
### Add new documents into MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.add_to_vector_store(db_name, collection_name, index_name, documents)
```
### Update specific document from MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.update_document(db_name, collection_name, file_name, documents)
```
### Delete specific document from MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.delete_document(db_name, collection_name, file_name)
```
### Delete collection from MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.delete_collection(db_name, collection_name)
```
### To use ChatService:
```python
from rag.chat import ChatService

chat_service = ChatService()

response = chat_service.chat(
    user_query,
    user_ip,
    db_name,
    collection_name,
    index_name"
)
print(response)
```
