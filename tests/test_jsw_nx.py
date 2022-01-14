import jsw_nx
from jsw_nx import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_packages():
    assert jsw_nx.days(2021,1) == 31
    assert jsw_nx.days(2021,2) == 28
    assert jsw_nx.days(2021,4) == 30