# Translated to Turkish by himmetcanumutlu

"""
Poker
"""
import enum
import random


@enum.unique
class Suite(enum.Enum):
    """Renk (sayım)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """Kart"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'


class Poker:
    """Poker destesi"""

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """Desteyi karıştır"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """Kart dağıt"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """Dağıtılacak kart var mı"""
        return self.current < len(self.cards)


def main():
    """Ana fonksiyon (programın girişi)"""
    poker = Poker()
    poker.shuffle()
    print(poker.cards)


if __name__ == '__main__':
    main()
