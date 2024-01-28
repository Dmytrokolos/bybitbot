import bybit
import os

# Налаштування
API_KEY = "xhRRJjEBe17BRHB2fT"
SECRET_KEY = "St9F4Y9dedm2HuCqFJuuxEBXrPp9cb57CKBB..."

# Функції
def register():
    # Запитуємо у користувача UID
    uid = input("Введіть UID биржі: ")

    # Реєструємося на біржі
    bybit.set_credentials(API_KEY, SECRET_KEY, uid)

def select_pair():
    # Отримуємо список торгових пар
    pairs = bybit.get_spot_pairs()

    # Виводимо список торгових пар
    for pair in pairs:
        print(pair)

    # Запитуємо у користувача пару
    pair = input("Виберіть торгову пару: ")

    return pair

def set_limits():
    # Запитуємо у користувача ліміт-ціну купівлі
    buy_limit = float(input("Введіть ліміт-ціну купівлі: "))

    # Запитуємо у користувача ліміт-ціну продажу
    sell_limit = float(input("Введіть ліміт-ціну продажу: "))

    return buy_limit, sell_limit

def start_trading():
    # Запускаємо автоматичну торгівлю
    bybit.start_spot_grid_trading(buy_limit, sell_limit)

def check_balance():
    # Отримуємо баланс
    balance = bybit.get_spot_balance()

    # Виводимо баланс
    print("Баланс:", balance)

def stop_trading():
    # Зупиняємо автоматичну торгівлю
    bybit.stop_spot_grid_trading()

# Інтерфейс
print("Бот ByBit")
print("Команди:")
print("1 - Реєстрація")
print("2 - Вибір торгової пари")
print("3 - Встановлення лімітів")
print("4 - Початок автоматичної торгівлі")
print("5 - Перевірка балансу")
print("Ctrl+Z - Зупинка бота")

# Цикл обробки команд
while True:
    # Отримуємо команду від користувача
    command = input("Введіть команду: ")

    # Обробляємо команду
    if command == "1":
        register()
    elif command == "2":
        pair = select_pair()
    elif command == "3":
        buy_limit, sell_limit = set_limits()
    elif command == "4":
        start_trading(buy_limit, sell_limit)
    elif command == "5":
        check_balance()
    elif command == "Ctrl+Z":
        stop_trading()
    else:
        print("Невідома команда")
