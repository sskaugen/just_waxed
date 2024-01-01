#this file will hold the console user interface for this application
#I plan as using this to test the logic as well as the functionality and update using a GUI
from Employee import Employee
from mathmodule import mathlogic

class CLI():
    #class methods
    employeelist = []

    @staticmethod
    def Welcome():
        print('Welcome to my Program. I hope this helps make your life a little easier')
        
    @staticmethod
    def create_employees():
        Employee.create_and_append_employee(CLI.Employeelist)
        
    
    @staticmethod
    def change_employee_info(employee_list):
        if len(employee_list) == 0:
            print('There are no employees. PLease create an employee first')
        else:
            info = input('what Employees info do you want to change?  ')
            print(f'you have selected to changed: {info}')
            choice = input('Is that correct? Input yes or no')
            if choice == 'yes':
                selection = input('what would you like to change?\nName (n)\nHourl Rate (hr)\nCommisson services (cs) \nCommisson products (cp)')
   
    #this will hold the loop that will run the continous logic of this program
    def run():
        return None


        
cli = CLI()
cli.Welcome()
cli.create_employees()
cli.change_employee_info(Employeelist)