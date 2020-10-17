Table = 'Table'
Hand = 'Hand'
Stockpile = 'Stockpile'


def hide_moved_cards(args):
    for i in range(len(args.cards)):
        card = args.cards[i]
        from_group = args.fromGroups[i]
        to_group = args.toGroups[i]

        if from_group.name in [Hand, Stockpile] and to_group.name == Table:
            card.isFaceUp = False
