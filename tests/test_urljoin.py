import jsw_nx as nx


def test_base_filter():
    url1 = "http://www.example.com/path/to/file.html"
    url2 = "/test.html"
    res = nx.urljoin(url1, url2)
    assert res == "http://www.example.com/test.html"
