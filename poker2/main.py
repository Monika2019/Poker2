# -*- coding: UTF-8 -*-
#from machine.std_mach import create_deck
from machine.std_mach import create_deck,\
    shuffled_deck,\
    record_deck

# 场景一：
# 拿出一副新牌
first_deck = []
create_deck(first_deck)
record_deck(first_deck, 'deck-001.txt')

shuffled_deck(first_deck)
record_deck(first_deck, 'deck-002.txt')
