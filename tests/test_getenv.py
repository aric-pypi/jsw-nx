import jsw_nx as nx


def test_get_env():
    assert '/Users/' in nx.getenv('HOME')
