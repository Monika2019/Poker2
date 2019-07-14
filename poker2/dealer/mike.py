# -*- coding: UTF-8 -*-

def deal_to_a_player(aDeck,num,player_cards):
    'Desc: Deal some cards to a play1er from a deck'

    for i in range(num):
        picked_card = random.choice(aDeck)
        player_cards.append(picked_card)
        aDeck.remove(picked_card)
    # print('\# NOTE: ==debug1: %s' % (player_cards))
    player_cards.sort()
    
    return
