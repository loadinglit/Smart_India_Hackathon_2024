# from llama_index.core import SummaryIndex
# from llama_index.readers.web import SimpleWebPageReader
# from IPython.display import Markdown, display
# import os
# from rag.models import Models

# llm = Models().azure_llm

# # documents = SimpleWebPageReader(html_to_text=True).load_data(
# #     ["https://scogo.in/"]
# # )

# from llama_index.readers.web import AsyncWebPageReader

# loader = AsyncWebPageReader()
# documents = loader.load_data(urls=["https://scogo.in/"])

# print(documents)

# from rag.secrets import Secrets
# # from rag.processing.document_loaders import DocumentLoader
# from rag.processing.vectorstores import VectorStoreManager

# vsm = VectorStoreManager(Secrets.ATLAS_CONNECTION_STRING)
# # docs = DocumentLoader.load_documents_from_directory("./data")   

# print(len(documents))

# db_name = "cs"
# collection_name = "fundamentals"
# vector_store_index = vsm.create_vector_store(db_name, collection_name, documents)

# print(documents[0])
# print(f"length: {len(documents)}")

from rag.inference.chat import ChatService

chat_service = ChatService()

user_query = "If I want to do different actions based on different variables then what should I use and why?"
db_name = "cs"
collection_name = "fundamentals"

response = chat_service.chat(
    user_query,
    db_name,
    collection_name,
)   
print(f"\nQuery: {user_query}")
print(f"\nResponse: {response}")

# from rag.processing.vectorstores import VectorStoreManager
# from rag.secrets import Secrets

# vector_store_manager = VectorStoreManager(URI=Secrets.ATLAS_CONNECTION_STRING)
# vectorstore = vector_store_manager._get_vector_store(db_name, collection_name)
# retriever = vectorstore.as_retriever(
#                     search_type="similarity",
#                     search_kwargs={"k": 3},
#             )

# context = retriever.invoke(user_query)


# print("\n\n".join(c.page_content for c in context))




# from llama_index.readers.web.main_content_extractor.base import MainContentExtractorReader

# loader = MainContentExtractorReader()
# documents = loader.load_data(urls=["https://www.dataconversionlaboratory.com/post/the-role-of-structured-content-in-rag#:~:text=By%20integrating%20structured%20content%20or,troubleshooting%20issues%2C%20or%20product%20recommendations."])

# print(f"Length: {len(documents)}")  
# print(f"Text: {documents[0].text}")

# import requests
# from main_content_extractor import MainContentExtractor

# # Get HTML using requests
# # url = "https://www.codewithharry.com/blogpost/c-cheatsheet/"
# url = "https://github.com/HawkClaws/main_content_extractor"
# response = requests.get(url)
# response.encoding = 'utf-8'
# content = response.text

# # Get HTML with main content extracted from HTML
# extracted_html = MainContentExtractor.extract(content)

# print(extracted_html)

# # Get HTML with main content extracted from Markdown
# extracted_markdown = MainContentExtractor.extract(content, output_format="markdown")

# print("\n\n\n\n")

# print(extracted_markdown)

# from llama_index.readers.web import AsyncWebPageReader

# loader = AsyncWebPageReader()
# documents = loader.load_data(urls=["https://scogo.in/"])

# print(documents[0].text)

# from llama_index.readers.web import BeautifulSoupWebReader

# loader = BeautifulSoupWebReader()
# documents = loader.load_data(urls=["https://www.codewithharry.com/blogpost/c-cheatsheet/"])

# print(documents[0].text)


# from rag.processing.document_loaders import DocumentLoader

# dl= DocumentLoader()

# # url = "https://www.codewithharry.com/blogpost/c-cheatsheet/"
# # url = "https://github.com/HawkClaws/main_content_extractor"
# url = "https://www.dataconversionlaboratory.com/post/the-role-of-structured-content-in-rag#:~:text=By%20integrating%20structured%20content%20or,troubleshooting%20issues%2C%20or%20product%20recommendations.   "

# docs = dl.load_document_from_weblink(url)

# print(docs)