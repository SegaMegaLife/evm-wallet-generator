from eth_account import Account
from mnemonic import Mnemonic
import json
import os

# Включаем поддержку HDWallet-функций
Account.enable_unaudited_hdwallet_features()

# Функция для генерации кошелька
def generate_wallet():
    mnemo = Mnemonic("english")  # Генерируем мнемоническую фразу
    mnemonic_phrase = mnemo.generate(strength=128)  # 12 слов
    acct = Account.from_mnemonic(mnemonic_phrase)  # Создаем кошелек

    wallet_data = {
        "mnemonic": mnemonic_phrase,
        "private_key": acct.key.hex(),
        "address": acct.address
    }

    return wallet_data

# Функция для сохранения данных в файл
def save_wallets(wallets, filename="wallets.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing_wallets = json.load(f)
    else:
        existing_wallets = []

    existing_wallets.extend(wallets)

    with open(filename, "w") as f:
        json.dump(existing_wallets, f, indent=4)

# Запрос количества кошельков у пользователя
try:
    num_wallets = int(input("Введите количество кошельков для генерации: "))
    if num_wallets <= 0:
        raise ValueError("Число должно быть больше 0.")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
    exit(1)

print(f"🔄 Начинаем генерацию {num_wallets} кошельков...")

# Генерация кошельков
wallets = [generate_wallet() for _ in range(num_wallets)]

# Сохранение в файл
save_wallets(wallets)

print(f"✅ Успешно сгенерировано и сохранено {num_wallets} кошельков в wallets.json!")
