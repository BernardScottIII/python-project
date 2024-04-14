import requests

response = requests.get("https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates?fields=record_date,security_desc,avg_interest_rate_amt&filter=security_desc:eq:Treasury%20Notes&sort=-record_date&page[size]=60")

Rf = [0.0]

for rate in response.json()["data"]:
    if rate["avg_interest_rate_amt"] != 'null':
        Rf.append( ( float(rate["avg_interest_rate_amt"]) / 100 ) / 12 )