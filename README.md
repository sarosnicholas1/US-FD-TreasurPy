# US-FD-TreasuryPy
##Description
This repository is an unofficial Python wrapper for the US Treasury Fiscial Data API. This api includes a substantial number of endpoints which I am continiously working to add. As of the offical version 1, this wrapper includes functions for Debt To Penny, Daily Treasury Statements, 120 Day Delinquent Debt Referral Compliance Report, Gold Reserve, Record Setting Auction, State and Local Government Series Securities (Non-Marketable), Treasury Report on Receivables (TROR), Schedules of Federal Debt by Day Activity and Schedules of Federal Debt by Day Summary.

#Usage
from TreasuryPy import tp

ex: tp.get_debt_to_penny({})

When calling the dataset, a parameters dictionary must be passed into the function. The parameters dictionary can contain parameters which can provided added functionality such as filtering, sorting, and formatting.

The fields value take in a string list of column names
The filters value take in a string list of column names with conditional opperator valid conditionals are: <, <=, >, >=, ==, === 
The pagination value takes in a dictionary with "number" and "size" corresponding to how many rows you want to return and at what position
The sorting value takes in a dictionary with the key being the selected field and the value being increasing or decreasing
The output value takes in a string of output types. The types are "csv", "json", "xml"
At this current time only the json output works


parameters = {
  "fields" : ["foo", "bar"],
  "filters" : ["foo_bar==2023-06-30", "foo_bar<=20"],  
  "pagination" : {
    "number" : 1,
    "size" : 10
  },
  "sorting" : {
    "foo" : "increasing"
  },
  "output" : "foo"
}


tp.get_debt_to_penny({})
