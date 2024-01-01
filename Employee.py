from datetime import datetime
from mathmodule import mathlogic
import math
#This is the Employee class which houses all the information about the employess
class Employee:
    def __init__(self,name,hourly_rate,commission_services,commission_products):
        self.__name = self.set_name(name)
        self.__hourly_rate = self.set_hourly_rate(hourly_rate)
        self.__commission_services = self.set_commission_services(commission_services)
        self.__commision_products = self.set_commission_products(commission_products)
        self.math_module = mathlogic()
    
    @classmethod
    def create_and_append_employee(cls,employeelist):
        name = input('Input your Employees Name: ')
        hourly = float(input('Input hourly rate: '))
        commisson_services = float(input('Input Commisson for Services: '))
        commisson_products = float(input('Input Commisson for products: '))
        newEmployee = cls(name,hourly,commisson_services,commisson_products)
        employeelist.append(newEmployee)
        return(newEmployee)

    def __str__(self):
        return f"Employee: name={self.get_name()}, Hourly_Rate={self.get_hourly_rate()},Commisson_services={self.get_commission_services()},Commisson_Products={self.get_commission_products()}"    

    #Getters for Private Variables
    def get_hourly_rate(self):
        return(self.__hourly_rate)
    
    def get_name(self):
        return(self.__name)
    
    def get_commission_services(self):
        return(self.__commission_services)
    
    def get_commission_products(self):
        return(self.__commision_products)
    
    #setters for Private Variables
    def set_hourly_rate(self,new_hourly_rate):
        self.__hourly_rate = new_hourly_rate
        return self.__hourly_rate
    
    def set_name(self, new_name):
        self.__name = new_name
        return self.__name
    
    def set_commission_services(self,new_commission_services):
        self.__commission_services = new_commission_services
        return self.__commission_services
    
    def set_commission_products(self,new_commission_products):
        self.__commision_products = new_commission_products
        return self.__commission_services
    
