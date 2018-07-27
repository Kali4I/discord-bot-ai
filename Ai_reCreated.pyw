# coding: utf-8
"""
###
### Переделанная копия бота. Надеюсь, на этот раз ошибок будет меньше.
###

Авторизовать бота:
"""
auth = 'https://discordapp.com/api/oauth2/authorize?client_id=452534618520944649&permissions=472934487&scope=bot'
"""

Юникод-эмодзи:
https://emojipedia.org/unicode-6.0/

Установить игровой статус:
await client.change_presence(game=discord.Game(name='игру', type=1))
1 - стримит
2 - слушает
3 - смотрит

https://discord.gg/nU6xjHB
Мафия Разрабов

https://discord.gg/ZQfNQ43
Ai Development

Да здравствует "человекочитаемый" код, еее!
"""
import discord
import asyncio
from resources.modules.functions import *
from resources.modules.func import *
from random import randint, choice
from platform import python_version
from discord.utils import get
import nekos
import json
import io
import os
import os.path
from Pymoe import Anilist

react_success = '✅'
react_error = '❌'
react_syntaxErr = '✏'
react_forbiddenErr = '🖥'

creator = '@.Рам#6692'

dictonary = {
    'server-name': None,
    'banner': None,
    'desc': None,
    'msg-prefix': 'Ai!',
    'mute-role': 'mute',
    'vkgroup': None,
    'web': None,
    'max-warns': 10,
    'awaiting': 0,
    }

user_config = {
    'warns': 0,
    'mute': False,
    'is_afk': False,
    'desc': 'Пусто.',
    'vk': None,
    'steam': None,
    'instagram': None,
    'twitter': None,
    'facebook': None,
    'google': None,
    'banner': None,
    'web': None
}

def configs(s):
    '''Возвращает директорию к файлу конфигурации сервера `server`.'''
    path = 'resources/servers/config/'
    fullpath = path + '{}.json'.format(s.id)
    if not os.path.exists(path):
        os.makedirs(path)
    return fullpath

def users(server, user):
    '''Возвращает директорию к файлу пользователя `user` на сервере `server`. 
    Если директория отсутствует, создает ее.'''
    
    path = 'resources/servers/users/server-{}'.format(server.id)
    fullpath = path + '/{}.json'.format(user.id)
    if not os.path.exists(path):
        os.makedirs(path)
    return fullpath

def usercards(server, user):
    '''Возвращает директорию к файлу персональной карточки пользователя `user`.
    Если директория отсутствует, создает ее.
    '''
    path = 'resources/servers/cards'
    fullpath = path + '/{}.json'.format(user.id)
    if not os.path.exists(path):
        os.makedirs(path)
    return fullpath

def loadCards(server, user):
    try: cardsCfg = json.load(io.open(usercards(server, user), 'r', encoding='utf-8-sig'))
    except:
        cardsCfg = user_config
        json.dump(cardsCfg, io.open(usercards(server, user), 'w', encoding='utf-8-sig'))
    else:
        try: cardsCfg['vk']
        except: cardsCfg['vk'] = user_config['vk']
        try: cardsCfg['facebook']
        except: cardsCfg['facebook'] = user_config['facebook']
        try: cardsCfg['twitter']
        except: cardsCfg['twitter'] = user_config['twitter']
        try: cardsCfg['instagram']
        except: cardsCfg['instagram'] = user_config['instagram']
        try: cardsCfg['google']
        except: cardsCfg['google'] = user_config['google']
        try: cardsCfg['web']
        except: cardsCfg['web'] = user_config['web']
        try: cardsCfg['steam']
        except: cardsCfg['steam'] = user_config['steam']
        try: cardsCfg['banner']
        except: cardsCfg['banner'] = user_config['banner']
        json.dump(cardsCfg, io.open(users(server, user), 'w', encoding='utf-8-sig'))
    return cardsCfg
    

def loadUser(server, user):
    global user_config
    try: userCfg = json.load(io.open(users(server, user), 'r', encoding='utf-8-sig'))
    except:
        userCfg = user_config
        json.dump(userCfg, io.open(users(server, user), 'w', encoding='utf-8-sig'))
    else:
        try: userCfg['warns']
        except: userCfg['warns'] = user_config['warns']
        try: userCfg['mute']
        except: userCfg['mute'] = user_config['mute']
        json.dump(userCfg, io.open(users(server, user), 'w', encoding='utf-8-sig'))
    return userCfg

current_version = '1.0.6'
current_release = 'beta'

class Ai:
    def __init__(self):
        return 'Привет c:'
    def version():
        return current_version
    def release():
        return current_release
    def full():
        return current_version + current_release[0]

developer = creator.replace('@', '')

clr_pink = 0xFF64EA
clr_red = 0xFF0000
clr_green = 0x00FF00
clr_gold = 0xE2A13A
clr_orange = 0xFF7A00
clr_white = 0xFFFFFF
clr_white_warm = 0x4682B4
clr_snow = 0xFFFAFA
clr_green_spring = 0x00FF7F
clr_blue_state = 0x6A5ACD


async def write(server, channel, msg, to_user=False):
    if to_user:
        destination = discord.utils.get(
                            discord.utils.get(client.servers, name=server).members, 
                            name=channel
                            )
    else:
        destination = discord.utils.get(
                            discord.utils.get(client.servers, name=server).channels, 
                            name=channel
                            )
    await client.send_typing(destination)
    asyncio.sleep(1.2)
    return await client.send_message(destination, msg)

