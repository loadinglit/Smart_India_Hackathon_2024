# Import key classes/functions for easier access
from .settings import logger
from .secrets import Secrets
from .prepare.database import DatabaseConnector  
from .prepare.document_loaders import DocumentLoader
from .prepare.vectorstores import VectorStoreManager
from .utils import TimeConverter

# Package metadata
__version__ = '0.0.1'
__author__ = 'Om Achrekar'
__email__ = 'om@scogo.in'