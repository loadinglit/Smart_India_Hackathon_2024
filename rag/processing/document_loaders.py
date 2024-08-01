import os
import boto3
from rag.settings import logger
from rag.secrets import Secrets
from llama_index.readers.s3 import S3Reader
from llama_index.core import SimpleDirectoryReader
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


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
    def _convert_format(documents: list) -> list:
        lc_documents = []
        for doc in documents:
            lc_doc = doc.to_langchain_format()
            lc_documents.append(lc_doc)

        return lc_documents

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

        valid_extensions = ['pdf', 'txt', 'md', 'docs', 'docx']

        try:
            file_count=0
            invalid_files = []
            for root, _, files in os.walk(directory_path):
                for file in files:
                    file_count+=1
                    if not any(file.lower().endswith(ext) for ext in valid_extensions):
                        invalid_files.append(file)
            
            if file_count > Secrets.FILE_UPLOAD_LIMIT:
                 raise ValueError(
                      "Please try to upload less number of files."
                 )
            if invalid_files:
                raise ValueError(
                    f"Directory contains invalid file types: {invalid_files}")

            reader = SimpleDirectoryReader(directory_path)
            documents = reader.load_data()
            lc_documents = DocumentLoader._convert_format(documents)
            logger.info(f"Loaded {file_count} documents from {directory_path}")  
            return lc_documents
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
            raise ValueError(
                "Both bucket name and directory must be provided.")
        
        valid_extensions = ['pdf', 'txt', 'md', 'docs', 'docx']

        try:
            # Initialize S3 client
                s3_client = boto3.client(
                    's3',
                    aws_access_key_id=Secrets.AWS_ACCESS_ID,
                    aws_secret_access_key=Secrets.AWS_ACCESS_SECRET_KEY,
                )

                # List objects in the specified directory
                response = s3_client.list_objects_v2(
                    Bucket=bucket_name, Prefix=directory)
                if 'Contents' not in response:
                    raise ValueError(
                        "No files found in the specified directory.")

                # Check if all files have valid extensions
                invalid_files = []
                file_count=0
                for obj in response['Contents']:
                    file_name = obj['Key']
                    file_count+=1
                    if not any(file_name.lower().endswith(ext) for ext in valid_extensions):
                        invalid_files.append(file_name)
                
                if file_count > Secrets.FILE_UPLOAD_LIMIT:
                 raise ValueError(
                      "Please try to upload less number of files."
                 )

                if invalid_files:
                    raise ValueError(
                        f"S3 directory contains invalid file types: {invalid_files}")

                # Load documents using S3Reader
                reader = S3Reader(
                    bucket=f"{bucket_name}/{directory}",
                    aws_access_id=Secrets.AWS_ACCESS_ID,
                    aws_access_secret=Secrets.AWS_ACCESS_SECRET_KEY,
                )
                documents = reader.load_data()
                logger.info(
                    f"Loaded {len(documents)} documents from S3 bucket {bucket_name}")

                # Convert documents to the desired format using DocumentLoader
                lc_documents = DocumentLoader._convert_format(documents)
                return lc_documents
        except (NoCredentialsError, PartialCredentialsError) as cred_error:
                logger.error(f"AWS credentials error: {cred_error}")
                raise
        except Exception as e:
                logger.error(f"Error loading documents from S3: {e}")
                raise
