 # Greg Suner and Alex Ciarmella
 # Concrete Player Class

 class GSACPlayer(Player.Player):
 
	def __init__(self):
		self.name - None
	#Decides next move based on opponents past moves
	#Looks for what opponent throws the most and tries to counter it. 0-rock, 1-paper, 2-scissors
	#Takes list of opponents past moves
	def play(self, pastmoves):
		rock, paper, scissors = 0
		
		for index, move in enumerate(pastmoves):

				if move == 0:
					rock += 1
				elif move == 1:
					paper += 1
				else
					scissors += 1
		else
			return 0
		
		#Look for most thrown move and throw counter
		if rock > paper && rock > scissors:
			return 0
		elif paper > rock && paper > scissors:
			return 2
		elif scissors > rock && scissors > paper:
			return 1
		else #Arbitrary throw if 2 or 3 are thrown evenly
			return 0
			
	def get_name(self)
		return self.name
		
	def set_name (self, playername):
		self.name = playername