import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    API_KEY = os.environ["API_KEY"]
except KeyError:
    API_KEY = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {API_KEY}")
    
    headers = {
        'Authorization': f"Bearer {API_KEY}"
    }
    r = requests.get("https://jedi.enterprise.corellium.com/api/v1/instances", headers=headers)
    if r.status_code == 200:
        data = r.json()
        device_name = data[0]['name']
        logger.info(f'Name of first device: {device_name}')
