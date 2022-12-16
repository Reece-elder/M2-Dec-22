# Will contain our Class that will be used to create / instantiate objects

# class is a template that contains functionality to create objects
# After class we specify the name of the class we are creating
class cake: # Class is essentially a function which returns objects
    flavour = "vanilla"
    tiers = 2
    toppings = ["cream", "strawberries"]
    gluten_free = True

    # The function in the class must take in a param called 'self'
    def eatCake(self):
        return "Cake is delicious!"

print(cake.flavour) # Accessing the class cake, not best practice to do 
vic_sponge = cake()
print(vic_sponge.toppings)
print(vic_sponge.eatCake())

# Exercise - Create a class with 4 pre set attributes and one function that just returns a string 
# for any animal you want, create 2 objects of this animal and print their attributes 

