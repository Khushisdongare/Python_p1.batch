import time
import logging
from functools import wraps
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_timestamp = datetime.now().isoformat()
        
        logging.info(f"Function '{func.__name__}' started at {start_timestamp}")
        logging.info(f"Arguments: args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)

        end_time = time.time()
        end_timestamp = datetime.now().isoformat()
        duration = end_time - start_time
        
        logging.info(f"Function '{func.__name__}' ended at {end_timestamp}")
        logging.info(f"Execution time: {duration:.4f} seconds\n")
        
        return result
    return wrapper
