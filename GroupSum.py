from collections import namedtuple

Item = namedtuple('Item', ['Id', 'Cost', 'Revenue', 'SellPrice'])

class ItemGroup:

    def __init__(self, items):
        self._items = items

    def get_group_sum_set(self, tag, num_of_a_group):
        ret_set = [0] * (len(self._items)/num_of_a_group + 1
                            if len(self._items)%num_of_a_group else 0)
        for idx, val in enumerate(self._items):
            ret_set[idx/num_of_a_group] += getattr(val, tag)
        return ret_set
