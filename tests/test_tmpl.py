import jsw_nx as nx
from datetime import datetime


def test_tmpl():
    list_str = 'The first what you want to talk to python is: "{0} {1}"'
    dict_str = 'The first what you want to talk to python is: "My name is {name} and I am {age} years old"'

    str1 = nx.tmpl(list_str, ['hello', 'world'])
    str2 = nx.tmpl(dict_str, {'name': 'John', 'age': '25'})

    assert str1 == 'The first what you want to talk to python is: "hello world"'
    assert str2 == 'The first what you want to talk to python is: "My name is John and I am 25 years old"'
