import jsw_nx as nx


def test_get_domain():
    assert nx.get_domain('http://www.baidu.com/link?url=3Ber') == 'www.baidu.com'
