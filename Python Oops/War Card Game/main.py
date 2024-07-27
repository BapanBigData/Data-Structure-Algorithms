"""
All the required imports 
"""
import sys
from deck import Deck
from player import Player
from war_card_game import WarCardGame

# Ensure the output is in UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')


player = Player("Bapan", Deck(isEmpty=True))
computer = Player("Computer", Deck(isEmpty=True), isComputer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)
game.print_welcome_msg()


while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    # answer = input(
    #     "\nAre you ready for the next round?\nPress enter to continue. Enter X to stop.")

    # if answer.lower() == 'x':
    #     break
