import jsw_nx as nx
from datetime import datetime


def test_env_select():
    assert nx.env_select() == 'local'
    assert nx.env_select('rmt') == 'rmt'

