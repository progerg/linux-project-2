import os
import time
import requests
import logging

DATA_DIR = "/data"
WEB_SERVER_URL = "http://web-server:5000/status"

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

__log__ = logging.getLogger(__name__)


def check_server_status():
    try:
        response = requests.get(WEB_SERVER_URL)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        logging.error("Error: %s", e)
        return False


def process_data():
    if check_server_status():
        __log__.info("Server is healthy")
    else:
        __log__.error("Server is not healthy")


if __name__ == "__main__":
    while True:
        process_data()
        time.sleep(10)
