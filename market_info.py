import yfinance as yf
import requests

response = requests.get(
    url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates?filter=record_date:eq:2024-02-29,security_desc:eq:Treasury%20Bills&sort=-record_date"
)

interest_rate = float(response.json()["data"][0]["avg_interest_rate_amt"])
interest_rate_data = response.json()["data"]
interest_rate_series = []

for i in range( len(interest_rate_data) - 1 ):
    # print(interest_rate_data[i]["avg_interest_rate_amt"])
    p0 = float(interest_rate_data[i]["avg_interest_rate_amt"])
    p1 = float(interest_rate_data[i + 1]["avg_interest_rate_amt"])
    interest_rate_series.append(
        ( (p1 - p0) / p0 )
    )

def adjust_close(price, dividend, split):
    adj_price = price
    if split != 0:
        adj_price /= split
    return adj_price - dividend

def get_return_series(ticker):
    
    stock = yf.Ticker(ticker).history(period = "5y", interval = "1mo")

    stock_return_series = []

    # Prevent KeyError
    if not all(col in stock.columns.values for col in ["Close", "Dividends", "Stock Splits"]):
        return stock_return_series
    
    stock_close = stock["Close"]
    stock_dividends = stock["Dividends"]
    stock_splits = stock["Stock Splits"]
    
    for idx in range(len(stock_close)):

        adj_stock_close_old = adjust_close(stock_close.iloc[idx - 1], stock_dividends.iloc[idx - 1], stock_splits.iloc[idx - 1])
        adj_stock_close_new = adjust_close(stock_close.iloc[idx], stock_dividends.iloc[idx], stock_splits.iloc[idx])

        stock_return_series.append( (adj_stock_close_new - adj_stock_close_old) / adj_stock_close_old)

    return stock_return_series

return_sp = get_return_series("^GSPC")
