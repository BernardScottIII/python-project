# ticker_list = []

# with open("nasdaq_tickers.txt", "r") as input:
#     for line in input:
#         ticker_list.append(line)

partial_ticker_list = []

with open("partial_tickers.txt", "r") as input:
    for line in input:
        partial_ticker_list.append(line)

# with open("nasdaq-listed.csv", "r") as input:
#     input.readline()
#     for line in input:
#         ticker_list.append(line.split(",")[0])

# with open("nasdaq_tickers.txt", "w+") as output:
#     for ticker in ticker_list:
#         output.write(ticker + "\n")