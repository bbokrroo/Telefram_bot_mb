
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

BOT_TOKEN = "7651320880:AAGRNYTRyuwK5m7uqbSD5SG9nnjWcrDtgjs"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

GREETING_MESSAGES = [
    "🌸 Вітаю, {name}! Твоя малина вже тут 😉",
    "💞 Привіт, {name}! Роздягайся… тобто, розслабляйся 😁",
    "🍓 Хей, {name}! Тут тобі точно сподобається!",
    "❤️‍🔥 {name}, вітаю в групі кохання і мемів!"
]

import random

async def greet_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        name = member.full_name
        message = random.choice(GREETING_MESSAGES).format(name=name)
        await context.bot.send_message(chat_id=update.chat_member.chat.id, text=message)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    handler = ChatMemberHandler(greet_new_member, ChatMemberHandler.CHAT_MEMBER)
    app.add_handler(handler)
    app.run_polling()
