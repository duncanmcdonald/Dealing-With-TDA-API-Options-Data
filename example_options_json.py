# Import the client
from td.client import TDClient
import os
import json

def print_nested(dict_obj):
    # Iterate over all key-value pairs of a dict
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            print_nested(value)
        else:
            if isinstance(value, list):
                print("")
                for inner in value:
                    print_nested(inner)
            else:
                print(key, ':', value)
                

# Create a new session, credentials path is required.
TDSession = TDClient(
    client_id = os.environ['TDAMERITRADE_CLIENT_ID'],
    redirect_uri = 'http://localhost',
    credentials_path='[put your path here]/credentials.json'
)

# Login to the session
TDSession.login()
        
# Option Chain Example
opt_chain = {
    'symbol': 'MSFT',
    'contractType': 'PUT',
    'optionType': 'S',
    'fromDate': '2020-04-01',
    'afterDate': '2020-05-21',
    'strikeCount': 20,
    'includeQuotes': False,
    'range': 'ITM',
    'strategy': 'ANALYTICAL',
}

'''
Option chain possible fields
symbol:
contractType:
strikeCount:
includeQuotes:
strategy:
interval
strike
range
fromDate
toDate
volatility
underlyingPrice
interestRate
daysToExpiration
expMonth
optionType
'''

# Get Option Chains
option_chains = TDSession.get_options_chain(option_chain = opt_chain)
for key, value in option_chains.items():
    with open('option_chain.json', 'w') as outfile:
        json.dump(option_chains, outfile, indent=2)


    
