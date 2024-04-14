# Part of Standard Library (No install required)
import statistics

# Third Party Library (pip install yfinance)
import yfinance as yahoo

# Script written for this activity
import market_info
import Rf

# Assume our risk-free rate is the average interest rate of T-Bills from the
# previous month
rfr = Rf.Rf

def get_excess_return(return_series):
        excess_r_series = []
        idx = 1
        for r in return_series:

            excess_r_series.append( (r - rfr[idx]) )
            idx += 1
        return excess_r_series

excess_return_gspc = get_excess_return(market_info.return_sp)

def compute_alpha_and_beta(ticker):

# Create a dictionary containing all available information about each asset
    # asset1 = yahoo.Ticker(ticker).info

    return_series = market_info.get_return_series(ticker)

    # Calcualte Excess Returns

    excess_return_asset = get_excess_return(return_series)
    true_excess_return_gspc = []

    if len(excess_return_asset) < 60:
        true_excess_return_gspc = excess_return_gspc[0:len(excess_return_asset)]
    else:
        true_excess_return_gspc = excess_return_gspc
    
    # print(ticker)
    # print(excess_return_asset)
    # print(true_excess_return_gspc)

    if len(true_excess_return_gspc) < 2:
         return (0,0)

    slope, intercept = statistics.linear_regression(true_excess_return_gspc, excess_return_asset)

    return (slope, intercept)