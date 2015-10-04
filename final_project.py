#War vs. Computer
#Create a dictionary assigning values for cards in order
#End of game is winner reaches 10 points or types exit
goal = 10
dealersPoints = 0
myPoints = 0
cards = {14:"Ace",13:"King",12:"Queen",11:"Jack",10:"10", 9:"9", 8:"8", 7:"7",6:"6",5:"5",4:"4",3:"3",2:"2"}
#switch the dictionary placement of the values above AS PER AHMAD meeting
#Can have it ask name
#Ready to play?
#Need pseudo random generator here
def main_function():
	dealersCard=random.randrange(2,15)
	myCard=random.randrange(2,15)
	dealersCard = cards [dealerRandom]
	print "The dealer's card is: ", dealersCard
	myCard=cards[userRandom]
	print "Your card is: ", myCard
	if dealersCard>myCard:
			dealersPoints+=1
	if dealersCard<myCard:
			myPoints+=1
	if dealersCard == myCard:
		print "Go to War"
#def Checkwinner():
def CheckWinner (dealersPoints,myPoints):
	if dealersPoints == 10:
		print "Dealer wins, better luck next time!"
	elif myPoints == 10:
		print " You are the big winner!"
# if war occurs
def war():
	print "shuffling"
	#countdown - 3 2 1 iteration
	dealerBattlecard = random
	userBattlecard = random
		if myBattlecard>dealerBattlecard


		print "You win this battle"
	else:
		print "Try again!"

#optional betting component - start with $100 then bet in increments of $5
#tally high score after 10 points or else game over if busts out of money
#beyond optional: keep track of reigning high score 




