card_val = {'A':11,'K':10,'Q':10,'J':10,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
def eval(hand):
	score = 0
	aces  = 0
	for card in hand:
		score += card_val[card[0]]
		if(card[0] == 'A'):
			aces += 1
			if(score > 21 and aces > 0):
				score -= 10
				aces -= 1
	return score