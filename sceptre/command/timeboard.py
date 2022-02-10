from command.handler import Handler


class TimeboardCommand(Handler):
    async def handle(self, context, message):
        await message.channel.send(
            'Timeboard command placeholder'
        )
