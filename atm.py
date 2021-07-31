class ATM(object):
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
    
    def widthdrawMoney(self):
        print("Money Widthdrawed")
    
    def depositMoney(self):
        print("Money Deposited")

atm = ATM(123456789,0000)
atm.widthdrawMoney()
atm.depositMoney()
