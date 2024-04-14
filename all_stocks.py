import stock_portfolio as sp

ticker_list = []

with open("NYSE_and_NYSE_MKT_Trading_Units_Daily_File.xls", "r") as input:
    for line in input:
        cols = line.split("\t")
        # print(cols)
        ticker_list.append(cols[1])

# print(ticker_list)

maxAlpha = 0
maxBeta = 0
maxAlphaTicker = ""
maxBetaTicker = ""

for ticker in ticker_list:
    # print(ticker)
    # print(type(ticker))
    alpha, beta = sp.compute_alpha_and_beta(ticker)
    if alpha > maxAlpha:
        maxAlpha = alpha
        maxAlphaTicker = ticker
    if beta > maxBeta:
        maxBeta = beta
        maxBetaTicker = ticker

print(maxAlpha)
print(maxBeta)
print(maxAlphaTicker)
print(maxBetaTicker)