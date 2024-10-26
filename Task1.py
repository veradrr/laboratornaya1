money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
budget = salary+money_capital
budget1= budget - spend #после первого месяца
month = 1
count = 0
while budget1 > 0:
    for i in range(month):
        spend = spend*(increase+1)
        budget1 = budget1 - (spend - salary)
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
