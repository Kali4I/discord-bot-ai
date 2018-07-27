# -*- coding: utf-8 -*-
import discord
import asyncio

client = discord.Client()

def getChannel(server, name):
    """
    Получение объекта канала учитывая объект сервера и имя канала.
    Аргументы:
        server = discord.Server() | Требуемый сервер;
        name = str() | Имя требуемого канала.
    """
    for channel in server.channels:
        if channel.name == name:
            __target__channel = channel
            return __target__channel
    return None

def getServerEmoji(server, name:str):
    """
    Получение объекта эмодзи, зная объект сервера и название эмодзи.
    Аргументы:
        server = discord.Server() | Сервер, среди эмодзи которого нужно искать;
        name = discord.Emoji() or str() | Название эмодзи, которое нужно искать.
    """
    return discord.utils.get(serv.emojis, name=name)

def getEmoji(name):
    """
    Получение объекта эмодзи, зная объект клиента и название эмодзи.
    Аргументы:
        name = str() | Название эмодзи, которое нужно получить из клиента.
    """
    return discord.utils.get(get_all_emojis(), name=name)

def getRole(names, server):
    """
    Получение объекта роли, зная название роли и объект сервера.
    Аргументы:
        names = str() or list() |
    """
    for r in server.roles:
        if r.name in names or r.name == str(names):
            role = r
            return role
    return None

def toFn(string):
    """
    Возвращает данную строку, убирая из нее символы, запрещенные в именах папок и файлов Windows.
    Аргументы:
        string = str() | Строка, из которой надо убрать "все лишнее".
    """
    target = str(string).replace('<', "").replace('>', "").replace(':', "").replace('*', "").replace('|', "").replace('?', "").replace('"', "").replace('/', "").replace('\\', "")
    return target

def getUsername(user_name, server):
    """
    Возвращает объект discord.User.
    Аргументы:
        user_name = str() | Никнейм пользователя.
        server = discord.Server() | Сервер, на котором искать пользователя.
    """
    user = user_name.replace('<', '').replace('>', '').replace('@', '').replace('!', '').replace('&', '')
    if user.isnumeric():
        return server.get_member(user)
    else:
        return discord.utils.get(server.members, name=user)

def htmlToHex(color: str):
    """
    Возвращает объект HEX цвета для Discord, преобразовывая цвет.
    Аргументы:
        html = str() | Цвет в формате HTML (напр. #F90F25 или F90F25)
    """
    if len(html) == 6:
        try: color_ = discord.Colour(int(color, 16))
        except: raise ValueError('Не удалось преобразовать цвет.')
        else: return color_
    elif len(html) == 7:
        try:
            clr = str(color).replace('#', '0x')
            color_ = discord.Colour(int(clr, 0))
        except: raise ValueError('Не удалось преобразовать цвет.')
        else: return color_
    else:
        raise InvalidColor('Код цвета должен состоять из 6 (без #) или 7 (с #) символов.')

async def sendEmbed(channel, c=0xffffff, t=None, d=None, a_name='', a_avatar='', i=None, f_text='', f_icon='', th=None, server_chat=True, **options):
    """!COROUTINE!
    Возвращает сообщение с вкладкой (discord.Embed)
    Аргументы:
        channel = discord.Channel() | Канал для отправки;
        c (0xffffff) = discord.Colour() | Цвет полоски;
        t = str() | Заглавие вкладки;
        d = str() | Описание (контент) вкладки;
        a_name = str() | Текст сверху;
        a_avatar = str() | (Только URL!!) Иконка сверху;
        i = str() | (Только URL!!) Изображение во вкладке;
        f_text = str() | Текст снизу;
        f_icon = str() | (Только URL!!) Иконка снизу;
        th = str() | (Только URL!!) Небольшое изображение сверху-справа;
        serverchat = bool | Отправлять-ли сообщения в серверный чат;
        **options | Дополнительные настройки (если имеются).
    """
    embed_ = discord.Embed(title=t, description=d, color=c, **options)
    if a_name or a_avatar:
        embed_.set_author(name=a_name, icon_url=a_avatar)
    if i:
        embed_.set_image(url=i)
    if f_icon or f_text:
        embed_.set_footer(icon_url=f_icon, text=f_text)
    if th:
        embed_.set_thumbnail(url=th)
    if server_chat:
        return await client.send_message(channel, embed=embed_)
    else:
        return await client.send_message(author, embed=embed_)

async def setEmbed(c=0xffffff, t=None, d=None, a_name='', a_avatar='', i=None, f_text='', f_icon='', th=None, server_chat=True, **options):
    embed_ = discord.Embed(title=t, description=d, color=c, **options)
    if a_name or a_avatar:
        embed_.set_author(name=a_name, icon_url=a_avatar)
    if i:
        embed_.set_image(url=i)
    if f_icon or f_text:
        embed_.set_footer(icon_url=f_icon, text=f_text)
    if th:
        embed_.set_thumbnail(url=th)
    return embed_
