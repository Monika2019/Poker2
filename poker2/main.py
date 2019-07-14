# -*- coding: UTF-8 -*-
from machine.std_mach import create_deck,\
    shuffled_deck,\
    record_deck
from dealer.mike import deal_to_a_player, deal_to_multi_players
# 场景一：
# 拿出一副新牌
first_deck = []
create_deck(first_deck)
record_deck(first_deck, 'deck-001.txt')

shuffled_deck(first_deck)
record_deck(first_deck, 'deck-002.txt')
'''
#场景二：
_deck = []
deal_to_a_player(first_deck,5,Monika_deck)
record_deck(Monika_deck,'Monika_deck.txt')

Monika1_deck = []
deal_to_a_player(first_deck,5,Monika1_deck)
record_deck(Monika1_deck,'1_deck.txt')
'''
# 场景三
Monika_deck = []
Monika1_deck = []

deal_to_multi_players(first_deck, Monika_deck, Monika1_deck)
record_deck(Monika_deck, 'Monika_deck.txt')
record_deck(Monika1_deck, '1_deck.txt')
