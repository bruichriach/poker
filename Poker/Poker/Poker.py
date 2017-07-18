import actions
from player import Player
import game

class Card:
	"""The Card Class"""
	def __init__(self, *arg):
		if len(arg) == 1:
			if len(arg[0]) >= 2:
				self.rank=arg[0][0]
				self.suit=arg[0][1]
				self.name=self.rank+self.suit
			else:
				raise Exception("Incorrect input length on card constructor")
		elif len(arg) == 2:
			self.rank=arg[0]
			self.suit=arg[1]
			self.name=self.rank+self.suit
		else:
			raise Exception("Incorrect number of inputs on card constructor")

	@property
	def rank(self):
		return self._rank

	@rank.setter
	def rank(self, d):
		if d in ranks:
			self._rank = d
		else:
			raise Exception("Invalid rank")

	@property
	def suit(self):
		return self._suit

	@suit.setter
	def suit(self, d):
		if d in suits:
			self._suit = d
		else:
			raise Exception("Invalid suit")

	def __str__(self):
		return "{}\n".format(self.name)


 

ranks=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
suits=["h","c","d","s"]

for a in ranks:
	for b in suits:
		print(Card(a+b))

def camel_case(message):
    new_message=""
    for a in range(0,len(message),2):
        new_message += message[a].upper()
        new_message += message[a+1].lower()
    return new_message
        
def valid_cards(hand):
    if (2*(len(hand)/2)==len(hand)):
        for a in range(0,len(hand),2):
            for b in range(0,a,2):
                if (hand[a:a+2] == hand[b:b+2]):
                    return False
            for b in range(0,4):
                if (hand[a+1] == suits[b]):
                    break
                if (b == 3):
                    return False
            for b in range(0,13):
                if (hand[a] == ranks[b]):
                    break
                if (b == 12):
                    return False
        return True
    else:
        return False

game.load_game()
player = Player()
game_state=game.state_exists(player.location)
while game.run:
	action_input = input(game_state.intro_text())
	for action in game_state.available_actions():
		if action_input == action.hotkey:
			player.do_action(action, **action.kwargs)
			break
		if action.reqlen != None:
			if len(action_input) == 2*action.reqlen:
				action_input=camel_case(action_input)
				if valid_cards(action_input):
					player.do_action(action, **action.kwargs)
				break
	game_state=game.state_exists(player.location)
	game_state.data_output()
	if player.location == 4:
		player.location = 0
		game_state=game.state_exists(player.location)

