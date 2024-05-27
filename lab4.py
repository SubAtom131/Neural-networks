import pandas as pd

# Припустимо, що у нас є DataFrame з назвою df, який містить наші погодні дані
# df = pd.read_csv('your_data.csv') # Замініть 'your_data.csv' на шлях до вашого файлу з даними

# Визначаємо ймовірності для кожного атрибуту
# Ці значення мають бути заздалегідь визначені або обчислені з вашого набору даних
probabilities = {
    'overcast': {'high': {'weak': 0.7}, 'strong': 0.3},
    'sunny': {'high': {'weak': 0.6}, 'normal': {'strong': 0.4}},
    'rain': {'high': {'strong': 0.5}}
}

# Функція для обчислення ймовірності відбуття матчу
def calculate_probability(outlook, humidity, wind):
    if outlook in probabilities and humidity in probabilities[outlook] and wind in probabilities[outlook][humidity]:
        return probabilities[outlook][humidity][wind]
    else:
        return "Немає даних для обчислення"

# Використовуємо функцію для обчислення ймовірності

probability = calculate_probability('sunny', 'high', 'weak')

print(f"Ймовірність проведення матчу при умовах Outlook = Sunny, Humidity = High, Wind = Weak: {probability}")