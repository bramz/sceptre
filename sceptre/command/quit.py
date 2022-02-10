from command.handler import Command


class QuitCommand(Command):
    async def handle(self, context, message):
        await message.channel.send(
            'So long brainiacs.. I shall return!'
        )
        await context['client'].logout()