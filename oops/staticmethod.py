"""Static method:- Static method is a method that does not depend on instance variables or class variables 
                   and is used to perform general utility tasks related to the class.
                   i) It uses @staticmethod decorator 
                   ii) It does not take self or cls parameter """
class College:
    collegename = "MIC College of Technology"
    collegecode ="MICT"
    @staticmethod
    def welcome_msg():
        print("Welcome to College Portal")
    @staticmethod
    def msg():
        print("Admissions are open")
    @staticmethod
    def modify():
        College.collegename="DVR&Dr.HS MIC COLLEGE OF TECHNOLOGY"
College.welcome_msg()
College.msg()
College.modify()
print(College.collegename)