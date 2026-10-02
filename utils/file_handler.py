import os
from utils.logger import logger

def read_file(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        return None
    except PermissionError:
        logger.error(f"Permission denied when reading: {path}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected error reading file {path}: {e}")
        return None

def write_file(path, data):
    try:
        with open(path, "wb") as f:
            f.write(data)
        logger.debug(f"Successfully wrote data to {path}")
    except PermissionError as e:
        logger.error(f"Permission denied when writing: {path}")
        raise e
    except Exception as e:
        logger.exception(f"Unexpected error writing file {path}: {e}")
        raise e