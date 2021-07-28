# - *- coding: utf- 8 - *-
#Язык разметки html
import telebot, random, config, wikipedia, pyshorteners, google_trans_new, time, rabom_keyboard, uuid, logging, os
from pyowm import OWM
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from googletrans import Translator
from functools import wraps
s = pyshorteners.Shortener()
wikipedia.set_lang('ru')
translator = Translator()
owm = OWM(config.API_KEY)
owm.config['language'] = 'ru' 
mgr = owm.weather_manager()


os.system('clear')
os.system('CLS')

#Выбор токена
version = int(input('Введите версию бота 1 или 2: '))
if version == 1:
	bot = telebot.TeleBot(config.API)
elif version == 2:
	bot = telebot.TeleBot(config.API1)

#Логги
f = open('rabom.txt', 'w')
f.close()
logging.basicConfig(filename='rabom.txt',level=logging.INFO, format = '%(asctime)s - %(message)s')
logging.info('Rabom started...')

#Переменные
admin_id = 1299393358 
moderator_id = -1001150368805
testers_id = [847595841, 1299393358, 827868931, 912994315]
users_id = [827868931, 731320294, 411222522, 967800364, 912994315, 84759584, 660463075, 967800364, 1433106866, 1340176765, 1786996290, 738452716, 865008475, 818152404]

filter_inf = ['√','π','∆']
filter_group = ['/chat_id', '/log_mode', '/chat_id@sjsjsjslfjaa_bot', '/logg_info']
global user_id;
global name;
global username;
global message_to_admin;
global rule;
global balance;
global token;
global anekdot;
global town;
global result_rus;
global url;
global inf;
logging.info( u'All variables are created' )

#Чёрный список
banned_users = []
def is_not_banned(func):
    @wraps(func)
    def decorator(message):
        if message.from_user.id not in banned_users and message.chat.id > 0 or message.text in filter_group:
        	return func(message)
    return decorator
@bot.message_handler(commands=['ban'])
def ban_user(message):
    message_args = message.text.split()
    if len(message_args) == 3 and message.chat.id == admin_id:
        prichin = message_args[2]
        banned_users.append(int(message_args[1]))
        bot.reply_to(message, text='OK')
        bot.send_message(message_args[1],f'Вам выдан бан🚫\n😬Причина: {prichin}')
    else:
        bot.reply_to(message, text='Ты не достоин')
       
@bot.message_handler(commands=['unban'])
def unban_user(message):
    message_args = message.text.split()
    if len(message_args) == 2 and message.chat.id == admin_id:
        banned_users.pop()
        bot.reply_to(message, text='OK')
        bot.send_message(message_args[1],'Вам выдан разбан✅')
    else:
        bot.reply_to(message, text='Ты не достоин')

#Выдача роли тестера
@bot.message_handler(commands=['tester'])
def tester_user(message):
    message_args = message.text.split()
    if len(message_args) == 2 and message.chat.id == admin_id:
        testers_id.append(int(message_args[1]))
        bot.reply_to(message, text='OK')
        bot.send_message(message_args[1],'Вам выдана роль tester🔧\nЧат тестеров👇🏻\nhttps://t.me/joinchat/iSM0tf8rU2EwNjZi')
    else:
        bot.reply_to(message, text='Ты не достоин')

