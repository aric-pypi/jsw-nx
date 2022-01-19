import jsw_nx as nx

def test_tmpl():
    url1 = 'https://www.google.com/search?q=python'
    url2 = 'https://student-api.alo7.com/api/v1/extend_units/21487?include=exercises&homework_id=7761529'
    assert nx.hashlize(url1) == { "q": 'python' }
    assert nx.hashlize(url2) == { 'include': 'exercises', 'homework_id': '7761529' }