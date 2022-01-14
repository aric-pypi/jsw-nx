import jsw_nx

def test_packages():
    assert jsw_nx.days(2021,1) == 31
    assert jsw_nx.days(2021,2) == 28
    assert jsw_nx.days(2021,4) == 30