#!/usr/bin/env python3 
# crazy 8s puzzle : get the longest left-right trick-subsequence 


class Card(object):
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", 
                  "10", "J", "Q", "K"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank 

    def __str__(self):
        return '%s of %s' (Card.rank_names[self.rank],Card.suit_names[self.suit])

    def __eq__(self, other):
         return (self.rank == 8) or (other.rank == 8)  or (self.rank == other.rank) or (self.suit == other.suit) 


class CrazyEights(object):
    def __init__(self):
        self.cards = []

    def read_card(self, card):
        suit = Card.suit_names.index(card.split()[1])
        rank = Card.rank_names.index(card.split()[0])
        c = Card(suit, rank)  # 7Hearts , JSpades 
        self.cards.append(c) 

    def get_longest_trick(self):
        memo = {}  # dictionary for memoization 
        n = len(self.cards)

        def trick(i):
            if i in memo: 
                return memo[i] 
            elif i == n-1:
                return 1
            else:
                res = 0
                for j in range(i+1, n):
                    if self.cards[i] == self.cards[j] and res < 1+trick(j):
                        res = 1 + trick(j)
                        memo[i] = res
            return res

        trick(0)
        print(memo)
        return max(memo.values())


def main():
    c8s_game = CrazyEights()
    for card in ['7 Hearts', '6 Hearts', '7 Diamonds', '3 Diamonds', '8 Clubs', 
                 'J Spades']:
        c8s_game.read_card(card)
    print(c8s_game.get_longest_trick())


if __name__ == '__main__':
    main()



