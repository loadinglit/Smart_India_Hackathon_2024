import tiktoken
from rag.settings import logger
from rag.settings import logger
from rag.database import DatabaseConnector
from llama_index.core.callbacks import TokenCountingHandler
from llama_index.core import ( VectorStoreIndex, StorageContext )
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch

class VectorStoreManager:
    """
    A class for managing vector stores in a database.

    Methods
    -------
    create_vector_store(db_name: str, collection_name: str, index_name: str, documents: list) -> VectorStoreIndex
        Creates a vector store from a list of documents.
    get_vector_store(db_name: str, collection_name: str, index_name: str) -> VectorStoreIndex
        Retrieves an existing vector store from the database.
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
