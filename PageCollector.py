class PageCollector:

    def __init__(self, products):
        self._products = products

    def get_sum(self, selector, page_num):

        def result_generator(products):
            sum_now = 0
            for idx, val in enumerate(products):
                sum_now += selector(val)
                if idx%page_num == page_num-1 or idx == len(products)-1:
                    yield sum_now
                    sum_now = 0

        return result_generator(self._products)
