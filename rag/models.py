import os
import openai
from rag.settings import logger
from rag.secrets import Secrets
from llama_index.core import Settings
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

class Models:
    """
    A class to initialize and manage the LLM and embedding models.

    Attributes
    ----------
    llm : AzureChatOpenAI
        An instance of the AzureChatOpenAI model.
    embed_model : AzureOpenAIEmbeddings
        An instance of the AzureOpenAIEmbeddings model.
    """

    def __init__(self):
        """
        Initializes the Azure large language models and embedding models.
        """

        self.azure_llm = AzureChatOpenAI(
            base_url=Secrets.GPT4o_BASE_URL,
            openai_api_version=Secrets.GPT4o_VERSION,
            openai_api_key=Secrets.GPT4o_KEY,
            openai_api_type="azure",
            model=Secrets.GPT4o_MODEL,
            temperature=0.0,
        )
        logger.info(f"Azure {Secrets.GPT4o_MODEL} initialized")
        
        self.embed_model = AzureOpenAIEmbeddings(
            openai_api_version=Secrets.ADA_VERSION,
            base_url=Secrets.ADA_BASE_URL,
            openai_api_key=Secrets.ADA_API_KEY,
        )
        logger.info(f"Azure {Secrets.ADA_MODEL} initialized")
        
        Settings.llm = self.azure_llm
        Settings.embed_model = self.embed_model
        os.environ["ALLOW_RESET"] = "TRUE"

        self.lite_llm = openai.OpenAI(
            api_key=Secrets.LITELLM_KEY, 
            base_url=Secrets.LITELLM_BASE_URL
        )
        logger.info("LiteLLM initialized")

    def ask_litellm(self, query: str) -> dict:
        """
        Queries the LiteLLM model with a given query.

        Parameters
        ----------
        query : str
            The query to send to the LiteLLM model.

        Returns
        -------
        dict
            A dictionary containing the response, usage, and model information.
        """
        messages = [{"role": "user", "content": query}]
        response = self.lite_llm.chat.completions.create(
            model="google/gemma-2-27b-it", messages=messages
        )
        return {
            "response": response.choices[0].message.content,
            "usage": response.usage,
            "model": response.model,
        }
