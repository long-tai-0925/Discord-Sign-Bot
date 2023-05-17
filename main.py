import discord
from discord.ext import commands
import datetime
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('User：', bot.user)

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.coin = 0
        self.last_sign = None

    def add_coin(self, amount):
        self.coin += amount

    def remove_coin(self, amount):
        if self.coin - amount < 0:
            return False
        self.coin -= amount
        return True

users = {}


# Sign(Main)
@bot.command(name='sign')
async def sign(ctx):
    user_id = ctx.author.id
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    if user_id in users and users[user_id].last_sign == today:
        await ctx.send(f'{ctx.author.mention} You signed in!')
        return
    coin_reward = random.randint(1, 101)
    if user_id not in users:
        users[user_id] = User(user_id, ctx.author.name)
    users[user_id].add_coin(coin_reward)
    users[user_id].last_sign = today
    with open('c:/Users/tulub/OneDrive/桌面/sign_log.txt', 'a') as f:
        f.write(f'{user_id} {today} {coin_reward}\n')
    await ctx.send(f'{ctx.author.mention} Sign in successfully! Get {coin_reward} Coin！')

    
# see user coin
@bot.command(name='coin')
async def coin(ctx):
    user_id = ctx.author.id
    if user_id not in users:
        await ctx.send(f'{ctx.author.mention} You dont gated Coin！')
        return
    coin = users[user_id].coin
    await ctx.send(f'{ctx.author.mention} You have {coin} Coin！')

    
# add coin
@bot.command(name='addcoin')
async def add(ctx, member: discord.Member, amount: int):
    if ctx.author.id != Your_Discord_ID:
        await ctx.send(f'{ctx.author.mention} You cannot do this！')
        return
    if member.id not in users:
        users[member.id] = User(member.id, member.name)
    users[member.id].add_coin(amount)
    await ctx.send(f'{member.mention} You Get {amount} Coin！')

    
# remove coin
@bot.command(name='removecoin')
async def remove(ctx, member: discord.Member, amount: int):
    if ctx.author.id != Your_Discord_ID :
        await ctx.send(f'{ctx.author.mention} You cannot do this！')
        return
    if member.id not in users:
        await ctx.send(f'{member.mention} Do not have any Coin')
        return
    success = users[member.id].remove_coin(amount)
    if success:
        await ctx.send(f'{member.mention} remove {amount} Coin！')
    else:
        await ctx.send(f'{member.mention} have error！')

        
# error message 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error


bot.run("YOUR_TOKEN")
