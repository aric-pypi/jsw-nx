import jsw_nx as nx
from datetime import datetime


def test_ipa():

    assert nx.is_process_alive('chrome') is True
    assert nx.is_process_alive('msn') is False
