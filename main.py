from command import Command
import discord

client = discord.Client()
PREFIX = "spot"

@client.event
async def on_ready():
    print("Log in as {}".format(client.user))


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.lower().startswith(PREFIX):
        args = message.content.rstrip().split()
        for com in Command.__subclasses__():
            if args[1].lower() in com().calls:
                reply = await com.execute(args[2:], message)

                if reply is None:
                    return
                elif type(reply) is str:
                    await message.channel.send(reply)
                elif type(reply) is discord.Embed:
                    await message.channel.send(embed=reply)
                return


with open("token", "r") as file:
    client.run(file.read())
