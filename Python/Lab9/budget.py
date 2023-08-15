class Budget:
    def __init__(self,balance):
       self.balance = balance

    def deposit(self,deposit):
        self.depositvar = deposit
        self.balance= self.balance+self.depositvar
        return self.balance

    def withdraw(self,withdraw):
        self.withdrawvar = withdraw
        self.balance = self.balance - self.withdrawvar
        return self.balance

    def transfer(self,payment,payee):
        payee.deposit(payment)
        self.withdraw(payment)
        return self.balance



clothing = Budget(54)
deposit_money_clothing = clothing.deposit(20)
withdraw_money_clothing = clothing.withdraw(5)

entertainment = Budget(75)
the_transfer = entertainment.transfer(10,clothing)
print(entertainment.balance,clothing.balance)


        


