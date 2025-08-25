import time
from scraper.table_scraper import TableScraper
import pandas as pd


if __name__ == "__main__":

    bot = TableScraper()
    bot.open("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area")
    
    table_xpath = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr' # XPath for rows
    data=bot.fetch_table_rows(table_xpath)

    table_xpath = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/thead/tr' # XPath for  column headings in the table
    header=bot.fetch_table_rows(table_xpath)

    bot.close()
    
    df = pd.DataFrame(data[1:], columns=header[0]) # Convert to dataframe
    df.to_csv('asian_countries.csv', index=False) # Convert to csv