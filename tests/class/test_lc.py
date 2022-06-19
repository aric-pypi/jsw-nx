import jsw_nx as nx


def test_lc():
    lco = nx.LcOption()
    res = lco.get('60f77c8e85071346450995d3')

    assert res['key'] == 'lc_test'
    assert res['value'] == 'leancloud2'
