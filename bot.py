import discord

def readtoken():
    with open('token.txt','r') as f:
        lines=f.readlines()
        return lines[0].strip()

token=readtoken()

client=discord.Client()

@client.event
async def on_message(message):
    print(message.content)
client.run(token)
