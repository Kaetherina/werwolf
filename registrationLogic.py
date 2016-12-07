# -*- coding: utf-8 -*-

import time
import random
import logging

master = "not set"
allowedRoles = ["Amor", "Seherin", "Hexe", "Jaeger"]
players = []
roles = []
playersRoles = []
specialRoles = []
numPlayers = 0
pw = "werwolf"

def setMaster(name):
	global players
	global master 
	master = name
	players.append(name)
	print("the master is set to \""+name+"\"")
def setPassword(password):
	global pw
	pw = password
	print("the password was set to \"" + password +"\"")
def getPassword():
	return pw
def setNumOfPlayers(numOfPlayers):
	global numPlayers
	numPlayers = numOfPlayers
	print("The number of players is "+ numPlayers)
def setSpecialRoles(wantedSpecialRoles):
	global roles
	if testSpecialRoles(wantedSpecialRoles):
		global specialRoles 
		specialRoles= wantedSpecialRoles
		roles = getAllRoles(numPlayers, wantedSpecialRoles)
		print("These are all the possible roles: "+ str(roles))
		return roles
	else:
		print("not all special roles were found.. do some spellcheck")
		return False

def testSpecialRoles(specialRoles):
	temp = -1
	for i in range(0, len(specialRoles)):
		if allowedRoles.index(specialRoles[i])<0:
			return False
	return True
def getAllRoles(num, specialRoles):
	global roles
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

def ready():
	if master == "not set":
		return "master"
	elif numPlayers <5:
		return "players"
	elif len(specialRoles) == 0:
		return "roles"
	else:
		return "ready"


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
