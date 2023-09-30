import os
import discord
from dotenv import load_dotenv
from scraper import scrape_live_scores
import csv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

bot = commands.Bot

def handle_message_repsonse(message) -> str:
    if message=='/livescore':
        async def live_score(ctx):
            try:
                live_data = scrape_live_scores()
                response = (
                    f"Team 1: {live_data['team1']}\n"
                    f"Team 2: {live_data['team2']}\n"
                    f"Livescore: {live_data['livescore']}"
                )
                await ctx.send(response)
            except Exception as e:
                await ctx.send("No live scores available! Try again later.")

    if message=='/generate':
        async def generate_csv(ctx):
            with open('liveScores.csv', 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    print(row)  

    if message=='/help':
        async def bot_help(ctx):
            help_message = (
                "Commands:\n"
                "/livescore - get the live scores\n"
                "/generate - get the csv file the livescores are stored ini\n"
            )  
            await ctx.send(help_message)

bot.run(TOKEN)
