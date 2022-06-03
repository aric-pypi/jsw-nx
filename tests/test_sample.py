import jsw_nx as nx


def test_sample():
    assert nx.type(nx.sample([1, 2, 3])) == 'int'
    assert nx.type(nx.sample([1, 2, 3], 2)) == 'list'
