salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total = 0
new_months = 0
for i in range(months):
    total = total - salary + spend
    spend = spend * (1 + increase)
    new_months = new_months + 1
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total, 2))
