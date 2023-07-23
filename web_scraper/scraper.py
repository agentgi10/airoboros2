```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, CHROMEDRIVER_PATH
from utils import format_data
import json

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_page(self):
        self.driver.get(BASE_URL)

    def extract_data(self):
        data = []
        elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.tv-data-view__item')))
        for element in elements:
            title = element.find_element_by_css_selector('.tv-data-view__title').text
            description = element.find_element_by_css_selector('.tv-data-view__description').text
            data.append(format_data(title, description))
        return data

    def handle_pagination(self):
        next_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tv-pagination__button_next')))
        if 'tv-pagination__button_disabled' not in next_button.get_attribute('class'):
            next_button.click()
            return True
        return False

    def scrape_data(self):
        self.navigate_to_page()
        all_data = []
        while True:
            data = self.extract_data()
            all_data.extend(data)
            if not self.handle_pagination():
                break
        self.driver.quit()
        return all_data

    def write_to_file(self, data):
        with open('output.jsonl', 'w') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')

if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.scrape_data()
    scraper.write_to_file(data)
```