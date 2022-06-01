import jsw_nx as nx

fu = nx.fileutils


def test_fileutils():
    res = fu.read_lines('/Users/aric.zheng/aric-notes/jsw-nx/jsw_nx/packages/qs.py')
    assert res == ['from urllib import parse', 'def qs(url):', 'query = parse.parse_qs(parse.urlparse(url).query)',
                    'return {k: v[0] if v and len(v) == 1 else v for k, v in query.items()}']
