import actions


class State:
	def intro_text(self):
		raise NotImplementedError()

	def data_output(self):
		raise NotImplementedError()

	def available_actions(self):
		return [actions.Help(),actions.Restart(),actions.Exit()]
		

class deal(State):
	def available_actions(self):
		return [actions.Help(),actions.Restart(),actions.Exit(),actions.Deal2Hand()]

	def intro_text(self):
		return """
		Please enter a starting hand."""

	def data_output(self):
		return

class preflop(State):
	def available_actions(self):
		return [actions.Help(),actions.Restart(),actions.Exit(),actions.Hand2Flop(),actions.Hand2River()]

	def intro_text(self):
		return """
		Please enter the flop or all table cards."""

	def data_output(self):
		print("""
		Here is the hand data""")

class flop(State):
	def available_actions(self):
		return [actions.Help(),actions.Restart(),actions.Exit(),actions.Flop2Turn()]

	def intro_text(self):
		return """
		Please enter the turn card."""

	def data_output(self):
		print("""
		Here is the Flop data""")

class turn(State):
	def available_actions(self):
		return [actions.Help(),actions.Restart(),actions.Exit(),actions.Turn2River()]

	def intro_text(self):
		return """
		Please enter the river card."""

	def data_output(self):
		print("""
		Here is the Turn data""")

		
class river(State):
	def available_actions(self):
		return [actions.Help(),actions.Exit()]
	
	def data_output(self):
		print("""
		Here is the River data""")
