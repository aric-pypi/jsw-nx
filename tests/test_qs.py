import jsw_nx as nx

def test_qs():
    url1 = 'https://www.google.com/search?q=python'
    url2 = 'https://student-api.alo7.com/api/v1/extend_units/21487?include=exercises&homework_id=7761529'
    assert nx.qs(url1) == { "q": 'python' }
    assert nx.qs(url2) == { 'include': 'exercises', 'homework_id': '7761529' }