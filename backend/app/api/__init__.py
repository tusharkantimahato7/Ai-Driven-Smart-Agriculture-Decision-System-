"""
myapi package initializer.
This file ensures that the package is recognized and can be imported.
It also sets up logging and configuration loading.
"""


import logging
from .config  import settings


# Configure Logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("initializing Api Package...")
