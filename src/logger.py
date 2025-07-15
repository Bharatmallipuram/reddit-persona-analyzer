import logging
import os
import sys
from datetime import datetime

def setup_logger(name="PersonaGen", log_dir="logs", level=logging.DEBUG):
    
    os.makedirs(log_dir, exist_ok=True)

    # Timestamped log file
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

    logger = logging.getLogger(name)

    # Avoid duplicate handlers if re-imported
    if getattr(logger, "_setup_complete", False):
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # File Handler with UTF-8 encoding (for emojis/special chars)
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stream Handler (console)
    stream_handler = logging.StreamHandler(sys.stdout)   # Prints the log into the terminal.
    try:
        stream_handler.setFormatter(formatter)
    except UnicodeEncodeError:
        # fallback plain formatter if terminal can't handle emoji
        stream_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

    logger.addHandler(stream_handler)

    # Flag to prevent re-adding handlers
    logger._setup_complete = True

    return logger
