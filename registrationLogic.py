import time
import math

master
allowedRoles[Amor, Seherin, Hexe, Jaeger]
players = []
playersRoles = []
pw = werwolf


def getReady(name, numOfPlayers, wantedSpecialRoles, password):
	master = name
	if not password:
		pw = password
	if not testSpecialRoles(wantedSpecialRoles):
		return False
	roles = getAllRoles(numOfPlayers, wantedSpecialRoles)
	while not numOfPlayers==len(players)
		time.sleep(5)
	giveRoles(roles[])
	return True

	
def newPlayer(name, inutPassword):
	if inputPassword==pw:
		if(players.index(name)>0):
			return False
		players = players.append(name)
		return True
	else:
		return False


def testSpecialRoles(specialRoles[]):
	for i in range(0, len(specialRoles)):
		if allowedRoles.index(specialRoles[i])<0
			return False
	return true

def getAllRoles(num, specialRoles[]):
	if num<8:
		numWerwolf = 1
	elif num<13:
		numWerwolf = 2
	elif num<16
		numWerwolf = 3
	else:
		numWerwolf = int(num/4)
	
	numSpecials = len(specialRoles)
	numBuerger = num - numWerwolf - numSpecials
	
	for i in range(0, num):
		if i<numWerwolf:
			roles[i]= "Werwolf"
		elif (i-numWerwolf)<numBuerger:
			roles[i]="Buerger"
		else:
			roles[i]=specialRoles[i-numWerwolf-numBuerger]
								
def giveRoles(roles[]):
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