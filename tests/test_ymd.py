import jsw_nx as nx
from datetime import datetime


def test_Ymd():
    year = 2022
    nx.Ymd.each_month(2022, lambda y, m: print(y,m))
