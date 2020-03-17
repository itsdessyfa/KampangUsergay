from userge import userge, Filters
from userge.db import Database

log = userge.getLogger(__name__)

welcome_db = Database("welcome")

welcome_list = welcome_db.filter({'on': True}, {'_id': 1})

welcome_chats = Filters.chat([])

for i in welcome_list:
    welcome_chats.add(i.get('_id'))


@userge.on_cmd("setwelcome", about="Creates a welcome message in current chat :)")
async def setwel(_, message: userge.MSG):
    if message.chat.type in ["private", "bot", "channel"]:
        await message.edit('Are you high XO\nSet welcome in a group chat')
        return

    try:
        welcome_string = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await message.edit("wrong syntax\n`.setwelcome <welcome message>`")
    else:
        new_entry = {'_id': message.chat.id, 'data': welcome_string, 'on': True}

        if welcome_db.findone('_id', message.chat.id):
            welcome_db.update({'_id': message.chat.id}, new_entry, 'set')
        else:
            welcome_db.addnew(new_entry)

        welcome_chats.add(message.chat.id)
        await message.edit(f"Welcome message has been set for the \n`{message.chat.title}`")


@userge.on_cmd("nowelcome", about="Dissables welcome message in the current chat :)")
async def nowel(_, message: userge.MSG):
    try:
        welcome_chats.remove(message.chat.id)
    except KeyError as e:
        await message.edit(e)
    else:
        welcome_db.update({'_id': message.chat.id}, {'on': False}, 'set')
        await message.edit("Dissabled Successfully !")


@userge.on_cmd("dowelcome", about="Turns on welcome message in the current chat :)")
async def dowel(_, message: userge.MSG):
    if welcome_db.findone('_id', message.chat.id):
        welcome_chats.add(message.chat.id)
        welcome_db.update({'_id': message.chat.id}, {'on': True}, 'set')
        await message.edit('I will welcome new members XD')

    else:
        await message.edit('Please set the welcome message with `.setwelcome`')


@userge.on_new_member(welcome_chats)
async def saywel(_, message: userge.MSG):
    welcome_message = welcome_db.findone('_id', message.chat.id)['data']

    user = message.from_user
    fname = user.first_name if user.first_name else ''
    lname = user.last_name if user.last_name else ''
    fullname = fname + ' ' + lname
    username = user.username if user.username else ''

    kwargs = {
        'fname': fname,
        'lname': lname,
        'fullname': fullname,
        'uname': username,
        'chat': message.chat.title if message.chat.title else "this group",
        'mention': f'<a href="tg://user?id={user.id}">{username or fullname or "user"}</a>',
    }

    await message.reply(welcome_message.format(**kwargs))


@userge.on_cmd("listwelcome", about="Shows the activated chats for welcome")
async def lswel(_, message: userge.MSG):
    liststr = ""
    welcome_list = welcome_db.filter({'on': True}, {'_id': 1, 'data': 1})

    for j in welcome_list:
        liststr += f"**{(await userge.get_chat(j.get('_id'))).title}**\n"
        liststr += f"`{j.get('data')}`\n\n"

    await message.edit(liststr or '`NO WELCOMES STARTED`')