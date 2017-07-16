from player import Player
		

class Action():
	def __init__(self, method, name, hotkey, reqlen, **kwargs):
		self.method = method
		self.hotkey = hotkey
		self.name = name
		self.reqlen = reqlen
		self.kwargs = kwargs

	def __str__(self):
		if self.hotkey == None:
			return "Enter {} cards".format(self.reqlen)
		else:
			return "{}: {}".format(self.hotkey, self.name)

class Help(Action):
    def __init__(self):
        super().__init__(method=Player.list_actions, name='Help', hotkey='h', reqlen=None)

class Restart(Action):
    def __init__(self):
        super().__init__(method=Player.new_hand, name='Start New Hand', hotkey='r', reqlen=None)

class Exit(Action):
    def __init__(self):
        super().__init__(method=Player.exit, name='Exit', hotkey='x', reqlen=None)

class Deal2Hand(Action):
    def __init__(self):
        super().__init__(method=Player.deal2hand, name='Enter Hand', hotkey=None, reqlen=2)

class Hand2Flop(Action):
    def __init__(self):
        super().__init__(method=Player.hand2flop, name='Enter Flop', hotkey=None, reqlen=3)

class Flop2Turn(Action):
    def __init__(self):
        super().__init__(method=Player.flop2turn, name='Enter Turn Card', hotkey=None, reqlen=1)

class Turn2River(Action):
    def __init__(self):
        super().__init__(method=Player.turn2river, name='Enter River Card', hotkey=None, reqlen=1)

class Hand2River(Action):
    def __init__(self):
        super().__init__(method=Player.hand2river, name='Enter Table Cards', hotkey=None, reqlen=5)