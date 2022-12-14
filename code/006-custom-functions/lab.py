import random

def rollDice(num):
    return random.randint(1, num)

print(rollDice(10))

# Function that will take in how many stats I want to generate
# Stat is 4 of our 6 sided dice rolled, remove the lowest
def statRoller(num):
    for i in range(num):
        sub_total = 0
        dice_roll = []
        for x in range(4):
            # rolling a dice and adding the total to my list
            dice_roll.append(rollDice(6))
        print(f"Pre removal: {dice_roll}")
        lowest = min(dice_roll)
        sub_total = sum(dice_roll) - lowest
        print(f"Post removal: {sub_total}")

statRoller(6)

def simpleTax(salary):
    taxableAmount = 0
    
    if salary < 12500:
        taxableAmount = 0
    elif salary < 23000:
        taxableAmount = salary * 0.19
    
    return taxableAmount

def complexTax(salary):
    totalTax = 0
    taxableAmount = 0

    if salary < 12500:
        totalTax = 0

    if salary > 12500:
        taxableAmount = salary - 12500
        totalTax += (taxableAmount * 0.19)

    if salary > 23000:
        taxableAmount = 0
        taxableAmount = salary - 23000
        totalTax += (taxableAmount * 0.41)

    return totalTax

print(complexTax(25000))
