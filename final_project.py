#War vs. Computer
#Player vs. Dealer high card in bets denomination of $5 beginning with $100.
#If PlayersCard=DealersCard then go to war and additional betting may occur if player has enough money.
#End of game is that 10 points has been reached or myCash<=0 or player types a key to exit
import random
dealersPoints = 0
myPoints = 0
name = raw_input ("What is your name? ")
print "Hello,",name, "let's play war!"
myCash = 100 
# running tally of myCash and exit game if myCash<=0 
def myBet ():
	myBet = int(raw_input ("You have $100 to start, minimum bet is $5. Place your bet in any increment of 5. "))
		if myBet>myCash:
			print "Sorry, you don't have enough money, place another bet?"	

def isdivisibleby5(number):
	return number %5==0
def IsthereaWinner ():
	return dealersPoints == 10 or myPoints ==10
def dealerWin (dealersCard,myCard,dealersPoints,myPoints,myCash,myBet):
	if dealersCard>myCard:
		print "Dealer wins this point, sorry!"
	dealersPoints+=1
	myCash-=myBet
	return myCash
def userWin(dealersCard,myCard,dealersPoints,myPoints,myCash,myBet):
	if dealersCard<myCard:
		print "You win this point, yay!"
	myPoints+=1
	myCash+=myBet
	return myCash
def gotoWar(dealersCard,myCard,dealersPoints,myPoints,myCash,myBet):
	if dealersCard == myCard:
		myBetWar = int(raw_input ("If you are ready, double your bet!"))
	myBet+=myBet
	return myBet
# print "Dealer wins, better luck next time!"
# print " You are the big winner!"
cards = {14:"Ace",13:"King",12:"Queen",11:"Jack",10:"10", 9:"9", 8:"8", 7:"7",6:"6",5:"5",4:"4",3:"3",2:"2"}
def PlayRound():
	dealerRandom=random.randrange(2,15)
	userRandom=random.randrange(2,15)
	dealersCard = cards [dealerRandom]
	print "The dealer's card is: ", dealersCard
	myCard=cards[userRandom]
	print "Your card is: ", myCard
	winningconditions
	

	if dealerRandom > userRandom:
		dealerWin
	elif userRandom > dealerRandom:
		userWin
	else:
		GotoWar()
#

	dealerWin (dealerRandom,userRandom,dealersPoints,myPoints,myCash,myBet):
		print myCash, "is what you have left to bet."
		myBet = int(raw_input ("Minimum bet is $5. Place your bet in any increment of 5. "))
	elif userWin (dealerRandom,userRandom,dealersPoints,myPoints,myCash,myBet):
		print myCash, "is what you have left to bet."
		myBet = int(raw_input ("Minimum bet is $5. Place your bet in any increment of 5. "))
	else: 
		GotoWar = raw_input("Go to War?") #(Go to War? Type yes or No to surrender half your bet)
		myBetWar = int(raw_input ("If you are ready, double your bet!"))
		myBet+=myBet

	# if dealersCard>myCard:
	# 	print "Dealer wins this point, sorry!"
	# 	dealersPoints+=1
	# 	myCash-=myBet
	# 	print myCash, "is what you have left to bet."
	# 	myBet = int(raw_input ("Minimum bet is $5. Place your bet in any increment of 5. "))
	# if dealersCard<myCard:
	# 	print "You win this point, yay!"
	# 	myPoints+=1
	# 	myCash+=myBet
	# 	print myCash, "is what you have left to bet."
	# 	myBet = int(raw_input ("Minimum bet is $5. Place your bet in any increment of 5. "))
	# if dealersCard == myCard:
	# 	GotoWar = raw_input("Go to War?") #(Go to War? Type yes or No to surrender half your bet)
		# myBetWar = int(raw_input ("If you are ready, double your bet!"))
		# myBet+=myBet
def countup(count2):
	if(count2 == 4):
		print "Shuffling"
	else:
		print count2
		countup(count2 +1)
countup(1)

IsthereaWinner(dealersPoints,myPoints)
# def war()
# option: if player types no and chooses to surrender then take half of myBet and subtract it from myCash
# countdown - 3 2 1 iteration while shuffling

# 	dealerBattlecard = random
# 	userBattlecard = random
# 		if myBattlecard>dealerBattlecard
# 		print "You win this battle"
# 	else:
# 		print "Try again!"

#exit the game with a key press 
#tally high score after 10 points or else game over if busts out of money
#beyond optional: keep track of reigning high score 



def dealerWin (dealersCard,myCard,dealersPoints,myPoints,myCash,myBet):
	if dealersCard>myCard:
		print "Dealer wins this point, sorry!"
	dealersPoints+=1
	myCash-=myBet
	return myCash
def userWin(dealersCard,myCard,dealersPoints,myPoints,myCash,myBet):
	if dealersCard<myCard:
		print "You win this point, yay!"
	myPoints+=1
	myCash+=myBet
	return myCash
def gotoWar(dealersCard,myCard,dealersPoints,myPoints,myCash,myBet):
	if dealersCard == myCard:
		myBetWar = int(raw_input ("If you are ready, double your bet!"))
	myBet+=myBet
	return myBet
+++++++
'''
def winningconditions(dealersCard, mycard, dealrepoint, mypoint, myCash, myBet):
	if d < U:
		dealersPoints+=1
	myCash-=myBet
	return
    elif d>u: return
else: (gotowar condition)

'''
S