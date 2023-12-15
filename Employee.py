#This is the Employee class which houses all the information about the employess
class Employee:
    def __init__(self, name, hourly_rate,commission):
        self.__name = name
        self.__hourly_rate = hourly_rate
        self.__commission = commission

    def get_hourly_rate(self):
        print("Current Hourly rate: " + str(self.__hourly_rate))
    
    def get_name(self):
        print("Employee Name is: " + str(self.__name))
    
    def get_commission(self):
        print("Current Commision Rate is: " + str(self.__commission))
        
    def set_hourly_rate(self,new_hourly_rate):
        self.__hourly_rate = new_hourly_rate
        print("New Hourly rate is: " + str(self.__hourly_rate))
    
    def set_name(self, new_name):
        self.__name = new_name
        print("Updated Employee Name is: " + str(self.__name))
    
    def set_commission(self,new_commission):
        self.__commission = new_commission
        print("New Commision Rate is: " + str(self.__commission))
    
        
        
        
emp_1 = Employee("Sean Skaugen", 16, .5)

emp_1.get_hourly_rate()
emp_1.get_name()
emp_1.get_commission()
print("----------------------------------------------")
print()

emp_1.set_hourly_rate(20)
emp_1.set_name("Sean James")
emp_1.set_commission(.75)