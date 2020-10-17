DamageMarker = ('Damage', '6d9eb2c3-698c-4386-ad16-3d19e2b61661')
ConstructionMarker = ('Construction', 'e43de45b-a83a-4455-bac9-95276c57d5a9')
OtherMarker = ('Other', 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee')
HighlightColor = "#ff0000"


def add_damage(card, x=0, y=0):
    add_marker(card, DamageMarker)


def add_construction(card, x=0, y=0):
    add_marker(card, ConstructionMarker)


def add_other(card, x=0, y=0):
    add_marker(card, OtherMarker)


def remove_damage(card, x=0, y=0):
    remove_marker(card, DamageMarker)


def remove_construction(card, x=0, y=0):
    remove_marker(card, ConstructionMarker)


def remove_other(card, x=0, y=0):
    remove_marker(card, OtherMarker)


def add_marker(card, marker):
    mute()
    name = marker[0]
    card.markers[marker] += 1
    notify("{} adds a {} to {}.".format(me, name, card))


def remove_marker(card, marker):
    mute()
    name = marker[0]
    if card.markers[marker] < 1:
        return
    card.markers[marker] -= 1
    notify("{} removes a {} from {}.".format(me, name, card))


def tap_card(card, x=0, y=0):
    mute()
    if card.orientation == Rot180:
        notify('{} reloads {}'.format(me, card))
        card.orientation = Rot90
    elif card.orientation == Rot90:
        notify('{} untaps {}'.format(me, card))
        card.orientation = Rot0
    else:
        notify('{} taps {}'.format(me, card))
        card.orientation = Rot90


def deplete_card(card, x=0, y=0):
    mute()
    if card.orientation == Rot180:
        notify('{} reloads {}'.format(me, card))
        card.orientation = Rot0
    else:
        notify('{} depletes {}'.format(me, card))
        card.orientation = Rot180


def deplete_card_name(card, x=0, y=0):
    mute()
    if card[0].orientation == Rot180:
        return "Reload"
    return "Deplete"


def flip_cards(cards, x=0, y=0):
    mute()
    for card in cards:
        if card.isFaceUp:
            notify("{} flips {} face down.".format(me, card))
            card.isFaceUp = False
        else:
            card.isFaceUp = True
            notify("{} flips {} face up.".format(me, card))


def highlight_cards(cards, x=0, y=0):
    mute()
    for card in cards:
        if card.highlight == HighlightColor:
            card.highlight = None
            notify('{} removes highlight from {}'.format(me, card))
        else:
            card.highlight = HighlightColor
            notify('{} highlights {}'.format(me, card))


def flip_coin(group, x=0, y=0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("{} flips heads.".format(me))
    else:
        notify("{} flips tails.".format(me))


def roll_d6(group, x=0, y=0):
    mute()
    n = rnd(1, 6)
    notify("{} rolls {} on a 6-sided die.".format(me, n))
