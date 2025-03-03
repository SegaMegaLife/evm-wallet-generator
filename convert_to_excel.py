import json
import pandas as pd

# Загружаем кошельки из JSON
def load_wallets(filename="wallets.json"):
    with open(filename, "r") as f:
        return json.load(f)

# Сохраняем в Excel
def save_to_excel(wallets, output_file="wallets.xlsx"):
    df = pd.DataFrame(wallets)  # Создаем DataFrame
    df = df[["mnemonic", "address", "private_key"]]  # Выбираем нужные столбцы
    df.to_excel(output_file, index=False)  # Сохраняем без индексов

    print(f"✅ Данные успешно экспортированы в {output_file}")

# Запускаем конвертацию
wallets = load_wallets()
save_to_excel(wallets)
