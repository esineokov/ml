revenue = float(input("Enter revenue: "))
costs = float(input("Enter costs: "))

if revenue > costs:
    print("Congratulations! You have a profit.")
    profit = revenue - costs

    print(f"Profitability: {(profit / revenue):.2f}")
    employees = int(input("Enter the number of employees: "))

    print(f"Profit per person: {(profit/employees):.2f}")
elif costs > revenue:
    print("You worked at a loss.")
else:
    print("You went to zero.")

