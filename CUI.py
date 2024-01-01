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
    
    #This method handles the 
    @staticmethod
    def handle_info_change(employee,choice):
        if choice == n:
            empname = input('Input New Name\n')
            employee.set_name(empname)
        elif choice == hr:
            emphourly = input('Input New Hourly Wage\n')
            employee.set_hourly_rate(emphourly)
        elif choice == cs:
            empcommissonservices = input('input New Commisson for Services\n')
            employee.set_commission_services(empcommissonservices)
        elif choice == cp:
            empcommissonproducts = input('input new Commisson for Products\n')
            employee.set_commission_products(empcommissonproducts)
        else:
            print('Nothing has been changed. Returning to starting page.')
        return employee


    @staticmethod
    def change_employee_info(employee_list):
        if len(employee_list) == 0:
            print('There are no employees. PLease create an employee first')
        else:
            target_name = input("what Employee's info would you like to change? ")
            print(f"you have selected to change: {target_name}'s attributes")
            status = CLI.search_for_employee(target_name)
            while status == None:
                   status = input('No employee by that name please re-enter name: ')
                
            else:
                print(f'{status.get_name()} was found')
                selection = input('\n\nwhat would you like to change?\nName (n)\nHourly Rate (hr)\nCommisson services (cs) \nCommisson products (cp)\n')
                selection_lower_case = selection.lower()
                while selection != n or hr or cs or cp:
                    print('invalid command insert a proper command\n Change name (n)\nChange Hourly Rate (hr)\nChange Commisson Services (cs)\nChange Commission Products (cp)\n')
                    selection = input('Input Proper Command Here: ')
                
                
                        

    #this will hold the loop that will run the continous logic of this program
    def run():
        return None


#have to catch and handle my Exception
cli = CLI()
cli.Welcome()
cli.create_employees()
cli.change_employee_info(CLI.employeelist)