from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo


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
reffs_programm_btn = InlineKeyboardButton(
    text="🤝 Реферальная программа",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/"),
)
autho_publish_btn = InlineKeyboardButton(
    text="🚀✉️ Автматическая публикация ответов",
    web_app=WebAppInfo(url="https://volodia.pavloff201343.fvds.ru/#/account/"),
)
# start_bot_btn = InlineKeyboardButton(
#     text="▶️Начать пользоваться ботом", callback_data="bot_start"
# )
# send_time_btn = InlineKeyboardButton(
#     text="🕔Настроить время отправки уведомлений", callback_data="set_push_time"
# )
# signature_answer_btn = InlineKeyboardButton(
#     text="🖋Подпись к ответу", callback_data="add_signature"
# )
get_balance_btn = InlineKeyboardButton(text="callback_data", callback_data="balance")

top_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            user_office_btn,
            feedback_btn,
            reffs_programm_btn,
            autho_publish_btn,
            get_balance_btn,
            include_wd_btn,
        ]
    ]
)


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


hundred_btn = InlineKeyboardButton(text="100", callback_data="pay_100")
five_hundres_btn = InlineKeyboardButton(text="500", callback_data="pay_500")
thousand_btn = InlineKeyboardButton(text="1000", callback_data="pay_1000")
two_thousand_btn = InlineKeyboardButton(text="2000", callback_data="pay_2000")
ten_thousand_btn = InlineKeyboardButton(text="10000", callback_data="pay_10000")

tariffs_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            hundred_btn,
            five_hundres_btn,
            thousand_btn,
            two_thousand_btn,
            ten_thousand_btn,
            # start_bot_btn,
        ]
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
