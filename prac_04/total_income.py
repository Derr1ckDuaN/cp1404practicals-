def main():
    """display income for given number of months"""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)

def print_income_report(incomes):
    """print income report """
    total = 0
    print("Income Report")

    index = 0
    for income in incomes:
        total+= income
        print(f"Month {index + 1:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
        index += 1

main()