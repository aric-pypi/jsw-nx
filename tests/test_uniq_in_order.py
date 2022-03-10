import jsw_nx as nx


def test_uniq_in_order():
    assert nx.unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    assert nx.unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
    assert nx.unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
