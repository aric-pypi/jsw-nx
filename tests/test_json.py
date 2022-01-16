import jsw_nx as nx


def test_json():
    json_str = '[{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]'
    target_json_str = '{"language": ["python", "ruby", "javascript"]}'
    assert nx.JSON.parse(json_str) == [{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]
    assert nx.JSON.stringify({"language": ["python", "ruby", "javascript"]}) == target_json_str
