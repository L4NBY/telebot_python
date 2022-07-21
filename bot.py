@bot.message_handler(content_types=['new_chat_members'])
def new_member(message):
    p = bot.reply_to(message, 'Bem vindo, ' + " ao grupo **" + message.chat.title + "** 🎉",parse_mode="Markdown")
    sleep(15)
    bot.delete_message(message.chat.id , p.id)
    k = bot.reply_to(message, f'você tem algum talento em programação ou algo do tipo ? ',parse_mode="Markdown")
    sleep(15)
    bot.delete_message(message.chat.id , k.id)
