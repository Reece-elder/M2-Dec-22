from bird import bird

class parrot(bird):

    def __init__(self, feathers, wingspan, knownWords):
        super().__init__(feathers, wingspan)
        self.knownWords = knownWords

    def talk(self):
        for word in self.knownWords:
            print(word)
        return True

    # Overriding and replacing the parent function eat()
    def eat(self):
        return "Cracker pls"

polly = parrot("red and green", 14, ["Hello", "World", "all"]) 
polly.talk()
print(polly.eat())