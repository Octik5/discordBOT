import disnake #pip install disnake
from disnake.ext import commands
import random
from googletrans import Translator #pip install googletrans
# yt_dlp

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())


@bot.slash_command(description='Приветственное сообщение')
async def welcome(ctx: disnake.AppCmdInter):
    embed = disnake.Embed(
        title="Привет",
        description="""
Добро пожаловать на наш дискорд сервер!

Мы рады приветствовать тебя здесь, в нашей дружелюбной и активной сообществе! Этот сервер предназначен для общения, обмена идеями, совместной игры и развлечений. У нас есть различные каналы для обсуждения разных тем, а также специальные голосовые каналы для групповых игр и разговоров.

Мы призываем всех участников соблюдать правила сервера, быть уважительными и толерантными друг к другу. Здесь каждый может найти единомышленников, делиться своими интересами и просто хорошо провести время в приятной компании.

Если у тебя возникнут вопросы или нужна помощь, не стесняйся обратиться к нашей команде модераторов. Мы всегда готовы помочь и поддержать.

Так что добро пожаловать в наше сообщество! Присоединяйся к нам, заводи новых друзей и наслаждайся приятной атмосферой, которую мы создаем вместе.""",
        color=disnake.Color.blue()
    )
    embed.add_field(name="Выберите роли которые вас интересуют", value=" ", inline=False)
    embed.add_field(name="Гость", value="🌗", inline=False)
    embed.add_field(name="Просто кент", value="🌘", inline=False)
    embed.add_field(name="Шнырь", value="🌑", inline=False)
    embed.add_field(name="Вы всегда можете вступить в нашу семью", value="[Заявки в семью](https://discord.gg/B8vFg3uf)", inline=False)
    embed.set_image(url="https://sun1-19.userapi.com/impg/8vOqjKQblrTGN7xP47Yely7g5YQj2ISaudCvdw/N880ZoJiUHY.jpg?size=1952x1098&quality=95&sign=f393ac41424fe22a4227e3e7907b7581&type=album")

    message = await ctx.send(embed=embed)

    emoji_roles = {
        "🌗": "Гость",
        "🌘": "Просто кент",
        "🌑": "Шнырь",
    }
    for emoji in emoji_roles.keys():
        await message.add_reaction(emoji)  # Используйте add_reaction вместо create_reaction



@bot.slash_command(description='Отправить сообщение в личные сообщения по роле')
async def send_dm_to_role(ctx: disnake.AppCmdInter, role: disnake.Role, *, message: str):
    members_with_role = [member for member in ctx.guild.members if role in member.roles]
    for member in members_with_role:
        try:
            mention = member.mention  # Mention the user in the message
            await member.send(f"{mention}")
            embed = disnake.Embed(
                title=message,

                color=disnake.Color.orange()
            )
            await member.send(embed=embed)
        except disnake.errors.HTTPException:
            print(f"Не удалось отправить сообщение {member.display_name}")

    await ctx.send(f"Отправил сообщение {len(members_with_role)} участникам с роль {role.name}")



@bot.slash_command(description='Создать новость')
async def news(ctx: disnake.AppCmdInter, *, news: str):

    embed = disnake.Embed(
        title="Новости!",
        description=news,
        color=disnake.Color.green()
    )

    news_message = await ctx.send(embed=embed)

@bot.slash_command(description='Создать голосование')
async def vote(ctx: disnake.AppCmdInter, *, event: str):
    embed = disnake.Embed(
        title="Голосование",
        description=event,
        color=disnake.Color.green()
    )

    message = await ctx.send(embed=embed)
    await message.add_reaction("👍")  # Добавление реакции на сообщение
    await message.add_reaction("👎")  # Добавление реакции на сообщение

@bot.slash_command(description='Оповищение о наборе в семью')
async def famq(ctx: disnake.AppCmdInter):
    embed = disnake.Embed(
        title="И снова привет",
        description="У тебя есть хорошая возможность вступить в нашу семью, подавай заявку прямо сейчас и мы сразу же её рассмотрим",
        color=disnake.Color.yellow()
    )
    embed.add_field(name="Ссылка на Google Forms", value="[GoogleForms](https://www.google.ru/forms/about/)",inline=False)
    message = await ctx.send(embed=embed)
    await message.add_reaction("👍")  # Добавление реакции на сообщение
    await message.add_reaction("👎")  # Добавление реакции на сообщение

