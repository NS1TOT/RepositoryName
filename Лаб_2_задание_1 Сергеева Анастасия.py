# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
while money_capital + salary >= spend:
    month += 1
    month_expenses = spend * (1 + increase) ** (month - 1)
    money_capital += salary - month_expenses
print("Количество месяцев, которое можно протянуть без долгов:", month-1)
