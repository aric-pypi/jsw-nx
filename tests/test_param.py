import jsw_nx as nx

def test_param():
    qsl1 = { "q": 'python' }
    qsl2 = { 'include': 'exercises', 'homework_id': '7761529' }
    assert nx.param(qsl1) == 'q=python'
    assert nx.param(qsl2) == 'include=exercises&homework_id=7761529'