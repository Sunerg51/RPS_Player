 # Greg Suner and Alex Ciarmella
 # Concrete Player Class

 class Player:
 
	def __init__(self):
	
	#Decides next move based on opponents past moves
	#For now, assumes a list parameter that has past moves in a "player, opponent, player,..." order
	#Looks for what opponent throws the most and tries to counter it
	#0-rock, 1-paper, 2-scissors
	def play(self, pastmoves):
		rock, paper, scissors = 0
		
		for index, move in enumerate(pastmoves):
			if index % 2 == 1:
				if move == 0:
					rock += 1:
				elif move == 1:
					paper += 1:
				else
					scissors += 1:
		else
			#Not sure how to output a move but for now the first move is just rock since the list is empty
			#Throw rock
		
		#Look for most thrown move and throw counter
		if rock > paper && rock > scissors:
			#Throw paper
		elif paper > rock && paper > scissors:
			#Throw scissors
		elif scissors > rock && scissors > paper:
			#Throw paper
		else
			#Throw scissors
		