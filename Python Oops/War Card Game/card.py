import sys

# Ensure the output is in UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')


class Card:
    
    SPECIAL_CARDS = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    
    def __init__(self, suit, value) -> None:
        self._suit = suit
        self._value = value
    
    @property
    def suit(self):
        return self._suit
    
    @property
    def value(self):
        return self._value
    
    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol
        
        if self.isSpecial():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")
    
    
    def isSpecial(self):
        return self._value in Card.SPECIAL_CARDS