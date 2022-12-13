import statistics

numbers = [19,63,51,7,99,11,23,15,17,8]

# Standard numeric functions
print(min(numbers)) # Minimum number in the array
print(max(numbers))

print(statistics.mean(numbers))
print(statistics.median(numbers))

print(round(5.571894)) # Round closest to int
print(round(5.671,1))  # Rounds to decimal point

print(abs(-560)) # Gives us absolute value (no negatives)

# String functions
str = "hello"
upr_str = "HELLO"

print(str.upper()) 
print(upr_str.lower())
print(upr_str.title()) # First char is Upper, all others are lower
print(str.replace('o', 'e')) # Replace all instances of 'o' with 'e'
print(len (str))

# Split Function
cities = "london,birmingham,leeds,manchester,bristol"
cityList = cities.split(',')
print(cityList[2])

# String formatting
drink = "Mocha"
size = "Large"
extras = "Whipped Cream"
order = f"{drink} ordered at size {size}, with {extras} added"
print(order)
order_format = "{} ordered at size {}, with {} added".format(drink, size, extras)
print(order_format)