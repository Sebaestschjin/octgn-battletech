Discard = "Scrapheap"

def scrap_card(card):
    mute()
    card.moveTo(me.piles[Discard])
    notify("{} scraps {}.".format(me, card))


def scrap_card_at_random(group, x=0, y=0):
    mute()
    card = group.random()
    if card is None:
        return
    card.moveTo(me.piles[Discard])
    notify("{} randomly scraps {}.".format(me, card))
