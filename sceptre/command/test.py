from command.handler import Handler


class TestCommand(Handler):
    async def handle(self, context, message):
        await message.channel.send(
            'Testing... Beep, Boop.'
        )
