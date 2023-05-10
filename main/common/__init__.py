import logging
from logging.config import fileConfig

#fileConfig('logging_config.ini')
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)