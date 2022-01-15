import jsw_nx as nx


def test_days():
    assert nx.days(2021, 1) == 31
    assert nx.days(2021, 2) == 28
    assert nx.days(2021, 4) == 30
    assert nx.days(2021, 5) == 31