```python
import os
import json
import logging
from selenium.common.exceptions import NoSuchElementException

def setup_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def check_file_path(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_configurations(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def check_element_exists(driver, element_id):
    try:
        driver.find_element_by_id(element_id)
    except NoSuchElementException:
        return False
    return True
```