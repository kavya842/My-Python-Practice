from abc import ABC, abstractmethod
class  Atm(ABC):
    @abstractmethod
    def withdraw():
        pass
    @abstractmethod
    def ch_bal():
        pass
class in_atm(Atm):
    def __init__(self,name,bal):
        self.name=name
        self.bal=bal
    def ch_bal(self):
        print('your acc balance is:',self.bal)
    def withdraw(self,amt):
        if self.bal>=amt:
            self.bal-=amt
            print(f'{amt} has been debited from your bank account')
        else:
            print('insufficient balance')
c1=in_atm('kavya',20000)
c1.ch_bal()
c1.withdraw(5000)
c1.ch_bal()
c1.withdraw(2000000)
c1.ch_bal()