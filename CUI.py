#this file will hold the console user interface for this application
#I plan as using this to test the logic as well as the functionality and update using a GUI
from Employee import Employee
from mathmodule import mathlogic

class CLI():
    @staticmethod
    def Welcome(cls):
        print('Welcome to my Program. I hope this helps make your life a little easier')
        
    @staticmethod
    def create_employees(cls):
        name = input('Input your Employees Name')
        hourly = float(input('Input hourly rate'))
        commisson_services = float(input('Input Commisson for Services'))
        commisson_products = float(input('Input Commisson for products'))
        

cli = CLI()
cli.Welcome()