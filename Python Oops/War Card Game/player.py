
class Player:
    
    def __init__(self, name, deck, isComputer=False) -> None:
        self.name = name
        self._deck = deck
        self._isComputer = isComputer
    
    @property
    def isComputer(self):
        return self._isComputer
    
    @property
    def deck(self):
        return self._deck
    
    def hasEmptyDeck(self):
        return self._deck.size == 0
    
    def drawCard(self):
        if not self.hasEmptyDeck():
            return self._deck.draw()
        else:
            return None
    
    def addCard(self, card):
        self._deck.add(card)