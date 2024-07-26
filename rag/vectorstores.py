import tiktoken
from rag.settings import logger
from rag.settings import logger
from rag.database import DatabaseConnector
from pymongo.operations import SearchIndexModel
from llama_index.core.callbacks import TokenCountingHandler
from llama_index.core import (VectorStoreIndex, StorageContext)
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch


class VectorStoreManager:
    """
    A class for managing vector stores in a database.

    Methods
    -------
    create_vector_store_index(name: str) -> SearchIndexModel
        Creates a vector search index for a vector store in MongoDB Atlas.

    create_vector_store(db_name: str, collection_name: str, index_name: str, documents: list) -> VectorStoreIndex
        Creates a vector store from a list of documents.

    add_to_vector_store(db_name: str, collection_name: str, index_name: str, documents: list)
        Adds documents to an existing vector store in the database.

    get_vector_store(db_name: str, collection_name: str, index_name: str) -> VectorStoreIndex
        Retrieves an existing vector store from the database.

    delete_vector_store(db_name: str, collection_name: str)
        Deletes an existing vector store from the database.

    delete_document(db_name: str, collection_name: str, file_name: str)
        Deletes a single document from an existing vector store from the database.

    update_document(db_name: str, collection_name: str, file_name: str, document: list)
        Updates a single document in an existing vector store in the database.
    
    """

    def __init__(self, URI: str):
        """
        Initializes the VectorStoreManager with a MongoDB client and a token counter.
        """
        db = DatabaseConnector("mongodb", URI)
        self.client = db.client
        # self.token_counter = TokenCountingHandler(
        #     tokenizer=tiktoken.encoding_for_model("gpt-4o").encode
        # )

    def create_vector_store_index(self, name: str) -> SearchIndexModel:
        """
        Creates a vector search index for a vector store in MongoDB Atlas.

        Returns
        -------
        SearchIndexModel
            The created search index model.
        """
        search_index_model = SearchIndexModel(
            definition={
                "fields": [
                    {
                        "type": "vector",
                        "path": "embedding",
                        "numDimensions": 1536,
                        "similarity": "cosine"
                    },
                    {
                        "type": "filter",
                        "path": "metadata.page_label"
                    }
                ]
            },
            name=name,
            type="vectorSearch",
        )

        return search_index_model

    def create_vector_store(
        self, db_name: str, collection_name: str, index_name: str, documents: list
    ) -> VectorStoreIndex:
        """
        Creates a vector store in MongoDB Atlas from a list of documents.

        Parameters
        ----------
        db_name : str
            The name of the database.
        collection_name : str
            The name of the collection.
        index_name : str
            The name of the index.
        documents : list
            A list of documents to index.

        Returns
        -------
        VectorStoreIndex
            The created vector store index.

        Raises
        ------
        Exception
            If there is an error creating the vector store.
        """
        try:
            atlas_vector_search = MongoDBAtlasVectorSearch(
                self.client,
                db_name=db_name,
                collection_name=collection_name,
                index_name=index_name,
            )
            vector_store_context = StorageContext.from_defaults(
                vector_store=atlas_vector_search
            )
            vector_store_index = VectorStoreIndex.from_documents(
                documents, storage_context=vector_store_context, show_progress=True
            )
            # logger.info(f"Total tokens added: {self.token_counter.total_embedding_token_count}")
            logger.info("Vector store index created successfully")
            return vector_store_index
        except Exception as e:
            logger.error(f"Error creating vector store: {e}")
            raise

    def add_to_vector_store(
        self, db_name: str, collection_name: str, index_name: str, documents: list
    ) -> VectorStoreIndex:
        """
        Adds documents to an existing vector store in MongoDB Atlas.

        Parameters
        ----------
        db_name : str
            The name of the database.
        collection_name : str
            The name of the collection.
        index_name : str
            The name of the index.
        documents : list
            A list of documents to index.

        Returns
        -------
        VectorStoreIndex
            The created vector store index.

        Raises
        ------
        Exception
            If there is an error creating the vector store.
        """
        try:
            atlas_vector_search = MongoDBAtlasVectorSearch(
                self.client,
                db_name=db_name,
                collection_name=collection_name,
                index_name=index_name,
            )
            vector_store_context = StorageContext.from_defaults(
                vector_store=atlas_vector_search
            )
            VectorStoreIndex.from_documents(
                documents, storage_context=vector_store_context, show_progress=True
            )
            # logger.info(f"Total tokens added: {self.token_counter.total_embedding_token_count}")
            logger.info("Documents added successfully")
        except Exception as e:
            logger.error(f"Error adding documents: {e}")
            raise

    def get_vector_store(self, db_name: str, collection_name: str, index_name: str) -> VectorStoreIndex:
        """
        Retrieves an existing vector store from MongoDB Atlas.

        Parameters
        ----------
        db_name : str
            The name of the database.
        collection_name : str
            The name of the collection.
        index_name : str
            The name of the index.

        Returns
        -------
        VectorStoreIndex
            The retrieved vector store index.

        Raises
        ------
        Exception
            If there is an error retrieving the vector store.
        """
        try:
            atlas_vector_search = MongoDBAtlasVectorSearch(
                self.client,
                db_name=db_name,
                collection_name=collection_name,
                index_name=index_name,
            )
            vector_store_index = VectorStoreIndex.from_vector_store(
                atlas_vector_search
            )
            logger.info("Vector store index retrieved successfully")
            return vector_store_index
        except Exception as e:
            logger.error(f"Error retrieving vector store: {e}")
            raise

    def delete_collection(self, db_name: str, collection_name: str):
        """
        Deletes an existing vector store from MongoDB Atlas.

        Parameters
        ----------
        db_name : str
            The name of the database.
        collection_name : str
            The name of the collection.

        Raises
        ------
        Exception
            If there is an error deleting the vector store.
        """
        try:
            db = self.client[db_name]
            db.drop_collection(collection_name)
            logger.info("Vector store deleted successfully")
        except Exception as e:
            logger.error(f"Error deleting vector store: {e}")
            raise

    def delete_document(self, db_name: str, collection_name: str, file_name: str):
        """
        Deletes a single document from an existing vector store from MongoDB Atlas.

        Parameters
        ----------
        db_name : str
            The name of the database.
        collection_name : str
            The name of the collection.
        file_name : str
            The name of the document.

        Raises
        ------
        Exception
            If there is an error deleting the vector store.
        """
        try:
            db = self.client[db_name]
            condition = {'file_name': file_name}
            collection = db[collection_name]
            result = collection.delete_many(condition)
            logger.info(f"{result.deleted_count} documents associated with {file_name} have been deleted.")
        except Exception as e:
            logger.error(f"Error deleting vector store: {e}")
            raise

    def update_document(self, db_name: str, collection_name: str, file_name: str, document: list):
        """
        Updates a single document in an existing vector store in MongoDB Atlas.

        Parameters
        ----------
        db_name : str
            The name of the database.
        collection_name : str
            The name of the collection.
        file_name : str
            The name of the document.
        document : list
            The updated document.

        Raises
        ------
        Exception
            If there is an error updating the document.
        """
        try:
            db = self.client[db_name]
            condition = {'file_name': file_name}
            collection = db[collection_name]
            result = collection.delete_many(condition)
            self.add_to_vector_store(db_name, collection_name, collection_name, document)
            logger.info(f"{result.deleted_count} documents associated with {file_name} have been updated.")
        except Exception as e:
            logger.error(f"Error updating document: {e}")
            raise