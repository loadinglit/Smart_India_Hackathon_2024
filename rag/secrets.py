import os
from dotenv import load_dotenv

load_dotenv()

class Secrets:
    GPT4o_BASE_URL = os.environ.get("AOAI_GPT4o_BASE_URL")
    GPT4o_VERSION = os.environ.get("AOAI_GPT4o_VERSION")
    GPT4o_KEY = os.environ.get("AOAI_GPT4o_KEY")
    GPT4o_MODEL = os.environ.get("AOAI_GPT4o_MODEL")
    AOAI_GPT4o_DEPLOYMENT = os.environ.get("AOAI_GPT4o_DEPLOYMENT")

    ADA_BASE_URL = os.environ.get("AOAI_ADA_BASE_URL")
    ADA_API_KEY = os.environ.get("AOAI_GPT4_KEY")
    ADA_VERSION = os.environ.get("AOAI_ADA_VERSION")
    ADA_MODEL = os.environ.get("AOAI_ADA_MODEL")
    ADA_DEPLOYMENT = os.environ.get("AOAI_ADA_DEPLOYMENT")

    LITELLM_KEY = os.environ.get("LITELLM_KEY")
    LITELLM_BASE_URL = os.environ.get("LITELLM_BASE_URL")

    ATLAS_CONNECTION_STRING = os.environ.get("ATLAS_CONNECTION_STRING")

    AWS_ACCESS_ID = os.environ.get("AWS_ACCESS_ID")
    AWS_ACCESS_SECRET_KEY = os.environ.get("AWS_ACCESS_SECRET_KEY")
