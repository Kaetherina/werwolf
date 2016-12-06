import registrationLogic
import telegram, logging
from telegram.ext import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

#dispatcher
#dispatcher = updater.dispatcher




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



numOfplayers = 0
wantedSpecialRoles = []
password = None
name = None
specialRoles = ["Amor", "Seherin", "Hexe", "Jaeger"]


def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text ="Bitte teile mir deine Daten mit folgenden Commands mit!")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Deinen Namen mit /myname NAME")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Anzahl der Spieler mit /anzahl ZAHL")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Die Wahl deiner 2 Klassen mit /class KLASSE1 KLASSE2")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Fuer mehr Infos zu den Klassen, benutze /classhelp")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Das Passwort fuer dein Spiel mit /pw PASSWORT")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Sobald du alles eingegeben hast, schreibe bitte /ready")
    bot.sendMessage(chat_id = update.message.chat_id, text ="P.S: Solltest du dich mal vertippt haben, so gebe einen Command einfach erneut ein! :)")
    

# Create the Updater and pass it your bot's token.

def set_name(bot, update, args):
    global name
    name = str(args[0])
    bot.sendMessage(chat_id = update.message.chat_id, text = "Vielen Dank " + name)

def set_anzahl(bot, update, args):  
    global numOfplayers
    numOfplayers = int(args[0])
    bot.sendMessage(chat_id = update.message.chat_id, text="Ok, du spielst mit " + str(args[0]) +" Spielern")

def set_class(bot, update, args):
    global wantedSpecialRoles
    if args[0] != args[1]:
        for i in specialRoles:
            if i == args[0]:
                wantedSpecialRoles.append(i)
            elif i == args[1]:
                wantedSpecialRoles.append(i)
        bot.sendMessage(chat_id = update.message.chat_id, text="Vielen dank, deine Klassen sind: ")
        bot.sendMessage(chat_id = update.message.chat_id, text= wantedSpecialRoles[0] + " und " + wantedSpecialRoles[1])
    else:
        bot.sendMessage(chat_id = update.message.chat_id, text="Falsche Klassen! tippe /classhelp fuer mehr Infos!")

def classhelp(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text="Es gibt folgende Klassen, aus denen du 2 wahlen musst! Achte auf die Schreibweise der Klassen!")
    for i in specialRoles:
        bot.sendMessage(chat_id = update.message.chat_id, text=i)

def set_pw(bot, update, args):
    global password
    password = str(args[0])
    print(password)
    bot.sendMessage(chat_id = update.message.chat_id, text="Vielen Dank, dein Passwort lautet: " + password)

def ready(bot, update):
    if name == None:
        bot.sendMessage(chat_id = update.message.chat_id, text = "Du hast keinen Namen angegeben, tippe /myname NAME")
    elif numOfplayers <= 4:
        bot.sendMessage(chat_id = update.message.chat_id, text = "Spielst du etwa mit weniger als fünf Leuten? Sag uns bitte mit /anzahl ZAHL , mit wie vielen Leuten du spielst! :)")
    elif password == None:
        bot.sendMessage(chat_id = update.message.chat_id, text = "Bitte gebe ein Passwort an. Nutze dafuer /pw PASSWORD")
    else:
        
        bot.sendMessage(chat_id = update.message.chat_id, text = "Vielen Dank, deine Daten wurden uebermittelt! :)")
        registrationLogic.getReady(name, numOfplayers, wantedSpecialRoles, password)


updater = Updater(token = '327185418:AAGrpXhyStp8mpt2AagG18QYeTFMz0AT9PY')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('myname', set_name, pass_args = True))
updater.dispatcher.add_handler(CommandHandler('anzahl', set_anzahl, pass_args = True))
updater.dispatcher.add_handler(CommandHandler('class', set_class, pass_args = True))
updater.dispatcher.add_handler(CommandHandler('classhelp', classhelp))
updater.dispatcher.add_handler(CommandHandler('pw', set_pw, pass_args = True))
updater.dispatcher.add_handler(CommandHandler('ready', ready))

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Ich kenne diesen Befehl nicht! :(")

updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))


#start
updater.start_polling()
