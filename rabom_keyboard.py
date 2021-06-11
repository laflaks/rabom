from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def menu_keyboard():
	menu_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	button1 = types.KeyboardButton('👤Профиль')
	button2 = types.KeyboardButton('🎲Random number')
	button3 = types.KeyboardButton('🔎Найти информацию')
	button4 = types.KeyboardButton('🔗Сократить ссылку')
	button5 = types.KeyboardButton('📜Перевод')
	button_settings = types.KeyboardButton('⚙Настройки')
	button_weather = types.KeyboardButton('⛅Погода')
	button_rating = types.KeyboardButton('📟Перевод двоичного кода')
	menu_keyboard.add(button1, button2, button3, button4, button5,button_weather,button_rating, button_settings)
	return menu_keyboard

def settings_keyboard():
	settings_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	button1 = types.KeyboardButton('🏠Меню')
	button2 = types.KeyboardButton('🔔Сообщение для администрации')
	settings_keyboard.add(button2, button1)
	return settings_keyboard

def log_keyboard():
	log_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	button1 = types.KeyboardButton('Включён log_mod!')
	log_keyboard.add(button1)
	return log_keyboard

def demenu_keyboard():
	demenu_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	button1 = types.KeyboardButton('🏠Меню')
	back_button = types.KeyboardButton('◀️Назад')
	demenu_keyboard.add(back_button,button1)
	return demenu_keyboard

def demenu_v2_keyboard():
	demenu_v2_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	button1 = types.KeyboardButton('🏠Меню')
	demenu_v2_keyboard.add(button1)
	return demenu_v2_keyboard

def translate_keyboard():
	translate_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	lang_button = types.KeyboardButton('🔤Языки перевода')
	translate_button = types.KeyboardButton('➡️Перевести')
	menu_button = types.KeyboardButton('🏠Меню')
	translate_keyboard.add(lang_button, translate_button, menu_button)
	return translate_keyboard

def my_lang_keyboard():
    my_lang_keyboard = InlineKeyboardMarkup()
    my_lang_keyboard.row_width = 2
    my_lang_keyboard.add(InlineKeyboardButton('Русский🇷🇺', callback_data ='ru'),InlineKeyboardButton('Русский🇷🇺', callback_data ='ru1'),InlineKeyboardButton('Казахский🇰🇿', callback_data ='kk'),InlineKeyboardButton('Казахский🇰🇿', callback_data ='kk1'),InlineKeyboardButton('Арабский🇦🇪', callback_data ='ar'),InlineKeyboardButton('Арабский🇦🇪', callback_data ='ar1'),InlineKeyboardButton('Японский🇯🇵', callback_data ='ja'),InlineKeyboardButton('Японский🇯🇵', callback_data ='ja1'),InlineKeyboardButton('Английский🇬🇧', callback_data ='en'),InlineKeyboardButton('Английский🇬🇧', callback_data ='en1'),InlineKeyboardButton('Китайский🇨🇳', callback_data ='zh_cn'),InlineKeyboardButton('Китайский🇨🇳', callback_data ='zh_cn1'),InlineKeyboardButton('Германский🇩🇪', callback_data ='de'),InlineKeyboardButton('Германский🇩🇪', callback_data ='de1'),InlineKeyboardButton('Польский🇵🇱', callback_data ='pl'),InlineKeyboardButton('Польский🇵🇱', callback_data ='pl1'),InlineKeyboardButton('Украинский🇺🇦', callback_data ='uk'),InlineKeyboardButton('Украинский🇺🇦', callback_data ='uk1'),InlineKeyboardButton('Персидский🇮🇷', callback_data ='fa'),InlineKeyboardButton('Персидский🇮🇷', callback_data ='fa1'),InlineKeyboardButton('Кыргызский🇰🇬', callback_data ='ky'),
InlineKeyboardButton('Кыргызский🇰🇬', callback_data ='ky1'))
    return my_lang_keyboard
    
'''def step2(call):
    menu2 = telebot.types.InlineKeyboardMarkup()
    menu2.add(telebot.types.InlineKeyboardButton(text = 'Третья кнопка', callback_data ='third'))
    menu2.add(telebot.types.InlineKeyboardButton(text = 'Четвертая кнопка', callback_data ='fourth'))'''