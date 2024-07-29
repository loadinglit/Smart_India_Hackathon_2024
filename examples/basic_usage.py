import os
from rag.secrets import Secrets
from rag.inference.chat import ChatService
from rag.models import LiteLLMModels
from rag.prepare.document_loaders import DocumentLoader
from rag.vectorstores import VectorStoreManager

def main():
    directory_path = "path/to/your/documents"
    documents = DocumentLoader.load_documents_from_directory(directory_path)
    
    # bucket_name = "your-bucket-name"
    # s3_directory = "path/in/bucket"
    # documents = DocumentLoader.load_documents_from_s3(bucket_name, s3_directory)

    vector_store_manager = VectorStoreManager(URI=Secrets.ATLAS_CONNECTION_STRING)

    db_name = "your_database_name"
    collection_name = "your_collection_name"
    vector_store_index = vector_store_manager.create_vector_store(db_name, collection_name, documents)

    chat_service = ChatService()

    user_query = "What is the process for onboarding new employees?"
    user_ip = "192.168.1.1"  

    response = chat_service.chat(user_query, user_ip, db_name, collection_name)


    response_from_custom_model = chat_service.ask_litellm("Hi", model=LiteLLMModels.PHI_3_MINI)


    print("Response:", response["response"])
    print("Source Documents:", response["source_documents"])

if __name__ == "__main__":
    main()