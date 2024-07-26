import warnings
from rag.models import Models
from rag.settings import logger
from rag.prompts import Prompts
from rag.secrets import Secrets
from llama_index.core import ChatPromptTemplate
from rag.vectorstores import VectorStoreManager
from llama_index.core.memory import ChatMemoryBuffer
from langchain_community.callbacks import get_openai_callback
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.storage.chat_store import SimpleChatStore


class ChatService:
    def __init__(self):
        self.chat_store = SimpleChatStore()
        self.prompts = Prompts()
        self.models = Models()

    def initialize_chat_store(self):
        try:
            chat_store = SimpleChatStore()
            logger.info("Chat store initialized successfully")
            return chat_store
        except Exception as e:
            logger.error(f"Error initializing chat store: {e}")
            raise
    
    def chat(
        self,
        user_query: str,
        user_ip: str,
        db_name: str,
        collection_name: str,
        index_name: str,
    ):
        try:
            warnings.filterwarnings("ignore")
            chat_memory = ChatMemoryBuffer.from_defaults(
                token_limit=3000,
                chat_store=self.chat_store,
                chat_store_key=user_ip,
            )

            text_qa_template = ChatPromptTemplate.from_messages(
                self.prompts.get_chat_text_qa_msgs()
            )

            vector_store_manager = VectorStoreManager(URI=Secrets.ATLAS_CONNECTION_STRING)
            index = vector_store_manager.get_vector_store(
                db_name, collection_name, index_name
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

            self.chat_store.persist(persist_path="chat_store.json")
            logger.info("Query processed successfully")
            return {
                "response": answer.response,
                "source_documents": answer.source_nodes[0].metadata["file_name"],
            }
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            raise
