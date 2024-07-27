"""Requires imports"""
from player import Player
from deck import Deck
from card import Card


class WarCardGame:
    """
    A class to represent the War card game.

    Attributes:
    ----------
    PLAYER : int
        Constant representing the player.
    COMPUTER : int
        Constant representing the computer.
    TIE : int
        Constant representing a tie.
    _player : Player
        The player object.
    _computer : Player
        The computer player object.
    _deck : Deck
        The deck used in the game.
    """

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player: Player, computer: Player, deck: Deck) -> None:
        """
        Initializes the WarCardGame with player, computer, and deck.

        Parameters:
        ----------
        player : Player
            The player object.
        computer : Player
            The computer player object.
        deck : Deck
            The deck used in the game.
        """
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self) -> None:
        """
        Shuffles the deck and deals initial cards to the player and computer.
        """
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character: Player) -> None:
        """
        Deals 26 cards to the given character.

        Parameters:
        ----------
        character : Player
            The player or computer receiving the cards.
        """
        for _ in range(26):
            card = self._deck.draw()
            character.addCard(card)

    def start_battle(self, cards_from_war: list = None) -> int:
        """
        Starts a battle round between the player and the computer.

        Parameters:
        ----------
        cards_from_war : list, optional
            List of cards from the previous war (default is None).

        Returns:
        -------
        int
            The winner of the round: PLAYER, COMPUTER, or TIE.
        """
        print("\n== Let's Start the Battle ==\n")

        player_card = self._player.drawCard()
        computer_card = self._computer.drawCard()

        print("Your card: ")
        player_card.show()

        print("\nComputer card: ")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(
            player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won this round")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.star_war(cards_won)

        return winner

    def get_round_winner(self, player_card: Card, computer_card: Card) -> int:
        """
        Determines the winner of a round based on the card values.

        Parameters:
        ----------
        player_card : Card
            The player's card.
        computer_card : Card
            The computer's card.

        Returns:
        -------
        int
            The winner of the round: PLAYER, COMPUTER, or TIE.
        """
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card: Card, computer_card: Card, previous_cards: list) -> list:
        """
        Collects all cards won in a round.

        Parameters:
        ----------
        player_card : Card
            The player's card.
        computer_card : Card
            The computer's card.
        previous_cards : list
            List of cards from the previous war.

        Returns:
        -------
        list
            List of cards won in the round.
        """
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character: Player, lst_of_cards: list) -> None:
        """
        Adds the won cards to the winning character's deck.

        Parameters:
        ----------
        character : Player
            The player or computer receiving the cards.
        lst_of_cards : list
            List of cards to be added to the deck.
        """
        for card in lst_of_cards:
            character.addCard(card)

    def star_war(self, cards_from_battle: list) -> None:
        """
        Starts a war round if there is a tie.

        Parameters:
        ----------
        cards_from_battle : list
            List of cards from the tied battle.
        """
        player_cards = []
        computer_cards = []

        for _ in range(3):
            player_card = self._player.drawCard()
            player_cards.append(player_card)

            computer_card = self._computer.drawCard()
            computer_cards.append(computer_card)

        print("Six hidden cards: XXX XXX")

        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self) -> bool:
        """
        Checks if the game is over based on the player's and computer's decks.

        Returns:
        -------
        bool
            True if the game is over, False otherwise.
        """
        if self._player.hasEmptyDeck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print("Try again. The computer won.")
            return True
        elif self._computer.hasEmptyDeck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print(f"Excellent. You won, {self._player.name}! Congratulations.")
            return True
        else:
            return False

    def print_stats(self) -> None:
        """
        Prints the current statistics of the player's and computer deck.
        """
        print("\n----")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(
            f"The computer has {self._computer.deck.size} cards on it's deck.")
        print("----")

    def print_welcome_msg(self) -> None:
        """
        Prints the welcome msg
        """
        print("===========================================")
        print("|        Welcome to War Card Game!        |")
        print("===========================================")
