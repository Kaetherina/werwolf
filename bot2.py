import registrationLogic
import telegram, logging
from telegram.ext import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

#dispatcher
#dispatcher = updater.dispatcher


masterReady = False
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text ="Hi, das hier ist unser Werwolf Spiel!")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Wenn du der Spielmaster bist, gib jetzt /master ein, sonst /spieler")


def master(bot, update, args):
    bot.sendMessage(chat_id = update.message.chat_id, text ="Perfekt, direkt beim Spielmaster! Bitte gibt uns mit den folgenden Commands wichtige Infos:")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Deinen Namen mit /mastername NAME")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Anzahl der Spieler mit /anzahl ZAHL")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Die Wahl so vieler Klassen wie du möchtest mit /class KLASSE1 KLASSE2")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Fuer mehr Infos zu den Klassen, benutze /classhelp")
    bot.sendMessage(chat_id = update.message.chat_id, text ="Das Passwort fuer dein Spiel mit /pw PASSWORT")
    bot.sendMessage(chat_id = update.message.chat_id, text ="..alternativ kannst du dieses Kommando auslassen und das Passwort bleibt \"werwolf\"")    
    bot.sendMessage(chat_id = update.message.chat_id, text ="Sobald du alles eingegeben hast, schreibe bitte /ready")
    bot.sendMessage(chat_id = update.message.chat_id, text ="P.S: Solltest du dich mal vertippt haben, so gebe einen Command einfach erneut ein! :)")

def set_master_name(bot, update, args):
    registrationLogic.setMaster(str(args[0]))
    bot.sendMessage(chat_id = update.message.chat_id, text = "Vielen Dank " + name +", du bist der Spielmaster ")
def set_anzahl(bot, update, args):
    num = int(args[0]) 
    if num<4:
        bot.sendMessage(chat_id = update.message.chat_id, text="Es können nur 5 oder mehr mitspielen - bitte gibt die Spieleranzahl erneut ein.")
    else:
        registrationLogic.setNumOfPlayers(int(args[0]))
        bot.sendMessage(chat_id = update.message.chat_id, text="Ok, du spielst mit " + num +" Spielern")
def set_class(bot, update, args):
    roles = registrationLogic.setSpecialRoles(args) #gibt bei Fehler False zurück und wenn es passt das feld roles[]   
    if bool == False:
        bot.sendMessage(chat_id = update.message.chat_id, text="Falsche Klassen! tippe /classhelp fuer mehr Infos!")
    else:
        bot.sendMessage(chat_id = update.message.chat_id, text="Vielen dank, die verfügbaren Klassen sind: " + str(roles))
def set_pw(bot, update, args):
    registrationLogic.setPassword(str(args[0]))
    bot.sendMessage(chat_id = update.message.chat_id, text="Vielen Dank, dein Passwort lautet: " + password)
def ready(bot, update):
    ready = registrationLogic.ready()

    if ready=="master":
        bot.sendMessage(chat_id = update.message.chat_id, text = "Bitte gib noch deinen Namen ein mit /mastername NAME")
    elif ready == "players":
        bot.sendMessage(chat_id = update.message.chat_id, text = "Die Spielerzahl passt noch nicht, bitte gib eine Zahl über 4 ein mit /anzahl ZAHL")
    elif ready == "roles":
        bot.sendMessage(chat_id = update.message.chat_id, text = "Du hast keine Sonderrollen ausgewählt, also spielt ihr ohne Amor, Seherin, Hexe und Jaeger")
    elif ready == "ready":
        bot.sendMessage(chat_id = update.message.chat_id, text = "Super! Jetzt können sich die anderen Spieler anmelden, das verwendete Passwort ist "+ registrationLogic.getpw())
        gameReady = True
    else:
        bot.sendMessage(chat_id = update.message.chat_id, text = "some internal failure")
def classhelp(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text="Es gibt die Klassen Amor, Seherin, Hexe und Jaeger. Achte bitte auf die Schreibweise der Klassen!") 


def spieler(bot,update,args):
    if masterReady:

    else:
        bot.sendMessage(chat_id = update.message.chat_id, text ="Bitte warte bis euer Spielmaster alle nötigen Daten eingetragen hat!")
        bot.sendMessage(chat_id = update.message.chat_id, text ="Gib, sobald er fertig ist nochmal /spieler ein")
# Create the Updater and pass it your bot's token.


updater = Updater(token = '327185418:AAGrpXhyStp8mpt2AagG18QYeTFMz0AT9PY')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('master', master))
updater.dispatcher.add_handler(CommandHandler('spieler', spieler))

updater.dispatcher.add_handler(CommandHandler('mastername', set_master_name, pass_args = True))
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