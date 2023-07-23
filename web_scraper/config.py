```python
# config.py

# Base URL of the website to be scraped
BASE_URL = "https://www.tradingview.com/pine-script-reference/v5/"

# Path to the ChromeDriver executable
CHROMEDRIVER_PATH = "chromedriver.exe"

# Path to the output file
OUTPUT_FILE = "data/output.jsonl"

# DOM element IDs
DOM_IDS = {
    "pagination": "pagination-id",  # Replace with actual ID
    "data_container": "data-container-id"  # Replace with actual ID
}

# Data schema for the scraped data
DATA_SCHEMA = {
    "reference_name": "",
    "description": "",
    "example": "",
    "parameters": "",
    "returns": ""
}

# Message names for logging and error handling
MESSAGES = {
    "scrape_success": "Data scraped successfully.",
    "scrape_error": "Error occurred while scraping data.",
    "write_success": "Data written to file successfully.",
    "write_error": "Error occurred while writing data to file."
}
```