class PokerHands():
    def __init__(self, cards):
        self.cards = cards

    def has_cards(self):
        return len(self.cards) > 0

    def which_hand(self):
        pairs=0
        three_kind=0
        r = ''
        for c in self.count_number_of_each() :
            if c == 2 :
                pairs+=1
            if c == 3 :
                three_kind+=1

        if pairs < 2:
            r = 'one pair'
        else:
            r = 'two pairs'

        if three_kind == 1:
            r = "three kind"

        if pairs == 1 and three_kind == 1:
            r = 'FullHouse'

        return r

    def highest_card(self):
        high = 0
        for c in self.cards:
            if c > high:
                high = c
        return high

    def count_number_of_each(self):
        '''
            Conta quantas de cada carta existem na mao
        '''
        counter=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in self.cards:
            counter[i]+=1
        return counter