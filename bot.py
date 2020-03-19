from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters



TG_TOKEN="1104975397:AAGsoIfqQqMInkL-ATs8nBp66JX8no8PK5E"


def message_handler(bot: Bot, updatet: Update):
    user = update.effective_user
    if user:
        name=user.first_name
    else:
        name='anonim'




    text = update.effective_message.text
    reply_text = f'Privet, {name}!\n\n{text}'


    bot.send_massage(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )
    

def main():
    bot=Bot(
        token=TG_TOKEN,
    )
    updater=Updater(
        bot=bot,
    )

    
   handler=MessageHandler(Filters.all, message_handler)
   updater.dispatcher.add_handler(handler)

   updater.start_polling()
   updater.idle()

if _name_ == '_main_':
    main()
    





    
