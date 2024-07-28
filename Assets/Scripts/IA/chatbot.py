from rivescript import RiveScript

def initialize_bot():
    bot = RiveScript()
    bot.load_file('./ejemplo.rive')  # Cargar los archivos RiveScript
    bot.sort_replies()  # Procesar las respuestas
    return bot

def get_bot_response(bot, message):
    reply = bot.reply("localuser", message)
    return reply

if __name__ == "__main__":
    bot = initialize_bot()
    while True:
        msg = input('You> ')
        if msg == '/quit':
            quit()
        reply = get_bot_response(bot, msg)
        print('Bot> ' + str(reply))
