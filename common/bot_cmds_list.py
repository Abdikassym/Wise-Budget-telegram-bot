from aiogram.types import BotCommand

private = [
    BotCommand(command="menu", description="Список всех комманд."),
    BotCommand(command="about", description="Инофрмация о боте."),
    BotCommand(command="payment", description="Способы оплаты."),
    BotCommand(command="shipping", description="Способы доставки."),
    BotCommand(command="magic", description="Magic filter was called.")
]
