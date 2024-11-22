salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_needed = 0
current_spend = spend
for i in range(months):
    needed = max(0, current_spend - salary)
    total_needed += needed
    current_spend *= (1 + increase)

capital = int(total_needed)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", capital)
