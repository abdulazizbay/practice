print("=== Encapsulation ===")

# Python : public, __private, _protected


class Account():
    # state
    description = "this class makes bank accaounts"
    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount
    # method

    def get_balance(self):
        print(f"owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def widthdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner


my_account = Account("Shown", 1000)
my_account.get_balance()

print("=======")
my_account.deposit(3500)
my_account.widthdraw(400)
my_account.get_balance()

print("------")
try:
    result = my_account.__amount
    print(result)
except Exception as err:
    print("no target state found:", err)

account_owner = my_account.holder
print("account owner:", account_owner)
