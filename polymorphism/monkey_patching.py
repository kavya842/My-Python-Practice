"""Mpnkey Patching:--Monkey patching is used to dynamically modify or extend the behaviour of 
                     classes or modules at runtime without changing their original source code."""

# Monkey Patching
#  Runtime lo class / module behaviour ni change cheyyadam
#  Feature add / bug fix / customization kosam

#  class Whatsapp:
#     def send(self):
#         print('sending text')
# def sending_new(self):
#     print('Hie kavya')
# Whatsapp.send=sending_new
# obj=Whatsapp()
# obj.send()

# class college:
    # def students(self):
        # print("Students are participating in culturals")
# def students_IT(self):
    # print(" IT students are participating in WEB WIZARDS")
# college.students=students_IT   // monkey patching
# obj1=college()
# obj1.students()

class Payment:
    def pay(self):
        print("Real payment")
def new_pay(self):
    print("Payment with discount")
Payment.pay = new_pay   # monkey patching
obj = Payment()
obj.pay()

# Monkey Patching
#  Runtime lo class / module behaviour ni change cheyyadam
#  Feature add / bug fix / customization kosam

"""  Mocking :-Mocking is a testing technique where real objects or services
               are replaced with fake implementations to simulate behaviour during testing."""
# If real system class based ga unte
# appudu mocking class level lo chestham.
# class EmailService:
#     def send(self):
#         print("Real email sending")
# def mock_send(self):
#     print("Fake email sending")
# EmailService.send = mock_send   # mocking class method
# obj = EmailService()
# obj.send()


class Payment:
    def pay(self):
        print("Money deducted")
def fake_pay(self):
    print("Fake payment success")
Payment.pay = fake_pay   # mocking in testing
obj = Payment()
obj.pay()