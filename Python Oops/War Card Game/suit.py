import sys

# Ensure the output is in UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')


class Suit:
    
    SYMBOLS = {'clubs': '♣', 'diamonds': '♦', 'hearts': '♥', 'spades': '♠'}
    
    def __init__(self, description) -> None:
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]
    
    @property
    def description(self):
        return self._description
    
    @property
    def symbol(self):
        return self._symbol   