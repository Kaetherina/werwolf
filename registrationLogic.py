import time
import random

master = "not set"
allowedRoles = ["Amor", "Seherin", "Hexe", "Jaeger"]
players = []
roles = []
playersRoles = []
numPlayers = 0
pw = "werwolf"


def getReady(name, numOfPlayers, wantedSpecialRoles, password):
	global numPlayers 
	numPlayers = numOfPlayers
	master = name
	print("the master is "+ name)
	if password:
		pw = password
		print("the password was set to "+ password)
	else:
		print("the password remains werwolf")
	players.append(name)

	if not testSpecialRoles(wantedSpecialRoles):
		return False
		print("not all special roles were found.. do some spellcheck")
	global roles
	roles = getAllRoles(numOfPlayers, wantedSpecialRoles)
	print("and these are all the roles: " + str(roles))
	return True

	
def newPlayer(name, inputPassword):
	if inputPassword==pw:
		if name in players:
			return "!name"
		players.append(name)
		print("we currently have these players: "+ str(players))
		print("the length of the array is currently "+ str(len(players)) + "while the number of players is " + str(numPlayers))

		if numPlayers==len(players):
			giveRoles()
			print("got all players now! Proceed to the game")
			return "success"
		return "player added"
	else:
		return "!password"


def testSpecialRoles(specialRoles):
	for i in range(0, len(specialRoles)):
		if allowedRoles.index(specialRoles[i])<0:
			return False
	return True

def getAllRoles(num, specialRoles):
	roles = []
	if num<8:
		numWerwolf = 1
	elif num<13:
		numWerwolf = 2
	elif num<16:
		numWerwolf = 3
	else:
		numWerwolf = int(num/4)
	
	numSpecials = len(specialRoles)
	numBuerger = num - numWerwolf - numSpecials
	
	for i in range(0, num):
		if i<numWerwolf:
			roles.append("Werwolf")
		elif (i-numWerwolf)<numBuerger:
			roles.append("Buerger")
		else:
			roles.append(specialRoles[i-numWerwolf-numBuerger])
	return roles
								
def giveRoles():
	global playersRoles
	global roles
	random.shuffle(roles)
	print(str(playersRoles))
	for i in range(0, len(roles)):
		playersRoles.append([players[i], roles[i]])
	print("go all players and roles now, have a look: " + str(playersRoles))
		
	
def reset(name):
	if name==master:
		players = []
		playersRoles = []
		return True
	else:
		return False
		
	
#playerRoles=[[Kaethe, Werwolf], [Kevin, Schlampe], []]