#Команды
@bot.message_handler(commands = ['start','help', 'menu', 'id', 'set', 'token', 'log_mode', 'chat_id', 'dior', 'leon', 'akeno', 'chel', 'jenenka', 'logg_info'])
@is_not_banned
def command_message(message):
	anekdot = random.randint(1,2)
	if message.text == "/start" and message.chat.id not in users_id:
		bot.send_message(message.chat.id,'Добро пожаловать!\nНапиши /help чтобы узнать о моих функциях',reply_markup = rabom_keyboard.menu_keyboard())
		user_id = str(message.chat.id)
		username = str(message.from_user.username)
		bot.send_message(moderator_id,f'Новый пользователь!\n💳id: {user_id}\n🚹username: @{username}')
		users_id.append(message.chat.id)
		bot.send_message(message.chat.id,'Теперь ты зарегистрирован!')
	elif message.text == "/start" and message.chat.id in users_id:
		bot.send_message(message.chat.id,'Ты уже зарегистрирован!')
	elif message.text == "/help":
		bot.send_message(message.chat.id,'Привет, вот что я могу:\n/help - <b>помощь, выдаёт список то чего я могу.</b>\n/set - <b>ввод максимального рандомного числа</b>\n/token - <b>ваш уникальный токен</b>\n🎲random number - <b>выдаёт рандомное число от 0 до вашего лимита.</b>\n👤Профиль - <b> выдаёт твой профиль</b>\n🔎Найти информацию  - <b>ищет информацию по ключевым словам из wiki</b>\n🔗Сократить ссылку - <b>сокращает введёную ссылку</b>\n📜Перевод - <b>переводит ваш текст</b>'.format(message.from_user, bot.get_me()),
		parse_mode = 'html')
	elif message.text == '/menu':
		bot.send_message(message.chat.id,'Кнопки выданы!', reply_markup = rabom_keyboard.menu_keyboard())
	elif message.text == '/id':
		bot.send_message(message.chat.id,str(message.chat.id))
	elif message.text == '/set':
		bot.send_message(message.chat.id,'Введите максимальное число которое может выпасть: ')
		bot.register_next_step_handler(message, get_max_random);
	elif message.text == '/token':
		token = uuid.uuid4()
		bot.send_message(message.chat.id,str(token))
	elif message.text == '/log_mode' and message.chat.id < 0:
		bot.send_message(moderator_id,'loggs notification ON!', reply_markup = rabom_keyboard.log_keyboard())
	elif message.text == '/chat_id' and message.chat.id < 0 or message.text == '/chat_id@sjsjsjslfjaa_bot' and message.chat.id < 0:
		bot.send_message(message.chat.id,str(message.chat.id))
	elif message.text == '/dior':
		audio = open(r'Dior.mp3', 'rb')
		time.sleep(0.05)
		bot.send_audio(message.chat.id, audio)
		audio.close()
	elif message.text == '/leon':
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECMu5gfFYa8h6XKaazzv6REimWtItprgAClQwAAi5S6EshuUSRit3omx8E')
		time.sleep(1)
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECMu9gfFYbTQHGcrhVv_eew2cNKyTAAgAC1Q8AApr66EszPtrYyTmWER8E')
	elif message.text == '/akeno':
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECMwRgfF1N69dWT4v5rrKglOSvb5RPTQAClAwAAk_e4Utdfn-I0qDfcx8E')
		time.sleep(1)
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECMwJgfF1LHDjlguDUU2Lm6PX-NMgJeQACHg4AAt0L6EvZUWw6gK5a9R8E')
		time.sleep(1)
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECMwFgfF1K37p0uOIo-AR71L0eqsPHPgACeAwAAkYL4EvBjYm7c0Cfrh8E')
	elif message.text == '/chel':
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECMwVgfF1NBoIpLZXrfEM5Pvf8p-1NSAAC8Q0AAvB96Es7496FzVRTDR8E')
	elif message.text == '/logg_info' and message.chat.id < 0:
		f = open('rabom.txt', 'r')
		bot.send_message(moderator_id, f.read(3500))
		f.close()
	
