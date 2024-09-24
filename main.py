import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

TOKEN = os.getenv('DISCORD_TOKEN')  # Now it uses an environment variable

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def post_job(ctx, *, job_description):
    with open('internJobListings.txt', 'a') as f:
        f.write(f"{job_description}\n")
    await ctx.send(f'Job posted: {job_description}')

@bot.command()
async def show_jobs(ctx):
    with open('internJobListings.txt', 'r') as f:
        jobs = f.readlines()
    if jobs:
        await ctx.send("Current Job Listings:\n" + "".join(jobs))
    else:
        await ctx.send("No job listings available.")

bot.run(TOKEN)
