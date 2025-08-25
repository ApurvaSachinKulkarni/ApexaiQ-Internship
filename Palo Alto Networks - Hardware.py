from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

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
    
if __name__ == "__main__":
    bot = TableScraper()
    bot.open("https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware-end-of-life-dates")
    
    table_xpath = './/table//tr' # XPath for rows in the table
    data=bot.fetch_table_rows(table_xpath)

    bot.close()
    
    df = pd.DataFrame(data[1:], columns=data[0]) # Convert to dataframe
    df=df.drop(columns=["End-of-Sale Date","Last Supported OS"])
    df = df.rename(columns={"End-of-Sale Product": "productName","End-of-Life Date":"EOL Date"})
    df["EOL Date"] = pd.to_datetime(df["EOL Date"], errors="coerce")
    df["EOL Date"] = df["EOL Date"].dt.strftime("%Y/%m/%d")
    df.to_csv('Hardware EOL Dates.csv', index=False) # Convert to csv