#Команды на кнопки
@bot.message_handler(content_types = ['text'])
@is_not_banned
def text_button_message(message):
	rule = 'user';
	balance = 0
	if message.text == '🎲Random number':
		try:
			bot.send_message(message.chat.id,str(random.randint(0,mr)))
		except:
			bot.send_message(message.chat.id,'Ты не ввёл максимальное число которое тебе может выпасть ヽ(｡◕o◕｡)ﾉ')
			bot.send_message(message.chat.id,'Используй команду /set')
	elif message.text == '👤Профиль' and message.chat.id in testers_id:
		username = str(message.from_user.username)
		user_id = str(message.chat.id)
		bot.send_message(message.chat.id,f'👤Имя: @{username}\n📂Права: tester🔧\n💳id: {user_id}\n💰Баланс: {balance} \nПользователей в боте: '+str(len(users_id)))
	elif message.text == '👤Профиль' and message.chat.id not in testers_id:
		username = str(message.from_user.username)
		user_id = str(message.chat.id)
		bot.send_message(message.chat.id,f'👤Имя: @{username}\n📂Права: {rule}\n💳id: {user_id}\n💰Баланс: {balance} \nПользователей в боте: '+str(len(users_id)))
	elif message.text == '🔎Найти информацию':
		if message.text not in filter_inf:
			bot.send_message(message.chat.id,'Введите ключевые слова', reply_markup = rabom_keyboard.demenu_v2_keyboard())
			bot.register_next_step_handler(message, get_inf);
	elif message.text == '🏠Меню':
		bot.send_message(message.chat.id,'Вы вернулись в меню.', reply_markup = rabom_keyboard.menu_keyboard())
	elif message.text == '🔗Сократить ссылку':
		bot.send_message(message.chat.id,'Введите ссылку:')
		bot.register_next_step_handler(message, get_url);
	elif message.text == '📜Перевод':
		bot.send_message(message.chat.id,'Вы перешли в меню перевода', reply_markup = rabom_keyboard.translate_keyboard())
	elif message.text == '◀️Назад':
		bot.send_message(message.chat.id,'Вы вернулись назад.', reply_markup = rabom_keyboard.translate_keyboard())
	elif message.text == '🔤Языки перевода':
		bot.send_message(message.chat.id,'Выберите языки!\n<b>Нажмите на кнопку с названием языка, который хотите сменить.</b>\n\n<b>Слева</b> - язык сообщения, которое Вы отправили.\n\n<b>Справа</b> - язык, на который нужно перевести.'.format(message.from_user, bot.get_me()),
		parse_mode = 'html', reply_markup = rabom_keyboard.my_lang_keyboard())
	elif message.text == '➡️Перевести':
		try:
			bot.send_message(message.chat.id,f'{talang} ➡️ {talangq}\n\nВведите текст: ', reply_markup = rabom_keyboard.demenu_keyboard())
			bot.register_next_step_handler(message, get_text);
		except:
			bot.send_message(message.chat.id, 'Вы не выбрали язык👅')
	elif message.text == '⚙Настройки':
		bot.send_message(message.chat.id,'Вы перешли в ⚙Настройки', reply_markup = rabom_keyboard.settings_keyboard())
	elif message.text == '⛅Погода':
		bot.send_message(message.chat.id,'Введите город ( ･ω･)☞\n(погоду в котором хотите узнать)')
		bot.register_next_step_handler(message, get_town);
	elif message.text == '🔔Сообщение для администрации':
		bot.send_message(message.chat.id,'✏️Введите ваше сообщение:')
		bot.register_next_step_handler(message, get_send);
	elif message.text == '📟Перевод двоичного кода':
		bot.send_message(message.chat.id,'❓Выберите путь', reply_markup = rabom_keyboard.code_keyboard())
	elif message.text == 'Текст в код':
		bot.send_message(message.chat.id,'✏️Введите ваш текст:')
		bot.register_next_step_handler(message, get_code_text);
	elif message.text == 'Код в текст':
		bot.send_message(message.chat.id,'✏️Введите ваш код:')
		bot.register_next_step_handler(message, get_code);
	elif message.text.lower() == 'знаменск':
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECKzhgdFcIvMtk8nBuzmw62EPkMdcDfgAC3AoAAv-ooEtnzxrHLeH5MB4E')
		#bot.send_photo(message.chat.id, open('znamensk.jpg', 'rb'))

#Функции
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global tolang;
    global talangq;
    global mylang;
    global talang;
    if call.data == 'ru':
        mylang = 'ru'
        talang = 'Русский🇷🇺'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'ru1':
        tolang = 'ru'
        talangq = 'Русский🇷🇺'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'en':
        mylang = 'en'
        talang = 'Английский🇬🇧'  
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'en1':
        tolang = 'en'
        talangq = 'Английский🇬🇧'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'kk':
        mylang = 'kk'
        talang = 'Казахский🇰🇿'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'kk1':
        tolang = 'kk'
        talangq = 'Казахский🇰🇿'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'ar':
        mylang = 'ar'
        talang = 'Арабский🇦🇪'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'ar1':
        tolang = 'ar'
        talangq = 'Арабский🇦🇪'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'ja':
        mylang = 'ja'
        talang = 'Японский🇯🇵'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'ja1':
        tolang = 'ja'
        talangq = 'Японский🇯🇵'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'zh_cn':
        mylang = 'zh_cn'
        talang = 'Китайский🇨🇳(упрощённый)'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'zh_cn1':
        tolang = 'zh_cn'
        talangq = 'Китайский🇨🇳(упрощённый)'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'de':
        mylang = 'de'
        talang = 'Германский🇩🇪'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'de1':
        tolang = 'de'
        talangq = 'Германский🇩🇪'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'pl':
        mylang = 'pl'
        talang = ' Польский🇵🇱'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'pl1':
        tolang = 'pl'
        talangq = 'Польский🇵🇱'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'uk':
        mylang = 'uk'
        talang = 'Украинский🇺🇦'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'uk1':
        tolang = 'uk'
        talangq = 'Украинский🇺🇦'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'fa':
        mylang = 'fa'
        talang = 'Персидский🇮🇷'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'fa1':
        tolang = 'fa'
        talangq = 'Персидский🇮🇷'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    elif call.data == 'ky':
        mylang = 'ky'
        talang = 'Кыргызский🇰🇬'
        bot.answer_callback_query(call.id,f'Язык ввода установлен: {talang}')
    elif call.data == 'ky1':
        tolang = 'ky'
        talangq = 'Кыргызский🇰🇬'
        bot.answer_callback_query(call.id,f'Язык вывода установлен: {talangq}')
    return mylang
    return tolang
    return talang
    return talangq
     
