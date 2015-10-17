#Game of War Player vs. Computer/Dealer modified version
#Player vs. Dealer high card wins and player bets in denominations of $5 starting with $100.
#If PlayersCard=DealersCard then go to war and additional betting may occur if player has enough money.
#End of game is that 10 points has been reached or myCash<=0 or player types a key to exit
import random
myCash = 100

#Function that runs the game 
def playGame():
	global myCash
	dealersPoints = 0
	myPoints = 0
	name=startGame()

	while (gameOver(dealersPoints, myPoints,name, myCash) !=True):
			# endGame(dealersPoints, myPoints)
			test = playRound(dealersPoints, myPoints,0,myBet)
			# print "test: ", test
			dealersPoints = test["dealersPoints"]
			myPoints = test["myPoints"]

	# else:
		# playRound(dealersPoints, myPoints)

#Functions to play game

def startGame():
	#insert audio here "Would you like to play a game?" a la Wargames
	name = raw_input ("What is your name? ")
	print "Hello,", name, "let's play War! High card wins each round."
	print "Your goal is to win 10 rounds and make smart bets without going bankrupt."
	print "Minimum bet is $5 and your bets must be in $5 denominations."
	print " "
	print "If we both have the same card, we go to War."
	print "At that point, you may double your bet or else you surrender that bet."
	print "Ok", name, "let's play!"
	global myCash
	myCash = 100
	return name

def playRound(dealersPoints, myPoints,bet,myBet):
	global myCash
	dealersPoints = dealersPoints
	myPoints = myPoints
	print "You currently have %d to bet." % myCash
	if bet == 0:
		myBet = getBet(myCash)
	else:
		myBet = bet
	cards = {14:"Ace",13:"King",12:"Queen",11:"Jack",10:"10", 9:"9", 8:"8", 7:"7",6:"6",5:"5",4:"4",3:"3",2:"2"}
	dealerRandom=random.randrange(2,15)
	userRandom=random.randrange(2,15)
	dealersCard = cards [dealerRandom]
	myCard=cards[userRandom]
	print "================================"
	print "								"
	print " _________         _________"
	print "|         |       |         |"
	print "|         |       |         |"
	print "|         |       |         |"
	print "| %-5s   |       | %-5s   |" %(dealersCard,myCard)
	print "|         |       |         |"
	print "|_________|       |_________|"
	print "								"
	print "Dealer's card     Your card",
	print "                             "
	# print "The dealer's card is: ", dealersCard
	# print "Your card is: ", myCard


	if dealersCard>myCard:
		print "Dealer wins this point, sorry!"
		dealersPoints+=1
		myCash-=myBet

	elif dealersCard<myCard:
		print "You win this point, yay!"
		myPoints+=1
		myCash+=myBet
	
	else:
		GotoWar(dealersPoints,myPoints,myBet,myCash)
	return {"myPoints": myPoints, "dealersPoints": dealersPoints}

def IsthereaWinner (dealersPoints, myPoints, name):
	print "Dealer's Points: ", dealersPoints
	print name,"'s Points: ", myPoints
	return dealersPoints == 10 or myPoints ==10

def gameOver(dealersPoints, myPoints, name, myCash):
	#End of game is that 10 points has been reached or myCash<=0 or player types a key to exit
	if myPoints ==10:
		print name, "you are the big winner this time!! Play again!!"
		print name, "You end this game with $%d" %myCash
	elif dealersPoints ==10:
		print "Sorry, dealer wins! Better luck next time!"
		print name, "You end this game with $%d" %myCash
	return IsthereaWinner(dealersPoints, myPoints, name)
#create a file to keep track of overall reigning high score, eventually can indicate whose score by initials

def getBet(myCash):
	myBet = int(raw_input("Enter your bet in denominations of $5 please."))
	if myBet %5 ==0 and myBet<=myCash:
		myCash-=myBet
		return myBet
	else:
		print "Please place a proper bet!"
		return getBet()
	
def GotoWar(dealersPoints,myPoints,myCash,myBet):
	GotoWar = raw_input("Go to War? Type yes if you are ready to double your bet!") #(Go to War? Type yes or No)
		# another option in the future is to surrender half your bet
	if GotoWar == "No" or GotoWar == "no":
		myCash-=myBet
		print "Sorry you can't go to war, surrender your original bet!"
			# check user has enough $ to double bet
	if myCash>=myBet*2: 
		myBet+=myBet
		myCash-=myBet
		print "									"
		print "Now your new bet is", myBet
		print "Discarding cards..."
		for x in range(1,4):
			print x	
	# do countdown and pick cards and winner
		playRound(dealersPoints, myPoints,myBet)

	# return (something that tells who the winner is)
	else:
		print "you don't have enough to go to war, Sorry!"
	
#run the game by calling playGame
playGame()