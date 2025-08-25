from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import time

def normalize_date(text):
    t = (text or "").strip()
    if not t or t.lower() in {"latest", "tbd", "n/a", "-"}:
        return t
    for fmt in ("%B %d, %Y", "%b %d, %Y", "%B, %Y", "%b, %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(t, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return t

driver = webdriver.Chrome()
driver.get("https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary")

# give React some time
time.sleep(5)

# scroll down slowly to trigger lazy loading
for i in range(5):
    driver.execute_script(f"window.scrollTo(0, {i*2000});")
    time.sleep(2)

# wait until at least one row appears
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//table//tbody//tr[td]"))
)

records = []

# get all tables with "Version" in header
tables = driver.find_elements(By.XPATH, "//table[.//th[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'version')]]")

for table in tables:
    # find the closest heading above the table
    software_name=" Prisma Access Browser"

    rows = table.find_elements(By.XPATH, ".//tbody/tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) < 3:
            continue
        version = cols[0].text.strip()
        release = normalize_date(cols[1].text.strip())
        eol = normalize_date(cols[2].text.strip())
        records.append([software_name, version, eol, release])

driver.quit()

# create single dataframe with rows from ALL tables
df = pd.DataFrame(records, columns=["Software Name", "Version", "EOL Date", "Release Date"])
df.to_csv('Software EOL Dates.csv', index=False) # Convert to csv