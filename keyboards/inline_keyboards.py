from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from datetime import timezone, timedelta, datetime, time


include_wd_btn = InlineKeyboardButton(
    text="🟣 Подключить Wildberries",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/account/"),
)

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            include_wd_btn,
        ]
    ]
)


main_menu_btn = InlineKeyboardButton(text="ℹ️ Главное меню", callback_data="main_menu")

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            main_menu_btn,
        ]
    ]
)


user_office_btn = InlineKeyboardButton(
    text="⚙️ Личный кабинет", callback_data="user_office"
)
feedback_btn = InlineKeyboardButton(
    text="🗒 Отзывы",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/feedbacks/"),
)
refs_programm_btn = InlineKeyboardButton(
    text="🤝 Реферальная программа",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/"),
)
autho_publish_btn = InlineKeyboardButton(
    text="🚀✉️ Автоматическая публикация ответов",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/account/"),
)
get_balance_btn = InlineKeyboardButton(text="💰 Баланс", callback_data="balance")

top_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [user_office_btn],
        [feedback_btn],
        [refs_programm_btn],
        [autho_publish_btn],
        [get_balance_btn],
        [include_wd_btn],
    ]
)

my_office_btn = InlineKeyboardButton(
    text="🏢 Мои кабинеты",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/account/"),
)
set_times_send_btn = InlineKeyboardButton(
    text="🕦 Настроить время отправки  уведомлений", callback_data="set_times_send"
)
feedback_signature_add_btn = InlineKeyboardButton(
    text="🖋 Подпись к ответу",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/account/"),
)

user_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [my_office_btn],
        [set_times_send_btn],
        [feedback_signature_add_btn],
        [get_balance_btn],
        [main_menu_btn],
    ]
)


time_day_night_btn = InlineKeyboardButton(
    text="Круглосуточно", callback_data="time_day_hight"
)
time_day_slice_min_btn = InlineKeyboardButton(
    text="День 9-18", callback_data="time_day_slice_min"
)
time_day_slice_max_btn = InlineKeyboardButton(
    text="День 9-21", callback_data="time_day_slice_max"
)
time_mytime_btn = InlineKeyboardButton(
    text="Ввести самостоятельно", callback_data="time_self"
)
back_to_user_menu_btn = InlineKeyboardButton(
    text="◀️ Назад", callback_data="back_to_user_menu"
)

time_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [time_day_night_btn],
        [time_day_slice_min_btn],
        [time_day_slice_max_btn],
        [time_mytime_btn],
        [back_to_user_menu_btn, main_menu_btn],
    ]
)


tz_dict = {
    "Калининград (UTC+2)": "utc 2",
    "Москва (UTC+3)": "utc 3",
    "Самара (UTC+4)": "utc 4",
    "Екатеринбург и Актау (UTC+5)": "utc 5",
    "Омск и Нур-Султан (Астана) (UTC+6)": "utc 6",
    "Красноярск (UTC+7)": "utc 7",
    "Иркутск (UTC+8)": "utc 8",
    "Якутск (UTC+9)": "utc 9",
    "Владивосток (UTC+10)": "utc 10",
    "Магадан (UTC+11)": "utc 11",
    "Сахалин и Камчатка (UTC+12)": "utc 12",
}


# add field utc in database
async def create_tz_menu(tz: int) -> InlineKeyboardBuilder:
    # bootom 4 stroke for check time
    # offset = timedelta(hours=tz)
    # current_tz = timezone(offset)
    # dt_now = datetime.now(tz=current_tz)
    # offset_time = dt_now.replace()
    kb_builder = InlineKeyboardBuilder()
    for key, val in tz_dict.items():
        if int(val.split(" ")[-1]) == tz:
            kb_builder.row(InlineKeyboardButton(text=f"✅ {key}", callback_data=val))
            continue
        kb_builder.row(InlineKeyboardButton(text=key, callback_data=val))
    return kb_builder


back_to_user_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[[back_to_user_menu_btn, main_menu_btn]]
)


update_balance_btn = InlineKeyboardButton(
    text="💰 Пополнить баланс", callback_data="update_balance"
)

update_balance_kb = InlineKeyboardMarkup(inline_keyboard=[[update_balance_btn]])


tariffs_btn = InlineKeyboardButton(text="📊Тарифы", callback_data="tariffs")
add_token_btn = InlineKeyboardButton(
    text="📝Добавить Wildberries токен", callback_data="add_token"
)
get_feedbacks_btn = InlineKeyboardButton(
    text="🗣Получить отзывы", callback_data="get_feedbacks"
)

start_menu = InlineKeyboardMarkup(
    inline_keyboard=[[tariffs_btn, add_token_btn, get_feedbacks_btn, main_menu_btn]]
)


hundred_btn = InlineKeyboardButton(
    text="392₽ за 100 ответов (скидка 20%)", callback_data="pay 100"
)
five_hundres_btn = InlineKeyboardButton(
    text="1 592₽ за 500 ответов (скидка 20%)", callback_data="pay 500"
)
thousand_btn = InlineKeyboardButton(
    text="2 872₽ за 1 000 ответов (скидка 20%)", callback_data="pay 1000"
)
two_thousand_btn = InlineKeyboardButton(
    text="5 592₽ за 2 000 ответов (скидка 20%)", callback_data="pay 2000"
)
ten_thousand_btn = InlineKeyboardButton(
    text="23 992₽ за 10 000 ответов (скидка 20%)", callback_data="pay 10000"
)

tariffs_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [hundred_btn],
        [five_hundres_btn],
        [thousand_btn],
        [two_thousand_btn],
        [ten_thousand_btn],
    ]
)

publish_btn = InlineKeyboardButton(text="📤Опубликовать", callback_data="publish")
edit_btn = InlineKeyboardButton(text="📝Редактировать", callback_data="edit")
regenerate_btn = InlineKeyboardButton(
    text="🔁Сгенерировать новый ответ", callback_data="regenerate"
)
not_answer_btn = InlineKeyboardButton(
    text="⛔️Не отвечать на отзыв", callback_data="not_answer"
)

feedback_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [publish_btn, edit_btn],
        [regenerate_btn, not_answer_btn],
        [main_menu_btn],
    ]
)
