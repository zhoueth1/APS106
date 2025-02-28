#############################
# APS106 Winter 2025 - lab5 #
# Card Game                 #
#############################

import random

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - DO NOT EDIT
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    cards = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            cards.append([suit,number])

    return cards

def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck

######################
# Part 1 - Deal Card #
######################

def deal_card(hand, deck):
    """
    (list,list) -> None

    Deals a card from the first element in the deck list and add it to the list
    representing the player's hand. This function should remove the first card
    from the deck list and append it to hand list.

    Parameters
    ----------
    hand : list
        List representing the player's hand
    deck : list
        List representing the deck of cards
    """
    # To Do: Complete the function

    hand.append(deck[0])
    deck.pop(0)


########################
# Part 2 - Score Cards #
########################

def score_cards(hand):
    """
    (list) -> int

    Calculate the score of the player's hand. The score is the sum of the values
    of the cards in the hand. Number cards are worth their number value, face cards (jack, queen, king)
    are worth 10, and aces are worth 11. If the hand contains an ace and the score
    is greater than 21, the ace should be worth 1 instead of 11.

    Parameters
    ----------
    hand : list
        List representing the player's hand

    Returns
    -------
    int
        The score of the collection of cards in the hand
    """
    # To Do: Complete the function
    score_map = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        '11': 10,
        '12': 10,
        '13': 10,
    }
    
    ace_count = 0
    score_acc = 0
    for card in hand:
        if card[1] == 1:
            ace_count += 1
        else:
            score_acc += score_map[str(card[1])]
    
    if ace_count == 0:
        return score_acc
    else:
        if ace_count == 1:
            if score_acc + 1 >= 21 or (score_acc + 11 > 21 and score_acc + 1 < 21):
                return score_acc + 1
            else:
                return score_acc + 11
        elif ace_count >= 2:
            if score_acc + ace_count >= 21:
                return score_acc + ace_count
            elif score_acc + 12 + (ace_count - 2) <= 21:
                return score_acc + 12 + (ace_count - 2)
            else:
                return score_acc + ace_count * 11



######################
# Part 3 - Play Game #
######################

def play(shuffled_deck):
    """
    (list) -> [str,int,int]

    Play the card game of with the shuffled deck of cards.

    Parameters
    ----------
    shuffled_deck : list
        List representing the shuffled deck of cards

    Returns
    -------
    list
        A list containing the winner of the game, the dealer's score, and the player's score.
        The winner is a string representing the winner of the game ('player' or 'dealer').
        The dealer's score is an integer representing the score of the player's hand.
        The player's score is an integer representing the score of the dealer's hand.
    """

    # define the player and dealer hands
    player_hand = []
    dealer_hand = []

    # To Do: Complete the function
    for i in range(2):
        deal_card(player_hand,shuffled_deck)
        deal_card(dealer_hand, shuffled_deck)
    
    while score_cards(player_hand) < 14:
        deal_card(player_hand, shuffled_deck)
        if score_cards(player_hand) > 21:
            return ["dealer", score_cards(dealer_hand), score_cards(player_hand)]
    
    while score_cards(dealer_hand) < score_cards(player_hand):
        deal_card(dealer_hand, shuffled_deck)
        if score_cards(dealer_hand) > 21:
            return ["player", score_cards(dealer_hand), score_cards(player_hand)]
    
    if score_cards(player_hand) > score_cards(dealer_hand):
        return ["player", score_cards(dealer_hand), score_cards(player_hand)]
    else:
        return ["dealer", score_cards(dealer_hand), score_cards(player_hand)]



