from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class TableScraper:
    def __init__(self, headless: bool = False, timeout: int = 15):
        opts = Options()
        opts.add_argument("--start-maximized") # Start maximized
        if headless:
            opts.add_argument("--headless=new") # Minimizing once started

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opts
        )
        self.wait = WebDriverWait(self.driver, timeout)
    
    def open(self, url: str):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.minimize_window()

    def minimize(self): # Explicitly minimize per requirement
        self.driver.minimize_window() 
 
    def close(self):
        self.driver.quit()

    def fetch_table_rows(self, table_xpath: str) -> list:
        rows = self.driver.find_elements(By.XPATH, table_xpath)
        data = []
        for row in rows:
        # Look for both header and data cells
            cells = row.find_elements("xpath", ".//th | .//td")
            cell_texts = [cell.text.strip() for cell in cells]
            data.append(cell_texts)
        return data