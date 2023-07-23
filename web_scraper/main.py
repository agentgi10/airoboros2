```python
import os
from selenium import webdriver
from scraper import Scraper
from data_handler import DataHandler
from config import BASE_URL, CHROMEDRIVER_PATH, OUTPUT_FILE

def main():
    # Setup webdriver
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

    # Initialize scraper and data handler
    scraper = Scraper(driver)
    data_handler = DataHandler(OUTPUT_FILE)

    # Navigate to the base URL
    driver.get(BASE_URL)

    # Scrape data and handle pagination
    while True:
        data = scraper.scrape_data()
        data_handler.write_to_file(data)

        if not scraper.handle_pagination():
            break

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()
```