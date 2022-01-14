import jsw_nx


def test_days():
    assert jsw_nx.days(2021, 1) == 31
    assert jsw_nx.days(2021, 2) == 28
    assert jsw_nx.days(2021, 4) == 30


def test_base_indexof():
    assert jsw_nx.indexof([1, 2, 3], 2) == 1
    assert jsw_nx.indexof([1, 2, 3], 5) == -1


def test_base_includes():
    assert jsw_nx.includes([1, 2, 3], 2) == True
    assert jsw_nx.includes([1, 2, 3], 5) == False


def test_base_map():
    assert jsw_nx.map([1, 2, 3], lambda v, i: v + 1) == [2, 3, 4]


def test_base_reduce():
    assert jsw_nx.reduce([1, 2, 3], lambda res, v, i: res + v) == 6


def test_base_filter():
    assert jsw_nx.filter([1, 2, 3], lambda v, i: v > 1) == [2, 3]


def test_base_mix():
    res = jsw_nx.mix(None, {"a": 123, "b": "234"}, {"c": 'AAA'})
    assert res == {"a": 123, "b": '234', "c": "AAA"}


def test_base_get():
    test_data = {
        'name': 'wonder',
        'contact': {
            'phone': 110,
            'sns': {
                'qq': {
                    'code': 112,
                }
            }
        },
    }

    assert jsw_nx.get(test_data, 'name') == 'wonder'
    assert jsw_nx.get(test_data, 'english_name') == None
    assert jsw_nx.get(test_data, 'contact.phone') == 110
    assert jsw_nx.get(test_data, 'contact.phone.mobile') == None
    assert jsw_nx.get(test_data, 'contact.sns.qq.code') == 112
    assert jsw_nx.get(test_data, 'other1.other2.other3') == None
    assert jsw_nx.get(None, 'name') == None
    assert jsw_nx.get(100, 'name') == None
    assert jsw_nx.get('some', 'name') == None
    assert jsw_nx.get('some', 'name', 'wonder') == 'wonder'


def test_rubify_to_f():
    assert jsw_nx.to_f('123.33') == 123.33
    assert jsw_nx.to_i('123') == 123
    assert jsw_nx.to_n('123') == 123
    assert jsw_nx.to_n('123.33') == 123.33
    assert jsw_nx.to_s(12.3) == '12.3'
