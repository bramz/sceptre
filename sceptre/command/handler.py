import importlib


class Handler:
    def handle(self):
        pass


def command_handler(module, handler) -> Handler:
    m = importlib.import_module(module)
    cmd = getattr(m, handler)
    return cmd


async def get_permissions(context, user) -> int:
    statement = '''
    select level from permissions where username = ?
    '''

    cursor = await context['db'].cursor()
    await cursor.execute(statement, (str(user), ))
    row = await cursor.fetchone()

    if row is None:
        return 0
    else:
        return row[0]


commands = [
    {
        'trigger': 'test',
        'module': 'command.test',
        'handler': 'TestCommand',
        'permissions': 2
    },
    {
        'trigger': 'timeboard',
        'module': 'command.timeboard',
        'handler': 'TimeboardCommand',
        'permissions': 2
    }
]