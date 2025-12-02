import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    )


# def setup_logger(log_dir="logs"):
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)
    
#     log_filename = datetime.now().strftime("log_%Y_%m_%d_%H_%M_%S.log")
#     log_filepath = os.path.join(log_dir, log_filename)
    
#     logging.basicConfig(
#         filename=log_filepath,
#         level=logging.INFO,
#         format='%(asctime)s - %(levelname)s - %(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S'
#     )
    
#     console = logging.StreamHandler()
#     console.setLevel(logging.INFO)
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     console.setFormatter(formatter)
    
#     logging.getLogger('').addHandler(console)
    
#     logging.info("Logger initialized")
#     return logging.getLogger('')