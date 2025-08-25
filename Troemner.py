from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import time
import re

class TableScraper:
    def __init__(self, headless: bool = False, timeout: int = 15):
        opts = Options()
        opts.add_argument("--start-maximized")
        if headless:
            opts.add_argument("--headless=new")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opts
        )
        self.wait = WebDriverWait(self.driver, timeout)
    
    def open(self, url: str):
        self.driver.get(url)
        self.driver.maximize_window()

    def minimize(self): # Explicitly minimize per requirement
        self.driver.minimize_window() 

    def close(self):
        self.driver.quit()

    def load_all_products(self):
        prev_count = 0
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # wait for AJAX load
            products = self.driver.find_elements(By.XPATH, "//ul[@id='resultsList']/li[contains(@class,'product-item')]")
            new_count = len(products)

            if new_count == prev_count:
                break
            prev_count = new_count
            print(f"Loaded {new_count} products...")

    def fetch_data(self):
        data = []

    # Make sure the DOM is fully loaded (call load_all_products() before this)
        products = self.driver.find_elements(
            By.XPATH, "//ul[@id='resultsList']/li[contains(@class,'product-item')]"
        )

        for product in products:
        # Product name + URL
            try:
                name_el = product.find_element(By.XPATH, './/a')
                product_name = name_el.text.strip()
                product_url = name_el.get_attribute("href")
            except:
                productName, productURL = "", ""

        # MODEL (part number) — parse from URL, then fallback to <li> id, then fallback from title text
            model = ""
            if product_url:
                m = re.search(r"/p/(\d+)", product_url)
                if m:
                    model = m.group(1)

            if not model:
                li_id = product.get_attribute("id")  # e.g., "product-list-row-80780388"
                m2 = re.search(r"(\d+)$", li_id or "")
                if m2:
                    model = m2.group(1)

            if not model and product_name:
                m3 = re.search(r"(\d{6,})", product_name)  # last resort: grab long number in title
                if m3:
                    model = m3.group(1)

        # Description
            try:
                description = product.find_element(
                    By.XPATH, ".//div[@class='description product-description']"
                ).text.strip()
            except:
                description = ""

        # Cost (may be absent on list cards)
            try:
                cost = product.find_element(
                    By.XPATH, "//*[@id='product-list-row-80780388']/div/div[4]/div[2]/div/div"
                ).text.strip()
            except:
                cost = ""

            data.append({
                "vendor": "troemner",
                "productName": product_name,
                "model": model,
                "description": description,
                "productURL": product_url,
                "cost": cost
            })

        return data



if __name__ == "__main__":
    bot = TableScraper()
    bot.open("https://www.troemner.com/Calibration-Weights/Balance-Calibration-Weights/OIML-Calibration-Weight-Sets/c/3944")
    
    bot.load_all_products()   # infinite scroll until all products load

    data = bot.fetch_data()
    bot.close()

    df = pd.DataFrame(data)
    df.to_csv("troemner_products.csv", index=False)