@bot.slash_command(description='Заглушает участника на сервере')
async def mute(ctx: disnake.AppCmdInter, user: disnake.Member):
    # Проверяем, является ли пользователь автором команды или ботом
    if user == ctx.author or user.bot:
        await ctx.send("Вы не можете замутить этого пользователя.")
        return

    # Получаем роль "Мут" или создаем новую роль, если она не существует
    mute_role = disnake.utils.get(ctx.guild.roles, name="Мут")
    if not mute_role:
        mute_role = await ctx.guild.create_role(name="Мут", reason="Роль для замьюченных пользователей")

    # Замьючиваем пользователя, добавляя ему роль "Мут"
    await user.add_roles(mute_role)
    await ctx.send(f"Пользователь {user.mention} замьючен.")

@bot.slash_command(description='нашивка')
async def nashivka(ctx: disnake.AppCmdInter):
    embed = disnake.Embed(
        title="На правой ноге офицера висит жетон [ HP - Octavius Gorsky 74696 ].",
        description="На правой ноге офицера висит жетон [ HP - Octavius Gorsky 74696 ].",
        color=disnake.Color.purple()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction("👍")  # Добавление реакции на сообщение
    await message.add_reaction("👎")  # Добавление реакции на сообщение


@bot.slash_command(description='Рандомайзер')
async def roll(ctx: disnake.AppCmdInter, min_value: int, max_value: int):
    if min_value >= max_value:
        await ctx.send("Неверный диапазон. Минимальное значение должно быть меньше максимального.")
        return

    random_number = random.randint(min_value, max_value)
    await ctx.send(f"Случайное число в диапазоне от {min_value} до {max_value}: {random_number}")

@bot.slash_command(description='Переводчик')
async def translate(ctx: disnake.AppCmdInter, *, text: str):
    translator = Translator()
    translation = translator.translate(text, dest='ru')

    await ctx.send(f"Перевод: {translation.text}")


@bot.slash_command(description='Все доступные команды бота')
async def helpp(ctx: disnake.AppCmdInter):
    embed = disnake.Embed(
        title="Bot команды",
        description="Вот список доступных команд:",
        color=disnake.Color.gold()
    )
    embed.add_field(name="*/helpp*", value="Информация по командам.", inline=False)
    embed.add_field(name="*/welcome*", value="Отображает приветственное сообщение и роли реагирования.", inline=False)
    embed.add_field(name="*/send_dm_to_role <role> <message>*", value="Отправляет прямое сообщение указанному пользователю с определенной ролью.", inline=False)
    embed.add_field(name="*/vote <event>*", value="Запускает сессию голосования по указанному событию.", inline=False)
    embed.add_field(name="*/famq*", value="Предоставляет ссылку для заполнения заявки в Google Form.", inline=False)
    embed.add_field(name="*/mute <user>*", value="Отключает звук у указанного пользователя.", inline=False)
    embed.add_field(name="*/nashivka*", value="Отображает информацию о конкретном значке.", inline=False)
    embed.add_field(name="*/news <news>*", value="Запускает новостную сессию по указанной информации.", inline=False)
    embed.add_field(name="*/roll <min_value> <max_value>*", value="Рандомайзер для вывода рандомного числа из пользовательского диапазона.", inline=False)
    embed.add_field(name="*/translate <text>*", value="Переводчик работающий по принципу автоопределения языка в <text> и выдающий результат на русский.", inline=False)
    embed.add_field(name="*/play <url> (на данный момент не работает!)*",value="Воспроизведение музыки через url youtube видео.",inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name="/helpp"))

@bot.event
async def on_raw_reaction_add(payload: disnake.RawReactionActionEvent):
    if payload.member.bot:
        return

    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = channel.guild
    user = guild.get_member(payload.user_id)

    emoji_roles = {
        "🌗": "Гость",
        "🌘": "Просто кент",
        "🌑": "Шнырь",
    }
    role = emoji_roles.get(payload.emoji.name)

    if role:
        target_role = disnake.utils.get(guild.roles, name=role)
        await user.add_roles(target_role)



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run('TOKEN')