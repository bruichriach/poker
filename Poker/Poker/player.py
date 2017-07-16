import game
 
class Player():
	def __init__(self):
		self.location = 0
	
	def do_action(self, action, **kwargs):
		action_method = getattr(self,action.method.__name__)
		if action_method:
			if action.hotkey == None:
				action_method(**kwargs)
			else:
				action_method(**kwargs)

	def list_actions(self):
		game_state=game.state_exists(self.location)
		available_actions = game_state.available_actions()
		for action in available_actions:
			print(action)

	def exit(self):
		game.run=False

	def new_hand(self):
		self.location = 0
		
	def deal2hand(self):
		self.location = 1

	def hand2flop(self):
		self.location = 2

	def flop2turn(self):
		self.location = 3

	def hand2river(self):
		self.location = 4

	def turn2river(self):
		self.location = 4



