import stock_portfolio as sp
import get_tickers as tickers

ticker_list = tickers.partial_ticker_list
stock_list = {}

maxAlpha = 0
maxBeta = 0
maxAlphaTicker = ""
maxBetaTicker = ""

# print(ticker_list)
for ticker in ticker_list:
    ticker = ticker[:-1]
    result, analysis, assessment = sp.comp_regression(ticker)
    if result == 0:
        stock_list[ticker] = (0,0,0,0)
        continue
    alpha, beta = result.params[0], result.params[1]
    stock_list[ticker] = (alpha, beta, analysis, assessment)
    print(ticker + ": " + str(stock_list[ticker]))
    if alpha > maxAlpha:
        maxAlpha = alpha
        maxAlphaTicker = ticker
    if beta > maxBeta:
        maxBeta = beta
        maxBetaTicker = ticker

print(stock_list)   
print(maxAlpha)
print(maxBeta)
print(maxAlphaTicker)
print(maxBetaTicker)
