
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
    
    expStr = expiration.strftime("%y%m%d")
 
    if oType == "call":
        oType = "C"
    elif oType == "put":
        oType = "P"
    else:
        raise ValueError, "oType must be 'call' or 'put'"

    strikeString = "%08d" % (strike*1000)

    return oSymbol+expStr+oType+strikeString
    

