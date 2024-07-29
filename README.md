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
## Phases
- Preparation Phase: Where we prepare the data, data processing/enrichment, and indexing the data. For this phase we are using LlamaIndex.
- Inference Phase: Where user interact with the pipeline, eg. input the search query, retrieve the relevant documents, and generate the response. For this phase we are using LangChain.
<p align="center">
<img width="700" alt="Screenshot 2024-07-29 at 5 22 56 PM" src="https://github.com/user-attachments/assets/ffaa5bb7-60ec-4b2f-aa91-55fe1d0c29fe">
</p>

## Example Usage
### Load documents from directory:
```python
from rag.prepare.document_loaders import DocumentLoader

# document types supported: .pdf, .txt, .md, .docx, .doc
docs = DocumentLoader.load_documents_from_directory(directory_path)
```
### Load documents from s3:
```python
from rag.prepare.document_loaders import DocumentLoader

# document types supported: .pdf, .txt, .md, .docx, .doc
docs = DocumentLoader.load_documents_from_s3(bucket_name, directory)
```
### Store documents into MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.prepare.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.create_vector_store(db_name, collection_name, documents)
```
### Add new documents into MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.prepare.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.add_to_vector_store(db_name, collection_name, documents)
```
### Update specific document from MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.prepare.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.update_document(db_name, collection_name, file_name, documents)
```
### Delete specific document from MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.prepare.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.delete_document(db_name, collection_name, file_name)
```
### Delete collection from MongoDB vector store:
```python
from rag.secrets import Secrets
from rag.prepare.vectorstores import VectorStoreManager

vector = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
vector.delete_collection(db_name, collection_name)
```
### To use ChatService:
#### Using default model:
```python
from rag.inference.chat import ChatService

chat_service = ChatService()

response = chat_service.chat(
    user_query,
    user_ip,
    db_name,
    collection_name,
)
print(response)
```
#### Using custom models:
As of now it supports two models:
- google/gemma-2-27b-it
- microsoft/Phi-3-mini-4k-instruct

```python
from rag.inference.chat import ChatService
from rag.models import LiteLLMModels

chat_service = ChatService()

response = chat_service.ask_litellm("Hi", model=LiteLLMModels.PHI_3_MINI)
```
