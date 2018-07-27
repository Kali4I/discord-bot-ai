import os.path, shutil, asyncio, discord
from discord import User
from random import choice
from resources.modules.func import sendEmbed

clr_def_ERROR = 0xff0000

def copytree(src, dst, symlinks=False, ignore=None):
    try:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
        return True
    except Exception as e:
        return e

async def send_permission_error(message):
    """
    Возвращает сообщение об отсутствии прав у пользователя.
    Аргументы:
        message = discord.Message() | Сообщение пользователя.
    """
    return await sendEmbed(c=clr_def_ERROR,
                            t='Ошибка прав (」°ロ°)」',
                            d='⚠ | У вас недостаточно прав.',
                            a_name=message.author.name,
                            channel=message.channel
                            )

async def send_me_permission_error(message):
    """
    Возвращает сообщение об отсутствии прав у бота.
    Аргументы:
        message = discord.Message() | Сообщение пользователя.
    """
    return await sendEmbed(c=clr_def_ERROR,
                            t='Не получилось (╥﹏╥)',
                            d='🖥 | У меня недостаточно прав.',
                            a_name=message.author.name,
                            a_avatar=message.author.avatar_url,
                            channel=message.channel
                            )

async def not_working(message):
    """
    Возвращает сообщение о том, что команда не может быть выполнена, пока у бота отсутствуют необходимые права.
    Аргументы:
        message = discord.Message() | Сообщение пользователя.
    """

    return await sendEmbed(c=clr_def_ERROR,
                            t='Не получилось (╥﹏╥)',
                            d='⚠ | У меня недостаточно прав.',
                            a_name=message.author.name,
                            channel=message.channel
                            )

async def send_error(chan, text):
    """Возвращает сообщение об ошибке."""
    return await sendEmbed(c=clr_def_ERROR,
                            t='Ошибка (╬ Ò﹏Ó)',
                            d=text,
                            channel=chan
                            )

async def send_exception(exception:str, channel):
    """Возвращает сообщение о возникшем исключении."""
    await sendEmbed(c=clr_def_ERROR,
                            t='Возникло исключение ヽ(ー_ー )ノ',
                            d=exception,
                            channel=channel
                            )
