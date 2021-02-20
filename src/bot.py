import discord
from discord.ext import commands, tasks
from time import sleep

bot = commands.Bot(command_prefix='$') #'$' prefixo para ativar os comandos EX: $action

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def action(ctx, arg): #substitua 'action' pelo nome da ação
    response = f'{ctx.author.display_name} ESCREVA AQUI A AÇÃO {arg}' #ctx.author.display_name = nome de quem escreveu o comando | arg = nome digitado(pode ser uma mention)
    await ctx.send(response)

@bot.command()
async def summon(ctx, arg):
    # escrever o nome da pessoa junto com a foto dela
    await ctx.send(arg)
    if (arg == 'usuário1'):
        await ctx.send(file=discord.File('placeHolder.png'))
    if (arg == 'usuário2'):
        await ctx.send(file=discord.File('placeHolder.jpg'))
    #entrar no chat de voz de quem escreveu a mensagem e tocar uma musica
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Local do audio no seu computador"))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.1)
        await vc.disconnect()

bot.run('TOKEN DO DISCORD')

