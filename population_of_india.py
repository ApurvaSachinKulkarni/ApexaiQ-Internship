from scraper.table_scraper import TableScraper
import pandas as pd

if __name__ == "__main__":

    bot = TableScraper()
    bot.open("https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_population")
    
    table_xpath = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/tbody/tr' # XPath for rows in the table
    data=bot.fetch_table_rows(table_xpath)

    table_xpath = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/thead/tr' # XPath for  column headings in the table
    header=bot.fetch_table_rows(table_xpath)

    bot.close()
    headers = ['header'.join(col).strip() for col in zip(header[0],header[1])]
    
    df = pd.DataFrame(data[1:], columns=data[0]) # Convert to dataframe
    df.to_csv('population_of_india.csv', index=False) # Convert to csv
