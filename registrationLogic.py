import time
import math

master = "not set"
allowedRoles = ["Amor", "Seherin", "Hexe", "Jaeger"]
players = []
playersRoles = []
pw = "werwolf"


def getReady(name, numOfPlayers, wantedSpecialRoles, password):
	master = name
	print("the master is "+ name)
	if not password:
		pw = password
	print("the password is set to "+ password)
	if not testSpecialRoles(wantedSpecialRoles):
		return False
		print("not all special roles were found.. do some spellcheck")
	roles = getAllRoles(numOfPlayers, wantedSpecialRoles)
	print("and these are all the roles: " + str(roles))
	while not numOfPlayers==len(players):
		time.sleep(5)
	giveRoles(roles)
	return True

	
def newPlayer(name, inutPassword):
	if inputPassword==pw:
		if(players.index(name)>0):
			return False
		players = players.append(name)
		return True
	else:
		return False


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
								
def giveRoles(roles):
	for i in range(0, roles.length):
		playersRoles[i][0] = players[i]
		playersRoles[i][1] = roles[i]
		
	
def reset(name):
	if name==master:
		players = []
		playersRoles = []
		return True
	else:
		return False
		
	
#playerRoles=[[Kaethe, Werwolf], [Kevin, Schlampe], []]
