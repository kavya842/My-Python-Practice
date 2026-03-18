"""Object Method :- Object method is a method that works on instance variables 
                    and is used to access or modify the data of a particular object."""
class aadhar:
      state="Andhra Pradesh"
      district="prakasam"
      mandal="Zarugumalli"
      pincode=523271
      def __init__(self,name,fathername,dob,houseno,):
            self.name=name
            self.fathername=fathername
            self.dob=dob
            self.houseno=houseno
      def disp(self):
        print(self.name,self.fathername,self.dob,self.houseno)
people1=aadhar("kavya","ravi","21-09-21",87)
people2=aadhar("mani","ravi","21-09-12",98)
people1.disp()
people2.disp()
print(vars(people1))
print(vars(people2))
            