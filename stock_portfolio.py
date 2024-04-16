# Third Party Library (pip install yfinance)
import statsmodels.api as stat
import numpy as np

# Script written for this activity
import market_info
import Rf

# Risk-Free Rate
rfr = Rf.Rf

def get_excess_return(return_series):
        excess_r_series = []
        idx = 1
        for r in return_series:
            if idx < len(rfr):
                excess_r_series.append( (r - rfr[idx]) )
                idx += 1

        return excess_r_series

excess_return_gspc = get_excess_return(market_info.return_sp)

def comp_regression(ticker):

    # Create a dictionary containing all available information about each asset
    return_series = market_info.get_return_series(ticker)

    # Avoid index out of bounds error
    if len(return_series) < 1:
        return (0,0,0)

    # Calcualte Excess Returns
    excess_return_asset = get_excess_return(return_series)
    true_excess_return_gspc = np.array([])

    if len(excess_return_asset) < 60:
        true_excess_return_gspc = np.array(excess_return_gspc[0:len(excess_return_asset)])
    else:
        true_excess_return_gspc = np.array(excess_return_gspc)

    if len(true_excess_return_gspc) < 2:
        return (0,0,0)

    true_excess_return_gspc = stat.add_constant(true_excess_return_gspc, prepend=True)
    regression = stat.OLS(excess_return_asset, true_excess_return_gspc).fit()

    analysis = ""
    assessment = ""

    # if intercept (alpha) is significantly different from zero
    alphaSignificance = ( (regression.params[0]) - 0 ) / regression.bse[0]
    if alphaSignificance < -2:
        analysis = "overpriced"
    elif alphaSignificance > 2:
        analysis = "underpriced"
    else:
        analysis = "hold"

    # if slope (beta) is significantly different from one
    betaSignificance = ( (regression.params[1]) - 1 ) / regression.bse[1]
    if betaSignificance < -2:
        assessment = "safer"
    elif betaSignificance > 2:
        assessment = "risker"
    else:
        assessment = "equivalent"

    # print(ticker, regression.summary(), analysis, assessment)

    return regression, analysis, assessment

# result = comp_regression(input("Enter ticker: "))
# print(result.summary())
# error = result.bse
# tvalues = result.tvalues
# print(error[0])
# print(error[1])
# print(tvalues)
# print(result.params)