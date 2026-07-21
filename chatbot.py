from colorama import init
from banner import show_banner
from colors import USER, BOT

from responses import get_response
from utils import current_date, current_time

init(autoreset=True)

show_banner()

name = input(USER + "👤 Enter Your Name: ")
print(BOT + f"🤖 Welcome {name}! 😊")
history = open("chat_history.txt", "a")
while True:
    user = input(USER + "\n👤 You: ").lower()
    history.write("You: " + user + "\n")

    if user == "date":
        print(BOT + "📅 Today's Date:", current_date())
        continue

    if user == "time":
        print(BOT + "🕒 Current Time:", current_time())
        continue

    reply = get_response(user)

    if reply == "exit":
        print(BOT + "🤖 Bot: Thank you for using Rule-Based AI Chatbot.")
        history.close()
        break

    print(BOT + "🤖 Bot:", reply)
    history.write("Bot: " + reply + "\n\n")