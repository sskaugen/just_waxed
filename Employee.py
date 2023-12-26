from datetime import datetime
import math
#I would like every employee to have thier own instance of math maybe?
#This is the Employee class which houses all the information about the employess
class Employee:
    def __init__(self, name, hourly_rate,commission,start_date,birth_date):
        self.__name = name
        self.__hourly_rate = hourly_rate
        self.__commission = commission
        self.__start_date = datetime.strptime(start_date, '%B %d %Y')
        self.__birth_date = datetime.strptime(birth_date, '%B %d %Y')
        

    #Getters for Private Variables
    def get_hourly_rate(self):
        print("Current Hourly rate: " + str(self.__hourly_rate))
        return(self.__hourly_rate)
    def get_name(self):
        print("Employee Name is: " + str(self.__name))
        return(self.__name)
    def get_commission(self):
        print("Current Commision Rate is: " + str(self.__commission))
        return(self.__commission)
        
    def get_start_date(self):
        print("Current Start Date is Rate is: " + str(self.__start_date))
        return(self.__start_date)
    def get_birth_date(self):
        print("Current Birth Date is: " + str(self.__birth_date))
        return(self.__birth_date)
    
    #setters for Private Variables
    def set_hourly_rate(self,new_hourly_rate):
        self.__hourly_rate = new_hourly_rate
        print("New Hourly rate is: " + str(self.__hourly_rate))
    
    def set_name(self, new_name):
        self.__name = new_name
        print("Updated Employee Name is: " + str(self.__name))
    
    def set_commission(self,new_commission):
        self.__commission = new_commission
        print("New Commision Rate is: " + str(self.__commission))
        
    def set_start_date(self,new_start_date):
        self.__start_date = datetime.strptime(new_start_date, '%B %d %Y')
        print("New start date is: " + str(self.__start_date))
    
    def set_birth_date(self,new_birthdate):
        self.__birth_date = datetime.strptime(new_birthdate, '%B %d %Y')
        print("New birth date is: " + str(self.__birth_date))
    
    def total_time_with_company(self):
        current_time = datetime.now()
        time_with_company = current_time - self.__start_date
        
        time_with_company_years = math.floor(time_with_company.days / 365)
        remaining_days = time_with_company.days % 365

        print("Current time with the Company is: {} Years and {} Days".format(time_with_company_years, remaining_days))