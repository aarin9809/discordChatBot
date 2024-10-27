import discord
import crawling
import ssl

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

        if message.content.startswith('!weather'):
            cmd = message.content.split()
            print(cmd)
            if len(cmd) == 2:
                w = cmd[1]
                print("search weather:", w)
                winfo = crawling.weather(w)
                print("\tweather info", winfo)
                await message.channel.send(winfo)
            else:
                print("wrong params")
                await message.channel.send("wrong params")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
token= open('token.txt').readline()
client.run(token)