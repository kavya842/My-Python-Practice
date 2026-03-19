class Bank:
    bname="union"
    bloc="kamepalli"
    def __init__(self,name,fathername,age,address,phno):
        self.name=name
        self.fathername=fathername
        self.age=age
        self.address=address
        self.phno=phno
    def disp(self):
        print(self.name,self.fathername,self.age,self.address,self.phno)
class Update_bank(Bank):
    def __init__(self,name,fathername,age,address,phno,aadharno,panno):
        super(). __init__(name,fathername,age,address,phno)
        self.aadharno=aadharno
        self.panno=panno
    def display(self):
        super().disp()
        print(self.aadharno,self.panno)
cus1=Update_bank("kavya","ravikumar",21,"kamepalli","8919951981",969272966108,"UPINE23415")
cus1.display()