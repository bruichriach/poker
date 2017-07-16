_game = {}
run=True
starting_position = 0

def load_game():
	_game[0]=getattr(__import__('locations'), "deal")()
	_game[1]=getattr(__import__('locations'), "preflop")()
	_game[2]=getattr(__import__('locations'), "flop")()
	_game[3]=getattr(__import__('locations'), "turn")()
	_game[4]=getattr(__import__('locations'), "river")()

def state_exists(x):
    return _game.get(x)