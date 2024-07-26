import os
from datetime import datetime

from dotenv import load_dotenv
from pytz import timezone

load_dotenv()

CHAT_ID = "@yandex_b_notifications"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
STANDINGS_PAGES = [
    "https://algocode.ru/standings_data/b_fall_2023/",
    "https://algocode.ru/standings_data/b_spring_2024/"
]
time_now = lambda: datetime.now(tz=timezone("Europe/Moscow"))
ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'YA', 'YZ')


class CONFIG:
    filename = f'archive/{time_now().strftime("%m-%d")}'
    data = {}
    old_data = {}
    users = {}
    user_id_by_name = {}
    page_authors = {}


messages = [
    ({"verdict": "(RT)|(TL)|(PE)|(WA)", "penalty": "1"}, [
        "*{name}* [начал/начала] работать над задачей *{task}*, но [понял/поняла], что не может найти подходящее решение.",
        "Стоило подумать, а не сразу отсылать свой код. У *@{name} gent@* первый штраф по задаче *{task}*",
        "Ой, *{name}* [решил/решила] отправить код без компиляции. Первый штраф за *{task}* уже в кармане.",
        "*{name}*, [взялся/взялась] за задачу *{task}*, но [осознал/осознала], что не стоило писать код в блокноте.",
        "*{name}*, [приступил/приступила] к задаче *{task}*, но [застрял/застряла] в раздумьях.",
        "Не спеши, *{name}*, подумай еще раз перед отправкой кода. Штраф за неверную посылку по задаче *{task}* уже прилетел.",
        "Казалось бы, простая задача... Но видимо не для всех. *{name}* [получил/получила] свой первый штраф за задачу *{task}*",
        "*{name}* [старался/старалась], [писал/писала] код... И все это ради того, чтобы получить *{verdict}* по задаче *{task}*",
        "Снова неудача! *{name}* не [смог/смогла] сдать задачу *{task}* с первой попытки",
        "*{name}* [решил/решила], что *{verdict}* по задаче *{task}* [ему/ей] нравится больше, чем *OK*",
        "*{name}* наверняка [хотел/хотела] получить OK но [получил/получила] *{verdict}*"
    ]),
    ({"verdict": "SV", "penalty": "1"}, [
        "Как обидно! *{name}* по задаче *{task}* [получил/получила] ошибку оформления"
    ]),
    ({"verdict": "OK", "penalty": "0"}, [
        "*{name}* [уничтожил/уничтожила] задачу *{task}* с первой попытки!",
        "*{name}* [сдал/сдала] задачу *{task}* с первой попытки. Наверное, [ему/ей] просто повезло...",
        "*{name}* мастерски [справился/справилась] с задачей *{task}* с первого раза.",
        "[Ученик/Ученица] *{name}* успешно [решил/решила] задачу *{task}* с первой попытки."
    ]),
    ({"verdict": "OK", "penalty": "[1-9][0-9]*"}, [
        "*{name}* сдал задачу *{task}* после {penalty} неверных посылок.",
        "*{name}*, изворачиваясь как [кот/кошка], [смог/смогла] поймать задачу *{task}* с %{penalty} попытка ablt%, будто это нить из клубка.",
        "Задача *{task}* не могла пройти мимо *@{name} gent@*, так что [он/она] ее решил после %{penalty} попытка gent%, словно с чашкой кофе в руках.",
        "*{name}* [решил/решила] задачу *{task}* с %{penalty} попытка ablt%, и [его/ее] успех был таким громким, что можно было услышать аплодисменты по всему кружку.",
        "Задача *{task}* пыталась противостоять *@{name} datv@*, но [он/она] с %{penalty} попытка ablt% [доказал/доказала] ей, кто здесь настоящий босс.",
        "[Ученик/Ученица] *{name}*, с %{penalty} попытка ablt% на счету, без проблем [разгадал/разгадала] задачу *{task}*, и даже сервера восторженно аплодировали.",
        "*{name}*, с %{penalty} попытка ablt% в запасе, [покорил/покорила] задачу *{task}*, словно владелец клавиатуры-танка.",
        "Задача *{task}* пыталась сбежать от *@{name} gent@*, но после %{penalty} попытка gent% [он/она] ее настиг и решил с легкостью.",
        "[Ученик/Ученица] *{name}*, с %{penalty} попытка ablt%, [справился/справилась] с задачей *{task}* так легко, словно это была задачка для младших классов.",
        "[Ученик/Ученица] *{name}*, несмотря на %{penalty} ошибка accs%, успешно [выполнил/выполнила] задание *{task}*.",
        "[Ученик/Ученица] *{name}*, с %{penalty} попытка ablt%, гениально [выполнил/выполнила] таску *{task}*."
    ]),
    ({"verdict": "(RT)|(TL)|(PE)|(WA)", "penalty": "[1-9][0-9]*0"}, [
        "Бесконечность не предел! У *@{name} gent@* уже %{penalty} посылка gent% по задаче *{task}*.",
        "У *@{name} gent@* только что стало %{penalty} посылка gent% по задаче *{task}*. Может [ему/ей] стоило выбрать географию, а не программирование?",
        "У *@{name} gent@* только что стало %{penalty} посылка gent% по задаче *{task}*. Может [ему/ей] стоило выбрать русский, а не программирование?",
        "*{name}* получает %{penalty} штраф accs% по задаче *{task}*. Кажется, пора забрать у [него/нее] ноутбук.",
        "*{name}* никак не может справиться с вердиктом *{verdict}* в задаче *{task}*. У [него/нее] уже %{penalty} посылка nomn%!",
        "Помогите *@{name} datv@*, [он/она] не справляется с задачей *{task}*! У [него/нее] уже %{penalty} штраф nomn%!"
    ]),
    ({"verdict": "PR"}, [
        "Задача *{task}* у *@{name} gent@* ожидает подтверждения. Ждём..."
    ])
    ({"verdict": "RJ"}, [
        "*{name}* получил БАН по задаче *{task}*",
        "О нет! *@{name} datv@* забанили задачу *{task}*!"
    ])
    ({"verdict": "CE", "penalty": "1"}, [
        "Ошибка компиляции у *@{name} gent@* в задаче *{task}*. Нужно компилировать код перед отправкой."
    ])
]


