import jsw_nx as nx


def test_param():
    deep_dict = {
        'a': {
            'b': {
                'c': {
                    'd': [1, 2, 4, 5]
                }
            }
        }
    }

    nx.deep_each(deep_dict, lambda k, v, parent: print(k, v, parent))
