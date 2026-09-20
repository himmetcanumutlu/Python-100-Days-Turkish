# Translated to Turkish by himmetcanumutlu

"""
Nesne yönelimli
Sayım (enum) - bir değişkenin değeri yalnızca sınırlı sayıda seçenek alıyorsa en uygun tip sayımdır
Sayım aracılığıyla sembolik sabitler tanımlayabiliriz; sembolik sabit, değişmez sabitten üstündür
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """Renk (sayım)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """Kart"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        suites = ('♠️', '♥️', '♣️', '♦️')
        faces = ('', 'A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{suites[self.suite.value]} {faces[self.face]}'


class Poker():
    """Poker destesi"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """Desteyi karıştır"""
        self.index = 0
        random.shuffle(self.cards)

    def deal(self):
        """Kart dağıt"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        """Daha fazla kart var mı"""
        return self.index < len(self.cards)


class Player():
    """Oyuncu"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """Kart çek"""
        self.cards.append(card)

    def arrange(self):
        """Eldeki kartları düzenle"""
        self.cards.sort(key=lambda card: (card.suite, card.face))


def main():
    """Ana fonksiyon"""
    poker = Poker()
    poker.shuffle()
    players = [
        Player('Doğu Sapkını'), Player('Batı Zehri'),
        Player('Güney İmparatoru'), Player('Kuzey Dilencisi')
    ]
    while poker.has_more:
        for player in players:
            player.get_card(poker.deal())
    for player in players:
        player.arrange()
        print(player.name, end=': ')
        print(player.cards)


if __name__ == '__main__':
    main()
