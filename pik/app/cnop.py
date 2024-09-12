from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


start_button = [
    [KeyboardButton(text="Geeks"), KeyboardButton(text="Направление")]
]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку')


geeks_inline = [
    [InlineKeyboardButton(text='GeeksPro', url='https://geeks.kg/geeks-pro'), 
     InlineKeyboardButton(text='Основной сайт Geeks', url='https://geeks.kg/allcourses'), 
     InlineKeyboardButton(text='Geeks Studio', url='https://geeks.kg/advantages')]
]
geeks_keyboard = InlineKeyboardMarkup(inline_keyboard=geeks_inline)


direction_inline = [
    [InlineKeyboardButton(text="Backend", callback_data='back'), 
    InlineKeyboardButton(text="Frontend", callback_data='front'), 
    InlineKeyboardButton(text='Android', callback_data='Android'), 
    InlineKeyboardButton(text="UX/UI", callback_data='UX/UI')]
]
direction_keyboard = InlineKeyboardMarkup(inline_keyboard=direction_inline)


front_inline = [
    [InlineKeyboardButton(text="HTML", url="https://developer.mozilla.org/en-US/docs/Web/HTML")],
    [InlineKeyboardButton(text="CSS", url="https://developer.mozilla.org/en-US/docs/Web/CSS")],
    [InlineKeyboardButton(text="JS", url="https://developer.mozilla.org/en-US/docs/Web/JavaScript")]
]
front_keyboard = InlineKeyboardMarkup(inline_keyboard=front_inline)


back_inline = [
    [InlineKeyboardButton(text='Python', url='https://docs.python.org/3/tutorial/index.html'), 
    InlineKeyboardButton(text='Aiogram', url='https://docs.aiogram.dev/en/latest/'),
    InlineKeyboardButton(text='Django', url='https://docs.djangoproject.com/en/5.1/')]
]
back_keyboard = InlineKeyboardMarkup(inline_keyboard=back_inline)


android_inline = [
    [InlineKeyboardButton(text="Java and Kotlin", url='https://docs.oracle.com/en/java/'), 
    InlineKeyboardButton(text='Android Studio', url='https://developer.android.com/studio/intro?hl=ru'),
    InlineKeyboardButton(text='Jetpack', url='https://developer.android.com/jetpack?hl=ru')]
]
android_keyboard = InlineKeyboardMarkup(inline_keyboard=android_inline)


dizi_inline = [
    [InlineKeyboardButton(text='Figma', url='https://www.reg.ru/blog/zhutkie-sajty-kotorye-vyzovut-u-vas-murashki/'), 
    InlineKeyboardButton(text='Sketch', url='https://www.reg.ru/blog/zhutkie-sajty-kotorye-vyzovut-u-vas-murashki/'), 
    InlineKeyboardButton(text='Framer', url='https://www.reg.ru/blog/zhutkie-sajty-kotorye-vyzovut-u-vas-murashki/')]
]
dizi_keyboard = InlineKeyboardMarkup(inline_keyboard=dizi_inline)