def get_inf(message):
		try:
			if message.text == '🏠Меню':
				bot.send_message(message.chat.id,'Вы вернулись в меню.', reply_markup = rabom_keyboard.menu_keyboard())
			elif message.text not in filter_inf and message.text != '🏠Меню':
				inf = message.text;
				bot.send_message(message.chat.id,'Ищу информацию🔃')
				bot.send_message(message.chat.id,wikipedia.summary(inf))
				bot.register_next_step_handler(message, get_inf);
			elif message.text in filter_inf:
				bot.send_message(message.chat.id,'Я символы не принимаю ಠ_ಠ')
				bot.register_next_step_handler(message, get_inf)
		except:
			bot.send_message(message.chat.id,'Информация не найдена ಠ_ಠ')
			bot.register_next_step_handler(message, get_inf)

def get_url(message):
		try:
			url = message.text;
			bot.send_message(message.chat.id,'Сокращаю ссылку🔃')
			bot.send_message(message.chat.id,s.tinyurl.short(url))
		except:
			bot.send_message(message.chat.id,'Я не могу сократить данную ссылку ಠ_ಠ')

def get_text(message):
	try:
		if message.text == '🏠Меню':
			bot.send_message(message.chat.id,'Вы вернулись в меню.', reply_markup = rabom_keyboard.menu_keyboard())
		elif message.text == '◀️Назад':
			bot.send_message(message.chat.id,'Вы вернулись в меню.', reply_markup = rabom_keyboard.translate_keyboard())
		elif message.text != '🏠Меню':
			result_rus = translator.translate(message.text, src=str(mylang), dest=str(tolang))
			bot.send_message(message.chat.id,result_rus.text)
			bot.register_next_step_handler(message, get_text);
	except:
		bot.send_message(message.chat.id,'Я не могу перевести этот текст!\nЛибо вы не выбрали язык ಠ_ಠ!')
	
def get_town(message):
	try:
		town = message.text
		observation = mgr.weather_at_place(town)
		w = observation.weather
		weather = w.detailed_status
		temp = w.temperature('celsius').get('temp')
		wind_speed = w.wind().get('speed')
		bot.send_message(message.chat.id,f'🏙Город: {town}\n🌦Погода: {weather}\n🌡Температура: {temp}°C\n💨Скорость ветра: {wind_speed} м/с')
	except:
		bot.send_message(message.chat.id,'Я не могу найти этот город на карте ._.')

def get_max_random(message):
	global mr;
	try:
		if int(message.text) < 100000:
			mr = int(message.text)
			bot.send_message(message.chat.id,'Принял!')
			return mr
		else:
			bot.send_message(message.chat.id,'Я до стольки считать не умею! ಠ_ಠ')
	except:
		bot.send_message(message.chat.id,'Я не знаю такой цифры ಠ_ಠ')
		
def get_code(message):
	try:
		code =''.join([chr(int(s, 2)) for s in message.text.split()])
		bot.send_message(message.chat.id, code)
	except:
		bot.send_message(message.chat.id,'Что-то не так')

def get_code_text(message):
	try:
		code_text = ' '.join(format(ord(x), 'b') for x in message.text)
		bot.send_message(message.chat.id, code_text)
	except:
		bot.send_message(message.chat.id,'Что-то не так')

def get_send(message):
	try:
		message_to_admin = str(message.text)
		user_id = str(message.chat.id)
		name = str(message.from_user.first_name)
		username = str(message.from_user.username)
		bot.send_message(message.chat.id,'📨Отправил')
		bot.send_message(admin_id,f'💬Сообщение от:\n💳id: {user_id}\n🚹username: @{username}\nТекст сообщения: {message_to_admin}')
		bot.send_message(moderator_id,f'💬Сообщение от:\n💳id: {user_id}\n🚹username: @{username}\nТекст сообщения: {message_to_admin}')
	except:
		bot.send_message(message.chat.id,'Я не могу такое отправить ಠ_ಠ')



bot.polling(none_stop = True)