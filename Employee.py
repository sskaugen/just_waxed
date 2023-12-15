class Employee:
    def __init__(self, name, hourly_rate,commison):
        self.__name = name
        self.__hourly_rate = hourly_rate
        self.__commison = commison

    def get_hourly_rate(self):
        print("Current Hourly rate: " + str(self.__hourly_rate))
        
        
        
emp_1 = Employee("Sean", 16, .5)

emp_1.get_hourly_rate()