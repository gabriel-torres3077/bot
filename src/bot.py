import discord
from discord.ext import commands, tasks
from time import sleep
import riotwatcher

bot = commands.Bot(command_prefix='$')
DISCORD_TOKEN = 'Token do bot'

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def action(ctx, arg): #substituir 'action' nome do comando
    response = f'@{ctx.author.display_name} ação {arg}' #substituir 'placeHolder' pela ação desejada
    await ctx.send(response)

@bot.command()
async def summon(ctx, arg):
    # escrever o nome da pessoa junto com a foto dela
    await ctx.send(arg)
    if (arg == 'Nome'):
        await ctx.send(file=discord.File('imagem.png'))
    if (arg == ''):
        await ctx.send(file=discord.File('.jpg'))
    if (arg == ''):
        await ctx.send(file=discord.File('.jpg'))
    if (arg == ''):
        await ctx.send(file=discord.File('.jpg'))
    #entrar no chat de voz de quem escreveu a mensagem e tocar uma musica
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="local do som"))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.1)
        await vc.disconnect()

@bot.command()
async def elo(ctx, summoner):
    watcher = riotwatcher.LolWatcher(DISCORD_TOKEN)
    my_region = 'br1'

    me = watcher.summoner.by_name(my_region, summoner)
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    tier = [dic['tier'] for dic in my_ranked_stats]
    pdl = [dic['leaguePoints'] for dic in my_ranked_stats]
    rank = [dic['rank'] for dic in my_ranked_stats]
    summonerName = [dic['summonerName'] for dic in my_ranked_stats]
    await ctx.send('O(a) {} ta {} {} com {} pdl '.format(summonerName[0], tier[0], rank[0], pdl[0]))
    print(my_ranked_stats)


@bot.command()
async def open(ctx, pagelink):
    page = pagelink
    if pagelink == 'youtube':
        page = ('https://www.youtube.com/')
    elif pagelink == 'reddit':
        page = ("https://www.reddit.com/")
    elif pagelink == "whatsapp":
        page = ("https://web.whatsapp.com/")

    embed = discord.Embed(title="Your link", url=page)
    await ctx.send(embed=embed)

bot.run(DISCORD_TOKEN)

