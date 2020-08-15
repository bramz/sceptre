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
    select level from permissions where username = $1;
    '''
    row = await context['db'].fetchrow(statement, str(user))

    if row is None:
        return 0
    else:
        return row['level']


commands = [
    {
        'trigger': 'test',
        'module': 'cmds.test',
        'handler': 'TestCommand',
        'permissions': 0
    }
]