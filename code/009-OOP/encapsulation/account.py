class account:

    # Rather than a constructor to declare funds we want 

    # int money = 0
    # string pin = ""

    # add your constructor that uses those variable types
    # because python is dynamically typed its generally better practice to not declare variables

    # _<var name> defines this SHOULD BE PRIVATE 
    _pin = "1234"
    _money = 500
    _password = "password"

    # Getter
    def displayMoney(self, password):
        if password == self._password:
            return self._money
        else:
            return "Invalid password!"

    # Setter
    def withdrawMoney(self, pin, amount):
        if pin == self._pin:
            self._money -= amount
            return self._money
        else:
            return "Invalid Pin!"


demoAccount = account()
print(demoAccount._money) # Nothing in Python stopping us from this..
print(demoAccount.displayMoney("password"))
print(demoAccount.withdrawMoney("1234", 210))