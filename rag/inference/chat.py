
import os
import warnings
from typing import Union
from rag.models import Models
from rag.settings import logger
from rag.prompts import Prompts
from rag.secrets import Secrets
from rag.models import LiteLLMModels
from llama_index.core import Settings
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from rag.processing.vectorstores import VectorStoreManager
from rag.processing.custom_chat_store import MongoChatStore
from langchain_community.callbacks import get_openai_callback
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

class ChatService:
    def __init__(self):
        self.URI = Secrets.ATLAS_CONNECTION_STRING
        self.prompts = Prompts()
        self.models = Models()
        Settings.llm = self.models.azure_llm
        Settings.embed_model = self.models.embed_model
        set_llm_cache(InMemoryCache())
        os.environ["ALLOW_RESET"] = "TRUE"
        self.store = {}

    def _initialize_chat_store(self):
        """
        Initializes the chat store.

        Returns
        -------
        SimpleChatStore
            The initialized chat store.
        
        Raises
        ------
        Exception
            If there is an error initializing the chat store.
        """
        try:
            chat_store = MongoChatStore(self.URI, "test_chat_store")
            logger.info("Chat store initialized successfully")
            return chat_store
        except Exception as e:
            logger.error(f"Error initializing chat store: {e}")
            raise

    def ask_litellm(self, query: str, model: Union[LiteLLMModels, str] = LiteLLMModels.GEMMA_2_27B_IT) -> dict:
        """
        Queries the LiteLLM model with a given query and model.

        Parameters
        ----------
        query : str
            The query to send to the LiteLLM model.
        model : LiteLLMModel or str
            The model to use for the query. Default is LiteLLMModel.GEMMA_2_27B_IT.

        Returns
        -------
        dict
            A dictionary containing the response, usage, and model information.
        """
        if isinstance(model, LiteLLMModels):
            model = model.value

        messages = [{"role": "user", "content": query}]
        response = self.models.lite_llm.chat.completions.create(
            model=model, messages=messages
        )
        return {
            "response": response.choices[0].message.content,
            "usage": response.usage,
            "model": response.model,
        }
    
    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]

    def chat(
        self,
        user_query: str,
        db_name: str,
        collection_name: str,
        user_ip: str = None,
    ):
        """
        Processes a user query and returns a response.

        Parameters
        ----------
        user_query : str
            The query from the user.
        user_ip : str
            The IP address of the user.
        db_name : str
            The name of the database.
        collection_name : str
            The name of the collection.

        Returns
        -------
        dict
            A dictionary containing the response and source documents.

        Raises
        ------
        Exception
            If there is an error processing the query.
        """
        try:
            warnings.filterwarnings("ignore")
            vector_store_manager = VectorStoreManager(URI=Secrets.ATLAS_CONNECTION_STRING)

            vector_search = vector_store_manager._get_vector_store(db_name, collection_name)
            
            qa_retriever = vector_search.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 3},
            )

            PROMPT = self.prompts.prompt

            runnable = PROMPT | self.models.azure_llm

            with_message_history = RunnableWithMessageHistory(
                runnable,
                self.get_session_history,
                input_messages_key="question",
                history_messages_key="history",
            )

            with get_openai_callback() as cb:
                response = with_message_history.invoke(
                    {"question": user_query},
                    config={"configurable": {"session_id": "abc123"}},
                )
                logger.info(f"Total tokens used: {cb.total_tokens}")
            logger.info("Query processed successfully")
            return {
                "response": response.content
            }
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            raise
