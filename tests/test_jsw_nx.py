import jsw_nx

def test_days():
    assert jsw_nx.days(2021,1) == 31
    assert jsw_nx.days(2021,2) == 28
    assert jsw_nx.days(2021,4) == 30

def test_base_indexof():
    assert jsw_nx.indexof([1,2,3],2) == 1
    assert jsw_nx.indexof([1,2,3],5) == -1

def test_base_includes():
    assert jsw_nx.includes([1,2,3],2) == True
    assert jsw_nx.includes([1,2,3],5) == False