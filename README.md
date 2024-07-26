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
### ChatService
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
