def dayRate(hr_rate):
    return round(8 * hr_rate)

def monthRate(hr_rate, discount):
    return round(hr_rate * 8 * 22 * (1 - discount))

def daysInBudget(budget, hr_rate, discount):
    res = budget / (8 * hr_rate * (1 - discount))
    return round(res)

print("Day Rate: ", dayRate(89))
print("Month Rate: ", monthRate(89, 0.42))
print("Day In Budget: ", daysInBudget(20000, 89, 0.2002))