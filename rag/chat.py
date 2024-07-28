import os
import warnings
from typing import Union
from rag.models import Models
from rag.settings import logger
from rag.prompts import Prompts
from rag.secrets import Secrets
from rag.models import LiteLLMModels
from llama_index.core import Settings
from llama_index.core import ChatPromptTemplate
from rag.vectorstores import VectorStoreManager
from rag.custom_chat_store import MongoChatStore
from llama_index.core.memory import ChatMemoryBuffer
from langchain_community.callbacks import get_openai_callback

class ChatService:
    def __init__(self):
        self.URI = Secrets.ATLAS_CONNECTION_STRING
        self.prompts = Prompts()
        self.models = Models()
        Settings.llm = self.models.azure_llm
        Settings.embed_model = self.models.embed_model
        os.environ["ALLOW_RESET"] = "TRUE"

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
    

    def chat(
        self,
        user_query: str,
        user_ip: str,
        db_name: str,
        collection_name: str,
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
            chat_memory = ChatMemoryBuffer.from_defaults(
                token_limit=3000,
                chat_store=self._initialize_chat_store(),
                chat_store_key=user_ip,
            )

            text_qa_template = ChatPromptTemplate.from_messages(
                self.prompts.get_chat_text_qa_msgs()
            )
            
            vector_store_manager = VectorStoreManager(URI=Secrets.ATLAS_CONNECTION_STRING)
            index = vector_store_manager._get_vector_store(
                db_name, collection_name
            )

            with get_openai_callback() as cb:
                answer = index.as_chat_engine(
                    chat_mode="context",
                    memory=chat_memory,
                    system_prompt=text_qa_template,
                ).chat(user_query)
                logger.info(f"Total tokens used: {cb.total_tokens}")

            if not answer.source_nodes:
                logger.warning("No nodes retrieved from software manuals.")
            else:
                logger.info(f"Retrieved {len(answer.source_nodes)} nodes for query: {user_query}")
            logger.info("Query processed successfully")
            return {
                "response": answer.response,
                "source_documents": answer.source_nodes[0].metadata["file_name"],
            }
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            raise