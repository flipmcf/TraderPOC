

def makeOptionSymbol(symbol, expiration, oType, strike, mini=False):
    """Returns options symbol string - OIC standard
       given a ticker symbol (str)
       an expiration date (datetime)
       a type (string either 'call' or 'put')  #TODO = make bool for efficiency
       a strike price (float)
       (optional) 'mini' (bool) to indicate mini options
    """
    
    oSymbol = symbol
    if mini:
        oSymbol = oSymbol+"7"
    
    expStr = expiration.strftime("%y%M%d")
 
    if oType == "call":
        oType = "C"
    elif oType == "put":
        oType = "P"
    else:
        raise ValueError, "oType must be 'call' or 'put'"

    strikeString = "%08d" % (i*1000)

    return oSymbol+expStr+oType+strikeString
    

def getOptionQuote(symbol, expiration,
                   mini=False):
    
    optionSymbol = makeOptionSymbol(symbol, expiration, mini)

    yQuery = """select option from yahoo.finance.options
                where symbol="%s"
                and expiration="%s"
                and option.symbol="%s"
             """
             




def __makeQS(queryVars):

  queryVars ={ "q" : 'select option from yahoo.finance.options where symbol="AAPL" and expiration="2013-11" and option.symbol="AAPL131101P00470000"',
             "diagnostics" : "true",
             "env" : "store://datatables.org/alltableswithkeys",
             "format" : "json",
             }
 
  url = "http://query.yahooapis.com/v1/public/yql" + "?" + qs

def __request():
  #response = UrlFetchApp.getRequest(url);
  #response = UrlFetchApp.fetch(url, {'muteHttpExceptions':true});
  #Logger.log(response); 
