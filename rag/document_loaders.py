from rag.settings import logger
from rag.secrets import Secrets
from llama_index.readers.s3 import S3Reader
from llama_index.core import SimpleDirectoryReader

class DocumentLoader:
    """
    A class for loading documents from various sources.

    Methods
    -------
    load_documents_from_directory(directory_path: str) -> list
        Loads documents from a local directory.
    load_documents_from_s3(bucket_name: str, directory: str) -> list
        Loads documents from an S3 bucket.
    """

    @staticmethod
    def load_documents_from_directory(directory_path: str) -> list:
        """
        Loads documents from a local directory.

        Parameters
        ----------
        directory_path : str
            The path to the directory containing documents.

        Returns
        -------
        list
            A list of loaded documents.

        Raises
        ------
        ValueError
            If the directory path is not provided.
        Exception
            If there is an error loading documents from the directory.
        """
        if not directory_path:
            raise ValueError("Directory path must be provided.")

        try:
            reader = SimpleDirectoryReader(directory_path)
            documents = reader.load_data()
            logger.info(f"Loaded {len(documents)} documents from {directory_path}")
            return documents
        except Exception as e:
            logger.error(f"Error loading documents from directory: {e}")
            raise

    @staticmethod
    def load_documents_from_s3(bucket_name: str, directory: str) -> list:
        """
        Loads documents from an S3 bucket.

        Parameters
        ----------
        bucket_name : str
            The name of the S3 bucket.
        directory : str
            The directory within the S3 bucket.

        Returns
        -------
        list
            A list of loaded documents.

        Raises
        ------
        ValueError
            If the bucket name or directory is not provided.
        Exception
            If there is an error loading documents from S3.
        """
        if not bucket_name or not directory:
            raise ValueError("Both bucket name and directory must be provided.")

        try:
            reader = S3Reader(
                bucket=f"{bucket_name}/{directory}",
                aws_access_id=Secrets.AWS_ACCESS_ID,
                aws_access_secret=Secrets.AWS_ACCESS_SECRET_KEY,
            )
            documents = reader.load_data()
            logger.info(f"Loaded {len(documents)} documents from S3 bucket {bucket_name}")
            return documents
        except Exception as e:
            logger.error(f"Error loading documents from S3: {e}")
            raise