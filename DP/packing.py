#!/usr/bin/env python3
# solution for

class KnapSack(object):
    def __init__(self, n, volume):
        self.n = n
        self.volume = volume
        self.items = []

    def add_item(self, _list):
        self.items.append(_list)

    def return_optimal_filling(self):
        filling_cache = [[None for _ in range(self.volume)] for _ in range(self.n)]

        def filling_bag(n, volume):
            if filling_cache[n-1][volume-1]:
                return filling_cache[n-1][volume-1]

            item_vol = int(self.items[n-1][1])
            item_val = int(self.items[n-1][2])

            if n == 0 or volume == 0:
                return 0
            elif item_vol > volume:
                ans = filling_bag(n-1, volume)
            else:
                ans = max(filling_bag(n-1, volume), item_val + filling_bag(n-1,
                                                                           (volume
                                                                            -
                                                                            item_vol)))
            filling_cache[n-1][volume-1] = ans
            return ans

        filling_bag(self.n, self.volume)
        return filling_cache

    def track_items(self):
        filling = self.return_optimal_filling()
        selected = []

        def track_items_helper(n, volume):
            if n == 0 or volume == 0:
                return
            elif filling[n-1][volume-1] == filling[n-2][volume-1]:
                track_items_helper(n-1, volume)
            else:
                selected.append(self.items[n-1][0])
                track_items_helper(n-1, volume - int(self.items[n-1][1]))

        track_items_helper(self.n, self.volume)
        return selected, filling[self.n-1][self.volume-1]

def main():
    testcases = int(input())
    for i in range(testcases):
        n, volume = tuple(int(x) for x in input().split())
        ks = KnapSack(n, volume)
        for j in range(n):
            ks.add_item([input().split(' ')])
        print(ks.return_optimal_filling())
