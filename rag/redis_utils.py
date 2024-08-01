from langchain.globals import set_llm_cache
from langchain_community.cache import RedisSemanticCache
from rag.models import Models
from llama_index.core import Settings
from rag.settings import logger
from rag.processing.database import DatabaseConnector
from langchain_community.chat_message_histories import RedisChatMessageHistory


class RedisUtils:
    def __init__(self, URI: str):
        self.URI = URI
        # self.client = DatabaseConnector("redis", URI)
        self.models = Models()
        Settings.embed_model = self.models.embed_model

    
    def initalise_redis_cache(self):
       set_llm_cache(RedisSemanticCache(
            embedding=self.models.embed_model,
            redis_url=self.URI
        ))
       logger.info("Redis cache initialised successfully.")


    def get_message_history(self, session_id: str) -> RedisChatMessageHistory:
        return RedisChatMessageHistory(session_id, url=self.URI)
    
