def create_deck():
	deck =[]
	suits = ['C','D','H','S']
	card_val = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
	for suit in suits:
		for card in card_val:
			deck += [card + suit]
	return deck