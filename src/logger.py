import logging 
import os
from datetime import datetime as dt 

log_file_name = f"{dt.now().strftime("%d_%m_%Y_%H_%M_%s")}.log"
log_file_path = os.path.join(os.getcwd(),"logs",log_file_name)
os.makedirs(log_file_path, exist_ok = True)

logging.basicConfig(
    filename=log_file_path,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",                
    level=logging.INFO
                    )