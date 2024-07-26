# Import key classes/functions for easier access
from .settings import logger
from .secrets import Secrets
from .database import DatabaseConnector  
from .document_loaders import DocumentLoader
from .vectorstores import VectorStoreManager
from .utils import TimeConverter

# Package metadata
__version__ = '1.0.0'
__author__ = 'Om Achrekar'
__email__ = 'om@scogo.in'