import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import KBinsDiscretizer, LabelEncoder

# Імпортування даних
url = 'https://raw.githubusercontent.com/susanli2016/Machine-Learning-with-Python/master/data/renfe_small.csv'
data = pd.read_csv(url)

# Перегляд даних
print(data.head())

# Перегляд назв колонок
print(data.columns)

# Видалення рядків з пропущеними значеннями в цільовій змінній
data = data.dropna(subset=['price'])

# Підготовка даних для навчання моделі
X = data.drop('price', axis=1)  # Вхідні характеристики
y = data['price']               # Цільова змінна

# Перетворення цільової змінної на категоріальну
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
y_binned = discretizer.fit_transform(y.values.reshape(-1, 1)).astype(int).ravel()

# Перетворення деяких категоріальних змінних з багатьма унікальними значеннями на числові
le = LabelEncoder()
X['origin'] = le.fit_transform(X['origin'])
X['destination'] = le.fit_transform(X['destination'])
X['train_type'] = le.fit_transform(X['train_type'])
X['train_class'] = le.fit_transform(X['train_class'])
X['fare'] = le.fit_transform(X['fare'])

# Видалення колонок, які не мають значного впливу або важко інтерпретуються
X = X.drop(['insert_date', 'start_date', 'end_date'], axis=1)

# Заповнення пропущених значень у вхідних характеристиках (якщо такі є)
X = X.fillna(X.mean())

# Розділення даних на навчальні та тестові набори
X_train, X_test, y_train, y_test = train_test_split(X, y_binned, test_size=0.2, random_state=42)

# Створення та навчання моделі
model = GaussianNB()
model.fit(X_train, y_train)

# Передбачення на тестових даних
predictions = model.predict(X_test)

# Оцінка точності моделі
accuracy = accuracy_score(y_test, predictions)
print(f'Точність моделі: {accuracy}')

# Відображення передбачення разом з фактичними значеннями
results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})

# Якщо потрібно відобразити деякі характеристики з тестових даних разом з передбаченням
X_test_display = X_test.copy()
X_test_display['Actual'] = y_test
X_test_display['Predicted'] = predictions

print(results.head())  # Перші кілька рядків результатів
print(X_test_display.head())  # Перші кілька рядків тестових даних з передбаченням
