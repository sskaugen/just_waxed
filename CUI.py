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
        Employee.create_and_append_employee(CLI.employeelist)
    
    @staticmethod
    def search_for_employee(target_name):
        for employee in CLI.employeelist:
            if employee.get_name() == target_name:
                return employee
        return None
    
    @staticmethod
    def change_employee_info(employee_list):
        if len(employee_list) == 0:
            print('There are no employees. PLease create an employee first')
        else:
            target_name = input('what Employees info do you want to change? ')
            print(f"you have selected to change: {target_name}'s attributes")
            status = cli.search_for_employee(target_name)
            if status == None:
                    raise Exception("No employee was found Please re-enter name\n")
            else:
                print(f'{status.get_name()} was found')
            #if choice == 'yes':
               # selection = input('\n\nwhat would you like to change?\nName (n)\nHourl Rate (hr)\nCommisson services (cs) \nCommisson products (cp)\n')
   
    #this will hold the loop that will run the continous logic of this program
    def run():
        return None


        
cli = CLI()
cli.Welcome()
cli.create_employees()
cli.change_employee_info(CLI.employeelist)