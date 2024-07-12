from datetime import datetime
import logging
import os

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(levelname)s - %(message)s",
)

if __name__ =="__main__":
    logging.info("This is a test log message")