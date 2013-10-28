import unittest

import datetime
from TraderPOC.streams.utils import makeOptionSymbol

class testMakeOptionSymbol(unittest.TestCase):

    def testAAPL(self):
        self.assertEqual("AAPL131101P00470000", 
                         makeOptionSymbol("AAPL",
                                          datetime.date(2013,11,01),
                                          "put",
                                          470
                                          )
                         )

    def testMini(self):
        self.assertEqual("AAPL7131101P00470000", 
                         makeOptionSymbol("AAPL",
                                          datetime.date(2013,11,01),
                                          "put",
                                          470,
                                          mini=True
                                          )
                         )                  
                         

    def testDecimal(self):
        self.assertEqual("AA131101C00009500",
                         makeOptionSymbol("AA",
                                          datetime.date(2013,11,01),
                                          "call",
                                          9.50
                                          )
                         )


def test_suite():
    return makeSuite(testMakeOptionSymbol)