# TODO: autoloading with cutting
title_replacements = {
    'Графы 6': 'Графы 6',
    'Неточные алгоритмы': 'Неточки',
    'Строки 3 🧶': 'Строки 3 🧶',
    'Персистентность': 'Персистентность',
    'Декартово дерево 🤮': 'Декартово дерево 🤮',
    'Математика 🤢': 'Математика 🤢',
    'Паросочетания 👫': 'Паросочетания 👫',
    'Теория игр 🤓': 'Теория игр 🤓',
    'Геометрия 2': 'Геометрия 2',
    'Теория игр 🤓': 'Теория игр 🤓',
    'Геометрия 2': 'Геометрия 2',
    'Корневая декомпозиция': 'Корнячка',
    'Графы 4': 'Графы 4',
    'Геометрия 1': 'Геометрия 1',
    'Графы 3': 'Графы 3',
    'Динамическое программирование 2': 'ДП 2',
    'Дерево отрезков 2': 'ДО 2',
    'Дерево отрезков 1': 'ДО 1',
    'Динамическое программирование 1': 'ДП 1',
    'Графы 2': 'Графы 2',
    'Задачи с двойным запуском': 'Двойной запуск',
    'Бинарный и тернарный поиск. Интерактивные задачи': 'Поиски+Интерактивки',
    'Теория чисел': 'ТЧ',
    'C++, стресс-тестирование и дебаг': 'Дебаг',
    'Строки 2': 'Строки 2',
    'Строки 1': 'Строки 1',
    'Графы 1': 'Графы 1'
}

reversed_title_replacements = {value: key for key, value in title_replacements.items()}

first_solve_message = "⚡ *{name}* [стал/стала] [первым/первой], кто решил задачу *{task}*!"

first_solves_message = """Первые решившие задачу *{task}*:
🥇{first}
🥈{second}
🥉{third}"""