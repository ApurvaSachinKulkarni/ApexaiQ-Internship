import requests
import pandas as pd
import matplotlib.pyplot as plt

class BitCoin_API:
    def GetUrl(url,params):
        response = requests.get(url,params=params)
        statuscode = response.status_code
        data = response.json()
        print("Status Code:", statuscode)
        return data
    
    def MakeDataFrame (data):
        df = pd.DataFrame(data["prices"],columns=["Date","Prices"])
        df["Date"] = pd.to_datetime(df["Date"], unit="ms")
        return df
    
    def PlotGraph(df):
        plt.figure(figsize=(12,6))
        plt.plot(df["Date"], df["Prices"], color="orange")
        plt.xlabel("Date")
        plt.ylabel("Bitcoin Price (USD)")
        plt.title("Bitcoin Prices Over Time")
        plt.xticks(rotation=45)
        plt.show()

if __name__ == "__main__":
    url="https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params={"vs_currency": "usd", "days": "30"}
    data = BitCoin_API.GetUrl(url,params)
    df = BitCoin_API.MakeDataFrame(data)
    BitCoin_API.PlotGraph(df)