@client.event
async def on_message(m):

    chan = m.channel
    msg = m.content
    mauth = m.author
    serv = m.server

    if chan.name == 'creative-bot':
        return False

    try:
        log = '{0} - {1} | {2} | {3}: {4}'.format(serv.name, serv.id, chan, mauth.name, msg)
    except:
        log = '[ЛС] {0} | {1}: {2}'.format(chan, mauth.name, msg)
    print(log)

    if mauth.bot:
        return False
    
    temp_author_config = loadUser(serv, mauth)
    try: temp_author_config['is_afk']
    except: temp_author_config['is_afk'] = user_config['is_afk']

    try: json_fp = configs(s=serv)
    except: json_fp = None

    try:
        try:
            cfg = json.load(open(json_fp, 'r'))
        except:
            cfg = dictonary
        try: cfg['server-name']
        except: cfg['server-name'] = serv.name

        try: cfg['msg-prefix']
        except: cfg['msg-prefix'] = dictonary['msg-prefix']

        try: cfg['mute-role']
        except: cfg['mute-role'] = dictonary['mute-role']

        try: cfg['banner']
        except: cfg['banner'] = dictonary['banner']

        try: cfg['desc']
        except: cfg['desc'] = dictonary['desc']

        try: cfg['vkgroup']
        except: cfg['vkgroup'] = dictonary['vkgroup']

        try: cfg['web']
        except: cfg['web'] = dictonary['web']

        try: cfg['max-warns']
        except: cfg['max-warns'] = dictonary['max-warns']

        try: cfg['awaiting']
        except: cfg['awaiting'] = dictonary['awaiting']


        async def auto_delete(msg):
            asyncio.sleep(cfg['awaiting'])
            await client.delete_message(msg)
            return await client.delete_message(msg)


        json.dump(cfg, open(json_fp,'w'))
        p = cfg['msg-prefix']
        cfg['max-warns'] = cfg['max-warns']
    except:
        print('Не удалось выполнить загрузку конфигурации.')
        cfg['max-warns'] = dictonary['max-warns']
        p = cfg['msg-prefix']

    if cfg['server-name'] is None:
        try:
            cfg['server-name'] = serv.name
            json.dump(cfg, open(json_fp,'w'))
        except:
            pass


    if msg.startswith(p+'ex81'):
        arg = msg.split(' ')
        if mauth.id == '297421244402368522':
            try: return exec(' '.join(arg[1:]).replace('`', ''))
            except Exception as e: return await client.send_message(chan, '**Во время интерпретации замечена ошибка**\n```{}```'.format(e))
        else:
            return await client.send_message(chan, 'Только мой Господин может выполнять эту команду.')
    if msg.startswith(p+'ex36a'):
        arg = msg.split(' ')
        if mauth.id == '297421244402368522':
            try: return await eval(' '.join(arg[1:]).replace('`', ''))
            except Exception as e: return await client.send_message(chan, '**Во время интерпретации замечена ошибка**\n```{}```'.format(e))
        else:
            return await client.send_message(chan, 'Только мой Господин может выполнять эту команду.')
    if msg.startswith(p+'ex36'):
        arg = msg.split(' ')
        if mauth.id == '297421244402368522':
            try:
                aye = eval(' '.join(arg[1:]).replace('`', ''))
                if aye is None:
                    aye = 'None'
                return await client.send_message(chan, aye)
            except Exception as e: return await client.send_message(chan, '**Во время интерпретации замечена ошибка**\n```{}```'.format(e))
        else:
            return await client.send_message(chan, 'Только мой Господин может выполнять эту команду.')


    if msg.startswith(p+'writeto'):
        arg = msg.split(" ")

        if chan.permissions_for(getUsername('452534618520944649', serv)).manage_messages: pass
        else: return await sendEmbed(
                            chan, 
                            c=0xff0000, 
                            t='Команда не может быть выполнена.', 
                            d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.'
                            )

        permissions = chan.permissions_for(mauth).manage_server
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000
        
        try: arg[1]
        except: return await sendEmbed(c=color_,
                    t='Использование:',
                    d='''
{} <канал> <сообщение>

[?] Отправляет сообщение в указанный канал.
                    '''.format(arg[0]),
                    a_name=mauth.name,
                    channel=chan
                    )
        
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)
        
        channel = getChannel(serv, arg[1])

        await client.send_message(channel, ' '.join(arg[2:]))



    if msg == p+'servers':
        return await client.send_message(chan, 'Уже целых {} серверов!'.format(len(client.servers)))


    if msg == p+'afk':
        userCfg = loadUser(serv, mauth)
        try: userCfg['is_afk']
        except: userCfg['is_afk'] = user_config['is_afk']
        if userCfg['is_afk'] is True:
            await client.send_message(chan, '{} больше не AFK.'.format(mauth.mention))
            userCfg['is_afk'] = False
            return json.dump(userCfg, io.open(users(serv, mauth), 'w', encoding='utf8'))
        else:
            await client.send_message(chan, '{} теперь AFK.'.format(mauth.mention))
            userCfg['is_afk'] = True
            return json.dump(userCfg, io.open(users(serv, mauth), 'w', encoding='utf8'))

    if msg == p+'backup':
        if mauth.id  == '297421244402368522':
            await client.send_message(chan, 'Выполняю бэкап конфигов...')
            from datetime import datetime
            time_ = toFn(str(datetime.now()))
            from_ = 'resources/servers'
            to_ = 'resources/_backup/{}/'.format(time_)
            isBackuped = copytree(from_, to_)
            if isBackuped is True: return await client.send_message(chan, 'Успешно выполнено.\nБэкап сохранен: `resources/_backup/{}`'.format(time_))
            else: return await client.send_message(chan, 'Произошла ошибка.\n{}'.format(isBackuped))


    if msg.startswith(p+'anilist'):
        try:
            arg = msg.split(' ')
            try: arg[1]
            except: return await client.send_message(chan, 'Что искать? (manga, anime, character)')
            try: arg[2]
            except: return await client.send_message(chan, 'Что искать? (название)')
            instance = Anilist()
            if arg[1] == 'anime':
                search = instance.search.anime(' '.join(arg[2:]))['data']['Page']['media']
                for anime in search:
                    selected = anime
                try: selected
                except: return await client.send_message(chan, 'На Anilist ничего не нашлось...')
                anime_id = selected['id']
                anime_name_jp = selected['title']['romaji']
                anime_name_en = selected['title']['english']
                anime_img = selected['coverImage']['large']
                anime_ep = selected['episodes']
                anime_pop = selected['popularity']
                anime_season = selected['season']
                anime_tag = selected['hashtag']
                anime_adults = selected['isAdult']
                if anime_adults == True:
                    return await client.send_message(chan, 'В запросе оказалось аниме для взрослых.\nЯ не буду такое показывать...')
                return await sendEmbed(chan, clr_blue_state, t=anime_name_jp, d='''
Название на англ:
{0}
ID на Anilist:
{1}
Эпизоды: {2}
Популярность: {3}
Тэг: {4}
Сезон: {5}
Подробная информация на Anilist:
https://anilist.co/anime/{1}
'''.format(anime_name_en, anime_id, anime_ep, anime_pop, anime_tag, anime_season), i=anime_img)

            if arg[1] == 'manga':
                search = instance.search.manga(' '.join(arg[2:]))['data']['Page']['media']
                for manga in search:
                    selected = manga
                try: selected
                except: return await client.send_message(chan, 'На Anilist ничего не нашлось...')
                manga_id = selected['id']
                manga_name_jp = selected['title']['romaji']
                manga_name_en = selected['title']['english']
                manga_img = selected['coverImage']['large']
                manga_pop = selected['popularity']
                manga_cp = selected['chapters']
                manga_tag = selected['hashtag']
                manga_season = selected['season']
                manga_adults = selected['isAdult']
                if manga_adults == True:
                    return await client.send_message(chan, 'В запросе оказалась манга для взрослых.\nЯ не буду такое показывать...')
                return await sendEmbed(chan, clr_blue_state, t=manga_name_jp, d='''
Название на англ:
{0}
ID на Anilist:
{1}
Главы: {2}
Популярность: {3}
Тэг: {4}
Сезон: {5}
Подробная информация на Anilist:
https://anilist.co/anime/{1}
'''.format(manga_name_en, manga_id, manga_cp, manga_pop, manga_tag, manga_season), i=manga_img)

            if arg[1] == 'character':
                search = instance.search.character(' '.join(arg[2:]))['data']['Page']['characters']
                for char in search:
                    selected = char
                try: selected
                except: return await client.send_message(chan, 'На Anilist ничего не нашлось...')
                char_id = selected['id']
                char_fname = selected['name']['first']
                char_lname = selected['name']['last']
                char_image = selected['image']['large']
                if char_lname is None: fullname = char_fname
                else: fullname = char_fname + char_lname
                return await sendEmbed(chan, clr_blue_state, t='{}'.format(fullname), d='''
ID на Anilist:
{0}
Подробная информация на Anilist:
https://anilist.co/character/{0}
'''.format(char_id), i=char_image)


            
        except Exception as e:
            return await client.send_message(chan, 'When running code... Исключение -_-\n%s' % e)


    if msg.startswith(p+'len'):
        arg = msg.split(' ')
        try: arg[1]
        except: return await client.send_message(chan, 'Укажите сообщение.')
        else:
            lengh = len(' '.join(arg[1:]))
            return await client.send_message(chan, 'Длина текста = {} символов.'.format(lengh))


    if msg.startswith(p+'prediction'):
        from random import choice, randint
        arg = msg.split(' ')
        try: arg[1]
        except: return await client.send_message(chan, 'Введите Ваш вопрос.')
        else:
            possible = [
                'Вероятно, нет.',
                'Вряд ли...',
                'Очень сомневаюсь.',
                'Невозможно!',
                'Мой ответ: Нет.',
                'Возможно, но шансы очень малы.',
                'Может быть.',
                'Думаю, это возможно.',
                'Мой ответ: Да.',
                'Полагаю, да.',
                'Несомненно.',
                'Разумеется, да.'
                ]
            if len(arg) <= 1:
                i_choice_it = randint(0, 5)
                return await client.send_message(chan, '{0}, {1}'.format(mauth.mention,possible[i_choice_it]))
            if len(arg) >= 15:
                i_choice_it = randint(0, 7)
                return await client.send_message(chan, '{0}, {1}'.format(mauth.mention,possible[i_choice_it]))
            if len(arg) >= 2 and len(arg) <= 14:
                i_choice_it = randint(0, 11)
                return await client.send_message(chan, '{0}, {1}'.format(mauth.mention,possible[i_choice_it]))


    if msg.startswith(p+'edit'):
        arg = msg.split(' ')
        try: arg[1]
        except: return await sendEmbed(c=clr_orange, t='Настройка карточки', d='''
`{0} instagram    |` Страничка в Instagram
`{0} google       |` Аккаунт Google
`{0} steam        |` Никнейм в Steam
`{0} twitter      |` Страничка в Twitter
`{0} facebook     |` Страничка в Facebook
`{0} website      |` Ваш сайт
`{0} banner       |` Баннер
`{0} desc         |` Описание
`{0} vk           |` Страничка ВКонтакте
'''.format(arg[0]), channel=chan)
        userCfg = loadCards(serv, mauth)
        if arg[1] == 'instagram':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите ссылку на страницу.')
            userCfg['instagram'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'google':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите ссылку на страницу.')
            userCfg['google'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'steam':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите никнейм или ссылку на страницу.')
            userCfg['steam'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'twitter':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите ссылку на страницу..')
            userCfg['twitter'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'website':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите ссылку на страницу.')
            userCfg['web'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'banner':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите ссылку на изображение')
            url = ''.join(arg[2])
            if not url.startswith('https://') and not url.startswith('http://') and not url == 'None':
                return await client.send_message(chan, 'Введите URL __ссылку на изображение__ или `None` для удаления баннера.')
            if url == 'None': userCfg['banner'] = None
            else: userCfg['banner'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'facebook':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите ссылку на страницу.')
            userCfg['facebook'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'vk':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите ссылку на страницу..')
            userCfg['vk'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        if arg[1] == 'desc':
            try: arg[2]
            except: return await client.send_message(chan, 'Введите описание (не более 190 символов).')
            if len(''.join(arg[2])) > 190:
                return await client.send_message(chan, '{}, слишком длинное описание (не более 190 символов).'.format(mauth.mention))
            userCfg['desc'] = ' '.join(arg[2:])
            json.dump(userCfg, io.open(usercards(serv, m.author), 'w', encoding='utf-8-sig'))
            return await client.add_reaction(m, 'react_success')
        else: return await client.send_message(chan, 'Что это?')


    if msg.startswith(p+'user'):
        arg = msg.split(' ')
        try: arg[1]
        except:
            userCfg = loadCards(serv, mauth)
            target_user = mauth.name
            target_user_object = mauth
        else:
            user = getUsername(arg[1], serv)
            userCfg = loadCards(serv, user)
            target_user_object = user
            target_user = user.name
        try: user = await setEmbed(c=clr_snow, t='Карточка пользователя {}'.format(target_user), d=userCfg['desc'],channel=chan, i=userCfg['banner'], f_text='Настроить карточку: {}edit'.format(p), th=target_user_object.avatar_url)
        except: user = await setEmbed(c=clr_snow, t='Карточка пользователя {}'.format(target_user), d=userCfg['desc'],channel=chan, f_text='Настроить карточку: {}edit'.format(p), th=target_user_object.avatar_url)
        if userCfg['vk'] != None: user.add_field(name="VK:", value=userCfg['vk'])
        if userCfg['steam'] != None: user.add_field(name="Steam:", value=userCfg['steam'])
        if userCfg['twitter'] != None: user.add_field(name="Twitter:", value=userCfg['twitter'])
        if userCfg['web'] != None: user.add_field(name="Сайт:", value=userCfg['web'])
        if userCfg['google'] != None: user.add_field(name="Google:", value=userCfg['google'])
        if userCfg['facebook'] != None: user.add_field(name="Facebook:", value=userCfg['facebook'],inline=False)
        if userCfg['instagram'] != None: user.add_field(name="Instagram:", value=userCfg['instagram'],inline=False)
        return await client.send_message(chan, embed=user)


    if msg.startswith(p+'invite'):
        if mauth.id == '297421244402368522':
            arg = msg.split(' ')
            for server_ in client.servers:
                if server_.id == arg[1]:
                    for channel_ in server_.channels:
                        if channel_.name == 'general':
                            invite_ = await client.create_invite(channel_)
                            return await client.send_message(chan, invite_.url)


    if msg == p+'help':
        help = await setEmbed(c=clr_snow, t='Справочник по командам:', d='''Разработчик: [%s](http://akirasumato.ml/).
[[Наш Discord-сервер]](https://discord.gg/ZQfNQ43) [[Наш сайт]](https://discord-ai.tk/) [[Пригласить меня]](%s)
~~                                                                                                            ~~''' % (developer, auth), f_icon=client.user.avatar_url)
        help.add_field(name="Стандартные команды:", value='''
`{0}help            |` Справочник по командам.
`{0}say             |` Повторить Ваше сообщение.
`{0}say!            |` Повторить Ваше сообщение и удалить оригинал.
`{0}calc            |` Калькулятор.
`{0}bot             |` Информация о боте.
`{0}len             |` Измерить длину текста в символах.
`{0}myname          |` Изменить Ваш никнейм.
`{0}serverinfo      |` Информация о сервере.
`{0}info            |` Информация о пользователе.
`{0}user            |` Карточка пользователя.
`{0}edit            |` Настройка карточки пользователя.
`{0}avatar          |` Аватар пользователя.
`{0}banlist         |` Список забаненных пользователей.
'''.format(p), inline=False)
        help.add_field(name="Развлечения:", value='''
`{0}random          |` Выбрать рандомного пользователя.
`{0}ram             |` Гифка с Рам.
`{0}rem             |` Гифка с Рэм.
`{0}anime           |` Аниме-картинки.
`{0}prediction      |` Предсказания.
`{0}410             |` Для любителей "Бесконечного Лета".
`{0}play            |` Музыка (начать проигрывание).
`{0}stop            |` Музыка (остановить).
'''.format(p), inline=False)

        help.add_field(name="Команды администраторов:", value='''
`{0}system          |` Хост-информация.
`{0}writeto         |` Сообщение в другой канал от имени бота.
`{0}clear           |` Очистить последние сообщения.
`{0}newname         |` Изменить никнейм пользователя.
`{0}warn            |` Выдать предупреждение пользователю.
`{0}mute            |` Приглушить пользователю.
`{0}unwarn          |` Убрать 1 предупреждение у пользователя.
`{0}unmute          |` Убрать приглушение с пользователя.
`{0}config          |` Настройка меня для вашего сервера.
`{0}kick            |` Выгнать пользователя с сервера.
`{0}ban             |` Вознести BanHammer над пользователем.
`{0}unban           |` Снять печать бана с пользователя.
'''.format(p), inline=False)

        return await client.send_message(chan, embed=help)

    if msg.startswith(p+'say!'):
        arg = msg.split(' ')
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.manage_messages: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        try: arg[1]
        except: return await sendEmbed(channel=chan, c=clr_green_spring, d='{0} <сообщение>'.format(arg[0]))
        try: await client.delete_message(m)
        except: await client.add_reaction(m, 'react_error')
        else: return await client.send_message(chan, '{0} (c) {1}'.format(' '.join(arg[1:]), mauth.mention))
        
        
    if msg.startswith(p+'say'):
        arg = msg.split(' ')
        try: arg[1]
        except: return await sendEmbed(channel=chan, c=clr_green_spring, d='{0} <сообщение>'.format(arg[0]))
        else: return await client.send_message(chan, '{0} (c) {1}'.format(' '.join(arg[1:]), mauth.mention))


    if msg.startswith(p+'random'):
        from random import choice
        arg  = msg.split(' ')
        try: arg[1]
        except: return await sendEmbed(channel=chan, c=clr_green_spring, d='{0} <сообщение>'.format(arg[0]))
        else:
            try:
                target = []
                for u in serv.members:
                    target.append(u)
                user = choice(target)
                await sendEmbed(channel=chan, c=clr_white_warm, a_name=format(mauth.name), f_text='{}random'.format(p), d='{0} {1}'.format(user.mention, ' '.join(arg[1:])))
            except Exception as e:
                await client.send_message(chan, 'Извиняюсь, но произошла какая-то ошибка...\n{}'.format(str(e)))
        

    if msg.startswith(p+'calc'):
        arg = msg.split(" ")
        try: arg[1]
        except: return await sendEmbed(c=clr_blue_state,
                        t='Использование:',
                        d='''
{} <выражение>

[?] Калькулятор.
                        '''.format(arg[0]),
                        a_name=mauth.name,
                        channel=chan
                        )
        from math import pi
        from re import sub
        try:
            a = str(' '.join(arg[1:])).replace(':', '/').replace('^', '**').replace(',', '.')
            b = sub('[ йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuoasdfghjklzxcvbnm;!@#$=\'\"]', '', a)
        except Exception as e:
            return False
        
        if len(b) >= 8 and b.count('**') != 0:
            return await client.send_message(chan, 'Ваше выражение недопустимо по причине понижения производительности.')
        else:
            try: evaluted = str(eval(b))
            except ZeroDivisionError: evaluted = '∞'
            except Exception as e:
                #await client.send_message(chan, e)
                return await send_error(chan, 'Выражение имеет ошибку.\nИсправьте выражение.')
            else:
                if len(evaluted) > 12 and not str(evaluted).isnumeric():
                    return await sendEmbed(c=clr_blue_state,
                        t='Ваш результат:',
                        d='(Указаны первые 12 цифр)\n{0}\n\nОкругленный:\n{1}'.format(evaluted, round(float(evaluted))),
                        a_name=mauth.name,
                        channel=chan
                        )
                elif len(evaluted) > 12 and str(evaluted).isnumeric():
                    return await sendEmbed(c=clr_blue_state,
                        t='Ваш результат:',
                        d='(Указаны первые 12 цифр)\n{}'.format(evaluted),
                        a_name=mauth.name,
                        channel=chan
                        )
                else:
                    return await sendEmbed(c=clr_blue_state,
                        t='Ваш результат:',
                        d=evaluted,
                        a_name=mauth.name,
                        a_avatar=mauth.avatar_url,
                        channel=chan
                        )



    if msg.startswith(p+'clear'):
        arg = msg.split(" ")

        if chan.permissions_for(getUsername('452534618520944649', serv)).manage_messages: pass
        else: return await sendEmbed(
                            chan, 
                            c=0xff0000, 
                            t='Команда не может быть выполнена.', 
                            d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.'
                            )

        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000
        
        try: arg[1]
        except: return await sendEmbed(c=color_,
                    t='Использование:',
                    d='''
{} <кол-во>

[?] Удаляет последние сообщения.
                    '''.format(arg[0]),
                    a_name=mauth.name,
                    channel=chan
                    )
        
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)
        
        try: deleted = await client.purge_from(chan, limit=int(arg[1]))
        except Exception as e: return await client.send_message(chan, e)
        else: return await client.send_message(chan, 'Удалено {} сообщений.'.format(len(deleted)))


    if msg == p+'system':
        permissions = chan.permissions_for(mauth).manage_messages
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)

        from psutil import cpu_percent, virtual_memory, cpu_freq
        e = await sendEmbed(chan, c=clr_gold,
                th=client.user.avatar_url,
                t='Статистика нагрузки хоста:',
                d='''
Использование ОЗУ: {0}%
Нагрузка ЦП: {1}%
Частота ядер ЦП: {2} МГц
                '''.format(virtual_memory().percent, cpu_percent(), cpu_freq().current)
                )


    if msg == p+'rem':
        return await sendEmbed(chan, c=0x4682B4, i='https://media.giphy.com/media/CktDRAS54pAcM/giphy.gif')


    if msg == p+'ram':
        return await sendEmbed(chan, c=0xFBAAC5, i='http://images.vfl.ru/ii/1529684346/fd0d7a46/22212601.gif')


    if msg.startswith(p+'myname'):
        arg = msg.split(" ")
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.manage_nicknames: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        try: arg[1]
        except:
            return await sendEmbed(c=clr_blue_state,
                    t='Использование:',
                    d='''
{0} [никнейм]

[?] Изменяет ваш никнейм. (Укажите вместо никнейма '!' для сброса).
                    '''.format(str(arg[0])),
                    a_name=mauth.name,
                    channel=chan
                    )
        try:
            if arg[1] == '!':
                await client.change_nickname(member=mauth, nickname=None)
                await client.add_reaction(m, 'react_success')
            else:
                await client.change_nickname(member=mauth, nickname=arg[1])
                await client.add_reaction(m, 'react_success')
            return True
        except discord.errors.Forbidden:
            await client.add_reaction(m, 'react_error')
            await client.add_reaction(m, 'react_forbiddenErr')
            return False
        except Exception as e:
            print(str(e))
            await client.add_reaction(m, 'react_error')
            await client.add_reaction(m, 'react_syntaxErr')
            return False

    if msg.startswith(p+'newname'):
        arg = msg.split(" ")
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.manage_nicknames: pass
        else:
            return await sendEmbed(chan, 
                            c=0xff0000, 
                            t='Команда не может быть выполнена.', 
                            d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.'
                            )

        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000
        try: arg[1]
        except:
            return await sendEmbed(c=clr_blue_state,
                    t='Использование:',
                    d='''
{0} <пользователь> [никнейм]

[?] Изменяет никнейм пользователя. (Укажите вместо никнейма '!' для сброса).
                    '''.format(str(arg[0])),
                    a_name=mauth.name,
                    a_avatar=mauth.avatar_url,
                    channel=chan
                    )
        
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)

        try:
            user = getUsername(arg[1], serv)
            if arg[2] == '!':
                await client.change_nickname(member=user, nickname=None)
                await client.add_reaction(m, 'react_success')
            else:
                await client.change_nickname(member=user, nickname=str(arg[2]))
                await client.add_reaction(m, 'react_success')
            return True
        except discord.errors.Forbidden:
            await client.add_reaction(m, 'react_error')
            await client.add_reaction(m, 'react_forbiddenErr')
            return False
        except Exception as e:
            print(str(e))
            await client.add_reaction(m, 'react_error')
            await client.add_reaction(m, 'react_syntaxErr')
            return False


    if msg.startswith(p+'anime'):
        args = msg.split(" ")
        anime_possible = ['avatar', 'neko', 'fox_girl', 'hug', 'pat']
        try: args[1].lower()
        except:
            await sendEmbed(c=clr_white_warm,
                        t='[!] Аниме ☆*:.｡.o(≧▽≦)o.｡.:*☆',
                        d='''
Доступные варианты:
{0} fox_girl
{0} avatar
{0} neko
{0} hug
{0} pat
                        '''.format(args[0]),
                        a_name=mauth.name,
                        channel=chan,
                        )
            return False
        if args[1].lower() not in anime_possible:
            await sendEmbed(c=clr_white_warm,
                        t='Аргумент {} не найден.'.format(args[1].lower()),
                        a_name=mauth.name,
                        channel=chan
                        )
        else:
            await sendEmbed(c=clr_white_warm,
                        t='Анимешная картинка:',
                        a_name=mauth.name,
                        i=str(nekos.img(args[1])),
                        channel=chan
                        )


    if msg.startswith(p+'warns'):
        arg = msg.split(' ')
        try: arg[1].lower()
        except:
            msg = await sendEmbed(c=clr_blue_state,
                    t='Использование:',
                    d='''
{} <пользователь>

[?] Показать кол-во предупреждений у пользователя.
                    '''.format(arg[0]),
                    a_name=mauth.name,
                    channel=chan
                    )
        else:
            
            target_user = getUsername(str(arg[1]), serv)
            userCfg = loadUser(serv, target_user)
        
            if userCfg['warns'] <= 0:
                return await sendEmbed(c=clr_white_warm,
                    t='Предупреждения (ノ°益°)ノ ',
                    d='''
                    Пользователь {} в данный момент не имеет предупреждений.
                    '''.format(arg[1]),
                    a_name=mauth.name,
                    a_avatar=mauth.avatar_url,
                    channel=chan
                    )
            else:
                return await sendEmbed(c=clr_white_warm,
                    t='Предупреждения (ノ°益°)ノ ',
                    d='''
                    Пользователь {0} в данный момент имеет {1} предупреждений(е).
                    '''.format(arg[1], userCfg['warns']),
                    a_name=mauth.name,
                    a_avatar=mauth.avatar_url,
                    channel=chan
                    )
        
        
    if msg.startswith(p+'warn'):
        arg = msg.split(" ")
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.kick_members: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        
        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000



        _username = ''
        _reason = ''
        
        try: arg[1].lower
        except:
            return await sendEmbed(c=color_,
                        t='Использование:',
                        d='''{0} <пользователь>

[?] Предупреждение - метод наказания. Если у пользователя наберется {1} предупреждений, я буду вынуждена отключить его от сервера.
                        '''.format(arg[0], cfg['max-warns']),
                        a_name=mauth.name,
                        channel=chan
                        )
        
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)

        else: _username = arg[1]
        try: arg[2].lower
        except: _reason = 'отсутствует.'
        else: _reason = ' '.join(arg[2:])
        
        target_user = getUsername(str(arg[1]), serv)
        userCfg = loadUser(serv, target_user)
        userCfg['warns'] += 1
        json.dump(userCfg, io.open(users(serv, target_user), 'w', encoding='utf8'))
        await client.add_reaction(m, 'react_success')
        await sendEmbed(c=clr_white_warm,
                    t='Предупреждения (ノ°益°)ノ ',
                    d='''
Я предупредила пользователя {0}.

Причина: {1}

Всего предупреждений: {2}'''.format(_username, _reason, userCfg['warns']),
                    a_name=mauth.name,
                    channel=chan
                    )

        if userCfg['warns'] >= cfg['max-warns']:
            try:
                await client.kick(target_user)
            except discord.errors.Forbidden:
                await send_me_permission_error(m)
            else:
                await sendEmbed(c=clr_red,
                    t='Отключение пользователя ｡ﾟ･ (>﹏<) ･ﾟ｡',
                    d='''
Я отключила от сервера пользователя {0} по причине последнего предупреждения ({1}).
Данный пользователь набрал {2} предупреждений, что является максимумом.
                    '''.format(_username, _reason, cfg['max-warns']),
                    a_name=mauth.name,
                    channel=chan
                    )
                userCfg['warns'] = 0
                return json.dump(userCfg, io.open(users(serv, target_user), 'w', encoding='utf8'))

    if msg.startswith(p+'unwarn'):
        arg = msg.split(" ")
        
        permissions = chan.permissions_for(mauth).kick_members
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000

        _username = ''
        _reason = ''
        
        try: arg[1].lower
        except:
            await sendEmbed(c=color_,
                        t='Использование:',
                        d='''{} <пользователь>

[?] Убрать одно предупреждение у пользователя.
                        '''.format(arg[0]),
                        a_name=mauth.name,
                        a_avatar=mauth.avatar_url,
                        channel=chan
                        )
            return False
        else: _username = arg[1]
        try: arg[2]
        except: _reason = 'отсутствует.'
        else: _reason = ' '.join(arg[2:])
        
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)

        user = str(_username).replace('>', "").replace('!', "").replace('@', "").replace('<', "")

        target_user = getUsername(user, serv)
        userCfg = loadUser(serv, target_user)
        
        if userCfg['warns'] >= 1:
            userCfg['warns'] -= 1
            json.dump(userCfg, io.open(users(serv, target_user), 'w', encoding='utf8'))
            await client.add_reaction(m, 'react_success')
            await sendEmbed(c=clr_green_spring,
                    t='Предупреждения (ノ°益°)ノ ',
                    d='''
Я сняла последнее предупреждение с пользователя {0}.

Причина: {1}

Всего предупреждений: {2}'''.format(_username, _reason, userCfg['warns']),
                    a_name=mauth.name,
                    a_avatar=mauth.avatar_url,
                    channel=chan
                    )
        else:
            await sendEmbed(c=clr_green_spring,
                    t='Предупреждения (ノ°益°)ノ ',
                    d='У пользователя {} нет предупреждений.'.format(_username),
                    a_name=mauth.name,
                    channel=chan
                    )


    if msg.startswith(p+'avatar'):
        arg = msg.split(' ')
        try: arg[1]
        except: pass
        else:
            target = getUsername(arg[1], serv)

            try:
                if target.avatar_url is None or target.avatar_url == '' or target.avatar_url == ' ':
                    return await client.send_message(chan, 'У {} нет аватарки...'.format(target.name))
                return await sendEmbed(c=clr_green_spring,
                            t='Аватар пользователя {}'.format(target.name),
                            i=target.avatar_url,
                            a_name=mauth.name,
                            channel=chan
                            )
            except AttributeError:
                await client.add_reaction(m, 'react_error')
                await client.add_reaction(m, 'react_syntaxErr')
                return False


    if msg.startswith(p+'mute'):
        arg = msg.split(" ")
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.manage_roles: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        
        try: arg[1]
        except: await sendEmbed(c=clr_green_spring,
                        t='Использование:',
                        d='''
{0} <пользователь>

[?] Приглушает пользователя (он не сможет отправлять сообщения).
                        '''.format(arg[0]),
                        a_name=mauth.name,
                        channel=chan
                        )
        else:
            author_perms = chan.permissions_for(mauth)
            if author_perms.manage_messages or mauth.id == '297421244402368522': pass
            else: return await send_permission_error(m)

            try:
                target_user = getUsername(arg[1], serv)

                userCfg = loadUser(serv, target_user)

                __ismuted__ = userCfg['mute']

                if __ismuted__ == False:
                    try:
                        targetr = getRole(cfg['mute-role'], serv)
                        
                        overwrite = discord.PermissionOverwrite()
                        overwrite.send_messages = False
                        overwrite.add_reactions = False
                        for c in serv.channels:
                            await client.edit_channel_permissions(c, targetr, overwrite)

                        await client.add_roles(target_user, targetr)
                        await client.add_reaction(m, 'react_success')
                        userCfg['mute'] = True
                        json.dump(userCfg, io.open(users(serv, target_user), 'w', encoding='utf8'))
                    except discord.errors.Forbidden:
                        await send_me_permission_error(m)
                        return False
                    except:

                        mute_role = await client.create_role(serv, name=cfg['mute-role'])

                        overwrite = discord.PermissionOverwrite()
                        overwrite.send_messages = False
                        overwrite.add_reactions = False
                        for c in serv.channels:
                            await client.edit_channel_permissions(c, mute_role, overwrite)

                        try:
                            await client.add_roles(target_user, mute_role)
                            await client.add_reaction(m, 'react_success')
                            userCfg['mute'] = True
                            json.dump(userCfg, io.open(users(serv, target_user), 'w', encoding='utf8'))
                        except Exception as e:
                            await client.send_message(chan, str(e))
                            return await client.add_reaction(m, 'react_error')
                else:
                    return await sendEmbed(c=clr_red,
                        d='Пользователь {} в данное время приглушен.'.format(target_user.mention),
                        a_name=mauth.name,
                        channel=chan
                        )
            except Exception as e:
                return await send_exception(exception=str(e), channel=chan)
                
            else:
                return await sendEmbed(c=clr_white_warm,
                        d='Я приглушила пользователя {}.'.format(target_user.mention),
                        a_name=mauth.name,
                        channel=chan
                        )


    if msg.startswith(p+'unmute'):
        arg = msg.split(" ")
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.manage_roles: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        
        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000

        try: arg[1]
        except:
            await sendEmbed(c=clr_blue_state,
                        t='Использование:',
                        d='''
'''+arg[0]+''' <пользователь>

[?] Пользователь снова сможет отправлять сообщения в чаты.
                        ''',
                        a_name=mauth.name,
                        a_avatar=mauth.avatar_url,
                        channel=chan
                        )
            return False
        else:

            if not permissions and not mauth.id == '297421244402368522':
                return await send_permission_error(m)

            try:
                
                target_user = getUsername(arg[1], serv)
                target_role = getRole(cfg['mute-role'], serv)

                userCfg = loadUser(serv, target_user)
                
                if userCfg['mute'] == False:
                    await sendEmbed(c=clr_red,
                        d='Пользователь {} и так имеет возможность использовать чаты.'.format(target_user.mention),
                        a_name=mauth.name,
                        channel=chan
                        )
                    return False
                else:
                    try:
                        await client.remove_roles(target_user, target_role)
                        userCfg['mute'] = False
                        json.dump(userCfg, io.open(users(serv, target_user), 'w', encoding='utf8'))
                    except AttributeError as err:
                        await send_exception(exception=str(err), channel=chan)
                        return False
            except discord.errors.Forbidden:
                await send_me_permission_error(m)
            else:
                await sendEmbed(c=clr_white_warm,
                        d='Пользователь {} снова может отправлять сообщения в чаты.'.format(target_user.mention),
                        a_name=mauth.name,
                        channel=chan
                        )

    
    if msg == p+'banlist':
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.ban_members: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        
        permissions = chan.permissions_for(mauth).manage_messages
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)

        try: bans = await client.get_bans(serv)
        except discord.errors.Forbidden:
            await client.add_reaction(m, 'react_error')
            await client.add_reaction(m, 'react_forbiddenErr')
            return False
        except Exception as e:
            await client.send_message(chan, e)
            await client.add_reaction(m, 'react_error')
            await client.add_reaction(m, 'react_syntaxErr')
            return False
        if len(bans) <= 0:
            return await client.send_message(chan, 'Забаненные пользователи отсутствуют.')
        bannedUsers = []
        for user in bans:
            bannedUsers.append(user.name)
        return await client.send_message(chan, 'Забаненные пользователи:\n{}'.format(', '.join(bannedUsers)))


    if msg == p+'server':
        infoboard = await setEmbed(
                    channel=chan, 
                    c=clr_white_warm, 
                    t='Сервер {}'.format(serv.name),
                    d=cfg['desc'],
                    i=cfg['banner'],
                    a_name=mauth.name,
                    th=serv.icon_url)
        if cfg['web'] != None: infoboard.add_field(name="Сайт:", value=cfg['web'])
        if cfg['vkgroup'] != None: infoboard.add_field(name="Группа ВК:", value=cfg['vkgroup'])
        return await client.send_message(chan, embed=infoboard)


    if msg == p+'serverinfo':
        infoboard = await setEmbed(
                    channel=chan, 
                    c=clr_white_warm, 
                    t='Информация о сервере {}'.format(serv.name),
                    a_name=mauth.name,
                    th=serv.icon_url)
        
        server_emojis = []
        for e in serv.emojis:
            server_emojis.append(e.name)
        em = ' '.join(server_emojis)
        emoji_list = em.replace('[', '')
        emoji_list = emoji_list.replace(']', '')
        emoji_list = emoji_list.replace(',', '')
        if len(server_emojis) < 1:
            emoji_list = 'Отсутствуют'
        iterated_emojis_list = emoji_list.split(" ")
        emojis_list_info = []
        for emoji in iterated_emojis_list:
            emojis_list_info.append(':'+str(emoji)+':')
        
        member_not_bot_counter = 0

        for member in serv.members:
            if member.bot:
                pass
            else:
                member_not_bot_counter += 1


        infoboard.add_field(name="Местные эмодзи:", value=str(', '.join(emojis_list_info)), inline=True)
        infoboard.add_field(name="Регион:", value=str(serv.region).upper(), inline=True)
        infoboard.add_field(name="ServerID:", value=str(serv.id), inline=True)
        infoboard.add_field(name="Владелец:", value=str(serv.owner.mention), inline=True)
        infoboard.add_field(name="Уровень верификации:", value=str(serv.verification_level), inline=True)
        infoboard.add_field(name="Основной канал:", value=str(serv.default_channel), inline=True)
        infoboard.add_field(name="AFK канал:", value=str(serv.afk_channel), inline=True)
        infoboard.add_field(name="Ожидание AFK:", value=str(serv.afk_timeout), inline=True)
        infoboard.add_field(name="Всего пользователей (и ботов):", value=str(serv.member_count), inline=True)
        infoboard.add_field(name="Обычных пользователей:", value=str(member_not_bot_counter), inline=True)
        infoboard.add_field(name="Сервер создан:", value=str(serv.created_at), inline=True)

        return await client.send_message(chan, embed=infoboard)


    if msg.startswith(p+'info'):
        arg = msg.split(' ')
        try: arg[1].lower()
        except:
            username = mauth
            userid = mauth.id
        else:
            username = getUsername(arg[1], serv)
            userid = username.id
        try:
            infoboard = await setEmbed(
                    channel=chan, 
                    c=clr_white_warm, 
                    t='Информация:', 
                    d=username.mention, 
                    a_name=username.name, 
                    th=username.avatar_url)
        except:
            await client.add_reaction(m, 'react_error')
            await client.add_reaction(m, 'react_syntaxErr')
            return False
        if username.bot:
            is_bot = 'Да'
        else:
            is_bot = 'Нет'
        infoboard.add_field(name="DiscordTag:", value=str(username), inline=True)
        infoboard.add_field(name="UserId:", value=str(userid), inline=True)
        infoboard.add_field(name="Является ботом:", value=is_bot, inline=True)
        infoboard.add_field(name="Аккаунт создан:", value=str(username.created_at), inline=True)
        return await client.send_message(chan, embed=infoboard)

    if msg.startswith(p+'ban'):
        arg = msg.split(' ')
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.ban_members: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')

        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000

        try: arg[1]
        except: return await sendEmbed(c=color_,
                    t='Использование:',
                    d='''
{} <пользователь>

[?] Да будет вознесен BanHammer над <пользователем> на этом сервере!
                    '''.format(arg[0]),
                    a_name=mauth.name,
                    channel=chan
                    )
        else:
            if not permissions and not mauth.id == '297421244402368522':
                return await send_permission_error(m)
            try:
                target_user = getUsername(user_name=arg[1], server=serv)
                await client.ban(target_user, delete_message_days=1)
            except discord.errors.Forbidden:
                await client.add_reaction(m, 'react_error')
                await client.add_reaction(m, 'react_forbiddenErr')
                return False
            except Exception as e:
                await client.send_message(chan, e)
                await client.add_reaction(m, 'react_error')
                await client.add_reaction(m, 'react_syntaxErr')
                return False
            else:
                await client.add_reaction(m, 'react_success')
                return True

    if msg.startswith(p+'kick'):
        arg = msg.split(' ')
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.kick_members: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        
        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000

        try: arg[1]
        except: return await sendEmbed(c=color_,
                    t='Использование:',
                    d='''
{} <пользователь>

[?] Выгнать пользователя с этого сервера.
                    '''.format(arg[0]),
                    a_name=mauth.name,
                    channel=chan
                    )
        else:

            if not permissions and not mauth.id == '297421244402368522':
                return await send_permission_error(m)

            try:
                target_user = getUsername(arg[1], serv)
                await client.kick(target_user)
            except discord.errors.Forbidden:
                await client.add_reaction(m, 'react_error')
                await client.add_reaction(m, 'react_forbiddenErr')
                return False
            except Exception as e:
                await client.send_message(chan, e)
                await client.add_reaction(m, 'react_error')
                await client.add_reaction(m, 'react_syntaxErr')
                return False
            else:
                await client.add_reaction(m, 'react_success')
                return True

    if msg.startswith(p+'unban'):
        arg = msg.split(' ')
        bot = chan.permissions_for(getUsername('452534618520944649', serv))
        if bot.ban_members: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')

        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000

        try: arg[1]
        except: return await sendEmbed(c=color_,
                    t='Использование:',
                    d='''
{} <пользователь>

[?] Снять великую печать бана с пользователя.
                    '''.format(arg[0]),
                    a_name=mauth.name,
                    channel=chan
                    )
        else:
            
            if not permissions and not mauth.id == '297421244402368522':
                return await send_permission_error(m)

            try:
                target_user = getUsername(user_name=arg[1], server=serv)
                await client.unban(serv, target_user)
            except discord.errors.Forbidden:
                await client.add_reaction(m, 'react_error')
                await client.add_reaction(m, 'react_forbiddenErr')
                return False
            except:
                await client.add_reaction(m, 'react_error')
                await client.add_reaction(m, 'react_syntaxErr')
                return False
            else:
                await client.add_reaction(m, 'react_success')
                return True


    if msg == p+'410':
        return await sendEmbed(t='Наш автобус отправляется в Ад!',c=0xf80101, i='https://j.gifs.com/WnrKoX.gif', f_text='Для поклонников "Бесконечного Лета"', channel=chan)


    if msg == client.user.mention or msg == p+'bot':
        em = await setEmbed(c=clr_green_spring,
                        t='Информация обо мне (◕‿◕)',
                        url='https://discordapp.com/oauth2/authorize?client_id=452534618520944649&scope=bot&permissions=301296759',
                        d='''
Обязательно посети: [наш Discord-сервер](https://discord.gg/ZQfNQ43) и [наш сайт](https://discord-ai.tk/)!!

Префикс для команд на этом сервере: {}
'''.format(p),
                        th=client.user.avatar_url,
                        a_name=mauth.name,
                        channel=chan
                        )
        em.add_field(name="Мой никнейм:", value=str(client.user.name), inline=True)
        em.add_field(name="Версия; Релиз:", value=Ai.version()+'; '+Ai.release(), inline=True)
        em.add_field(name="Мой DiscordTag:", value=str(client.user), inline=True)
        em.add_field(name="Разработчик:", value='[%s](http://akirasumato.ml/)' % (developer), inline=True)
        em.add_field(name="Язык программирования:", value='Python', inline=True)
        em.add_field(name="Версия Python; Discord.py:", value='[{0}](https://www.python.org/); [{1}](http://discordpy.readthedocs.io/en/latest/api.html)'.format(python_version(), discord.__version__), inline=True)
        em.add_field(name="Список всех доступных команд:", value=p+'help', inline=False)
        em.add_field(name="Помощь с кодом:", value='[Nightmare#7694](https://discord.gg/esEGUqS/)', inline=False)
        return await client.send_message(chan, embed=em)


    if msg.startswith(p+'config'):
        arg = msg.split(" ")

        permissions = chan.permissions_for(mauth).manage_messages
        if permissions or mauth.id == '297421244402368522':
            color_ = clr_blue_state
        else:
            color_ = 0xff0000

        try: arg[1]
        except:
            info = await setEmbed(c=color_,
                        t='Использование:',
                        d='''
{} <параметр> <значение>

[?] Позволяет настроить мой функционал под ваш сервер.
[?] Конфигурация доступна только для администратора сервера.
[?] Если у вас имеются права, доступные параметры будут показаны ниже.
                        '''.format(arg[0]),
                        a_name=mauth.name,
                        a_avatar=mauth.avatar_url,
                        channel=chan
                        )
            
            if permissions or mauth.id == '297421244402368522':
                info.add_field(name='Параметр `msg-prefix`:', value='"str" (Префикс команд | Любой символ или "default" для "Ai!")', inline=False)
                info.add_field(name='Параметр `mute-role`:', value='"str" (Названия(е) ролей(и) или "default" для "mute")', inline=False)
                info.add_field(name='Параметр `banner`:', value='"str" (Баннер сервера | Ссылка или "default" для None)', inline=False)
                info.add_field(name='Параметр `desc`:', value='"str" (Описание сервера | Текст или "default" для None)', inline=False)
                info.add_field(name='Параметр `vkgroup`:', value='"str" (Группа ВК (ссылка) | Текст или "default" для None)', inline=False)
                info.add_field(name='Параметр `web`:', value='"str" (Ссылка на сайт | Текст или "default" для None)', inline=False)
                info.add_field(name='Параметр `max-warns`:', value='"int" (Макс.кол-во варнов | Число или "default" для 10)', inline=False)
            return await client.send_message(chan, embed=info)
        author_perms = chan.permissions_for(mauth)
        if not permissions and not mauth.id == '297421244402368522':
            return await send_permission_error(m)
        if arg[1] == 'values':
            text = '''
msg-prefix: `{0}`
mute-role: `{1}`
banner: `{2}`
desc:
```{3}```
vkgroup: `{4}`
web: `{5}`
max-warns: `{6}`
role-permissions: `{7}`
allow-warn: `{8}`
allow-mute: `{9}`
allow-kick: `{10}`
allow-ban: `{11}`
            '''.format(cfg['msg-prefix'],cfg['mute-role'],cfg['banner'],cfg['desc'],cfg['vkgroup'],cfg['web'],cfg['max-warns'],cfg['role-permissions'],cfg['allow-warn'],cfg['allow-mute'],cfg['allow-kick'],cfg['ban'])
            return await sendEmbed(chan, clr_orange, t='Конфигурация', d=text, a_avatar=mauth.avatar_url, a_name=mauth.name)
        if arg[1] == 'msg-prefix':
            try: arg[2].lower()
            except:
                try: info = cfg['msg-prefix']
                except: info = dictonary['msg-prefix']
                await client.send_message(chan, 'Параметр "msg-prefix": `{0}`'.format(info))
                return False
            if arg[2] == 'default':
                cfg['msg-prefix'] = dictonary['msg-prefix']
                json.dump(cfg, open(json_fp,'w'))
            else:
                cfg['msg-prefix'] = ''.join(arg[2:])
                json.dump(cfg, open(json_fp,'w'))
            return await client.send_message(chan, 'Параметр "msg-prefix" теперь `{0}`'.format(cfg['msg-prefix']))

        if arg[1] == 'mute-role':
            try: arg[2]
            except:
                try: info = cfg['mute-role']
                except: info = dictonary['mute-role']
                await client.send_message(chan, 'Параметр "mute-role": `{0}`'.format(info))
                return False
            if arg[2] == 'default':
                cfg['mute-role'] = dictonary['mute-role']
                json.dump(cfg, open(json_fp,'w'))
            else:
                cfg['mute-role'] = ' '.join(arg[2:])
                json.dump(cfg, open(json_fp,'w'))
            return await client.send_message(chan, 'Параметр "mute-role" теперь `{0}`'.format(cfg['mute-role']))

        if arg[1] == 'desc':
            try: arg[2]
            except:
                try: info = cfg['desc']
                except: info = dictonary['desc']
                await client.send_message(chan, 'Параметр "desc": `{0}`'.format(info))
                return False
            if arg[2] == 'default':
                cfg['desc'] = dictonary['desc']
                json.dump(cfg, open(json_fp,'w'))
            else:
                cfg['desc'] = ' '.join(arg[2:])
                json.dump(cfg, open(json_fp,'w'))
            return await client.send_message(chan, 'Параметр "desc" теперь `{0}`'.format(cfg['desc']))

        if arg[1] == 'banner':
            try: arg[2]
            except:                 
                try: info = cfg['banner']
                except: info = dictonary['banner']
                await client.send_message(chan, 'Параметр "banner": `{0}`'.format(info))
                return False
            if arg[2] == 'default':
                cfg['banner'] = dictonary['banner']
                json.dump(cfg, open(json_fp,'w'))
            else:
                url = ''.join(arg[2])
                if not url.startswith('https://') and not url.startswith('http://'):
                    return await client.send_message(chan, 'Введите URL __ссылку на изображение__ или `default` для значения по умолчанию ({}).'.format(dictonary['banner']))
                cfg['banner'] = ' '.join(arg[2:])
                json.dump(cfg, open(json_fp,'w'))
            return await client.send_message(chan, 'Параметр "banner" теперь `{0}`'.format(cfg['banner']))
        
        if arg[1] == 'vkgroup':
            try: arg[2]
            except:
                try: info = cfg['vkgroup']
                except: info = dictonary['vkgroup']
                await client.send_message(chan, 'Параметр "vkgroup": `{0}`'.format(info))
                return False
            if arg[2] == 'default':
                cfg['vkgroup'] = dictonary['vkgroup']
                json.dump(cfg, open(json_fp,'w'))
            else:
                cfg['vkgroup'] = ' '.join(arg[2:])
                json.dump(cfg, open(json_fp,'w'))
            return await client.send_message(chan, 'Параметр "vkgroup" теперь `{0}`'.format(cfg['vkgroup']))
        
        if arg[1] == 'web':
            try: arg[2]
            except:
                try: info = cfg['web']
                except: info = dictonary['web']
                await client.send_message(chan, 'Параметр "web": `{0}`'.format(info))
                return False
            if arg[2] == 'default':
                cfg['web'] = dictonary['web']
                json.dump(cfg, open(json_fp,'w'))
            else:
                cfg['web'] = ' '.join(arg[2:])
                json.dump(cfg, open(json_fp,'w'))
            return await client.send_message(chan, 'Параметр "web" теперь `{0}`'.format(cfg['web']))
        
        if arg[1] == 'max-warns':
            try: arg[2]
            except:
                try: info = cfg['max-warns']
                except: info = dictonary['max-warns']
                await client.send_message(chan, 'Параметр "max-warns": `{0}`'.format(info))
                return False
            if arg[2] == 'default':
                cfg['max-warns'] = dictonary['max-warns']
                json.dump(cfg, open(json_fp,'w'))
            else:
                try: cfg['max-warns'] = int(arg[2])
                except: return await client.send_message(chan, 'Параметр "max-warns" не удалось изменить.')
                json.dump(cfg, open(json_fp,'w'))
            return await client.send_message(chan, 'Параметр "max-warns" теперь `{0}`'.format(cfg['max-warns']))
            
        
    if msg.startswith(p+'stop'):
        try:
            voice_client = client.voice_client_in(serv)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(chan, 'Я не нахожусь в голосовом канале.')
        except:
            return False


    if msg.startswith(p+'play'):
        try:
            channel = mauth.voice.voice_channel
            bot = channel.permissions_for(getUsername('452534618520944649', serv))
        except:
            return await client.send_message(chan, 'Подключитесь к голосовому каналу перед использованием команды.')
        if bot.connect and bot.speak: pass
        else: return await sendEmbed(chan, c=0xff0000, t='Команда не может быть выполнена.', d='У меня отсутствуют все \nнеобходимые права для выполнения \nданной команды.')
        arg = msg.split(' ')
        try: arg[1]
        except: return await client.send_message(chan, 'Введите ссылку.')

        player_options = {
            'default_search': 'auto',
            'quiet': True,
        }

        try:
            if not discord.opus.is_loaded():
                discord.opus.load_opus('opus')
            try:
                voice_client = client.voice_client_in(serv)
                await voice_client.disconnect()
            except AttributeError:
                pass
            try:
                voice = await client.join_voice_channel(channel)
            except discord.errors.InvalidArgument:
                return await client.send_message(chan, 'Подключитесь к голосовому каналу перед использованием команды.')
            try:
                try:
                    await voice_client.disconnect()
                    await client.join_voice_channel(channel)
                except: pass

                url_ = ' '.join(arg[1:]).replace('<', '').replace('>', '').replace('`', '')
                
                try:
                    player = await voice.create_ytdl_player(url=url_, ytdl_options=player_options)
                    player.start()
                except Exception as e:
                    return client.send_message(chan, 'Попробуйте еще раз.\n{}'.format(e))

                text = '''
Запрос: %s
Видео: %s
Просмотры: %s
Лайки: %s
Дизлайки: %s
Длительность: %s
Дата публикации: %s
Опубликовал: %s
                ''' % (url_,player.title,player.views,player.likes,player.dislikes,player.duration,player.upload_date,player.uploader)
                await sendEmbed(chan, clr_white_warm, 'Музыка', d=text)
            except Exception as e:
                await client.send_message(chan, '{}'.format(e))
                return await client.add_reaction(m, 'react_error')
        except Exception as e:
            await client.send_message(chan, '{}'.format(e))
            return await client.add_reaction(m, 'react_error')

@client.event
async def on_channel_delete(channel):
    print('{0} ### Удален канал {1}'.format(channel.server, channel.name))

@client.event
async def on_channel_create(channel):
    print('{0} ### Создан канал {1}'.format(channel.server, channel.name))

@client.event
async def on_member_remove(member):
    print('{0} ### Пользователь {1} вышел.'.format(member.server, member.name))

@client.event
async def on_member_ban(member):
    print('{0} ### Пользователь {1} забанен.'.format(member.server, member.name))

@client.event
async def on_member_unban(member):
    print('{0} ### Пользователь {1} разбанен.'.format(member.server, member.name))

@client.event
async def on_server_remove(server):
    print('$$$ Меня убрали с сервера {0} - {1}! :('.format(server.name, server.id))

@client.event
async def on_member_join(member):
    print('### Присоединился {0} к серверу {1}'.format(member.name, member.server))

    ### ВОЗВРАТ РОЛИ МУТА ###

    try: role_for_mute = cfg['mute-role']
    except: role_for_mute = dictonary['mute-role']
    mute_role = getRole(names=role_for_mute, server=member.server)
    userCfg = loadUser(member.server, member)

    if userCfg['mute'] == True:
        print('### Пользователь {0} получил мут на сервере {1} после перезахода.'.format(member, member.server))
        return await client.add_roles(member, mute_role)


@client.event
async def on_ready():

    print('Discord-Бот Ай [Re-Created]\nРазработчик AkiraSumato_01 (aka Ram).')
    print('Я - {0} | {1}'.format(client.user, client.user.id))
    print('------------------------------------')
    print('Я в онлайне уже на {0} серверах :$'.format(len(client.servers)))
    print('------------ Exceptions ------------')
    #await client.change_presence(game=discord.Game(name='на свой стремный код.', type=3), status='online')
    await client.change_presence(game=discord.Game(name='ничто!', type=1), status='dnd')

try:
    client.run('NDUyNTM0NjE4NTIwOTQ0NjQ5.DhQOCw.wm4KRIqHXYBeZxR1nwgmvaqqRK0')
except:
    print('Подключение к Discord не удалось.')