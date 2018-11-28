import capncord


class Bot(capncord.Bot):
    async def on_ready(self):
        name = await self.user.name
        print(f"Ready as {name}")
        await self.wait_for("message", check=lambda m: m.content.startswith("apple"))
        print("Boom!")

    async def on_message(self, message):
        name = await message.author.name
        print(f"{name}: {message.content}")
        if message.content.startswith("!ping"):
            await self.send("Pong!")
        elif message.content.startswith("!id"):
            history = await self.history()
            await self.send(history[1].id)
        elif message.content.startswith("!getmsg"):
            arg = message.content.split()[1]
            msg = await self.get_message(int(arg))
            await self.send(msg.content)

bot = Bot()

with open("token.txt") as f:
    bot.run(f.read())
