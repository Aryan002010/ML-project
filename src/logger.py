
# this script is preparing a logging system that will save log messages into a file named with the current timestamp in the "logs" folder. The log file will 
# contain information about each log message, including the timestamp, logger name, severity level, and the actual log message content.





import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started") 