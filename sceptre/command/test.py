from command.handler import Handler


class QuitCommand(Handler):
    async def handle(self, context, message):
        await message.channel.send(
            'Testing... Beep, Boop.'
        )
