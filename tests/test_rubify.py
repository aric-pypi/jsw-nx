import jsw_nx as nx


def test_rubify_to_f():
    assert nx.to_f('123.33') == 123.33
    assert nx.to_i('123') == 123
    assert nx.to_n('123') == 123
    assert nx.to_n('123.33') == 123.33
    assert nx.to_s(12.3) == '12.3'


def test_rubify_times():
    nx.times(5, lambda i: print(i))
