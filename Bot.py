# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands

bot = commands.Bot(
# set up the bot
token=os.environ['TMI_TOKEN'],
client_id=os.environ['CLIENT_ID'],
nick=os.environ['BOT_NICK'],
prefix=os.environ['BOT_PREFIX'],
initial_channels=[os.environ['CHANNEL']]
)

# bot.py, below bot object
@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws #this is only needed to send messages within event_ready
    await ws.sendprivmsg(os.environ['CHANNEL'], f"/me has landed!")

#bot.py
if __name__ == "__MAIN__":
    bot.run()