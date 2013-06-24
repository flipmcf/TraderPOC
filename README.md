TraderPOC
=========

A Open Source Stock Trading Framework

There is no code here yet - Repository Setup

The concept is an open source Trading Framework where the framework is free but the decision making algorithms can be kept secret.

Should provide packages and configuration for anyone to connect to their online broker.
  Etrade, TDAmeritrade, etc.

Should provide packages to connect to streams.
  Free streams like yahoo or google finance.
  Paid 3rd party streams.

Oh, a gui would be nice, but I have zero experience with that.




Components:

Trading Base: responsible for communication between us and your broker

-----------

Streamer Base: Responsible for receiving streaming data from internet (including, but not limited to quotes)
  ---ok so created a module called 'feeds'.  What's the difference between a 'stream' and a 'feed'
     a stream IsA feed.  a feed is not always a stream... ok....
     
     However, from an 'expert' point of view, everything is a 'stream of information'  
      so you can 'stream' data to the experts from a 'feed'.
     
     So, all experts see 'streams'.   The stream object, however, may simply be connecting to a feed somewhere on the net,
        for example, login to an email account where folks send messages to and parse the messages.
        
        the info we get, tho, will be output as a Stream.
     
So, stream is the right idea.  Stream objects may get info from a 'feed' somewhere, but the output will always be a 'stream'
  Still wondering about implementation.

---------------

Expert Base: responsible for taking data from streamer or other experts and providing opinions on trades.

---------------

Authentication system:  for gaining access to any system requiring authentication.

---------------


Trading Base should be an ABC that is designed to talk to specific brokers, such as etrade, and use an autheticator.

Streamer Base shoud provide a stream that experts can subscribe to.
   Twitter, Stocks, StockTwits, blogs, earnings reports, news, analyst upgrades, mutual fund holdings - anything.
   
   
Experts put it together - it's the 'meat' of the system.
   Experts can, and usually do, subscribe to one or more streams for inputs
   Experts utilize any algorithm (some can be written here as utilities, such as MACD, %K/%D etc)
   Experts can not communicate directly to Trading.
   Experts can (more commonly) provide a Stream consumable by other experts.
      stream can be local, or provided back to web for other experts to consume as a stream.
   Experts can read company reports, or anything and make opinions.
   Experts can form opions by 'managing' a collection of experts.
   Experts should, at first, be extremely single-minded - but if an expert managing many experts becomes sucessful, the entire
    algorithm could be put into a single expert to reduce latency between data and trades.
   
   
'Trader' is a TradingBase designed to listen to an expert and execute trades.
   Traders can send trades directly to broker, prepare trades, or monitor conditional trades.
   For example, etrade cannot do a percent trailing stop on an option, or submit a trailing stop based on a condition,
    so the Trader can do what the broker cannot do.
    also good for 'hidden stops'
   
   
