import jsw_nx as nx
from datetime import datetime


def test_Date():
    timestamp = 1528797322
    date_time = datetime.fromtimestamp(timestamp)

    assert nx.Date.format(date_time, 'date') == '2018-06-12'
    assert nx.Date.format(date_time, 'time') == '17:55:22'
    assert nx.Date.format(date_time, 'datetime') == '2018-06-12 17:55:22'
    assert nx.Date.now() == int(datetime.now().timestamp())
    assert isinstance(nx.Date.create('2019-12-04'), datetime) is True
    assert isinstance(nx.Date.create(1528797322), datetime) is True
