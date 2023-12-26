from Employee import Employee
from mathmodule import mathlogic
#def __init__(self, name, hourly_rate,commission_services,commision_products,start_date,birth_date):
def main():
    emp1 = Employee('Ximena',float(15),float(.07),float(.10),"december 15 2022","march 23 2001")
    print(mathlogic.total_made_commison_from_services(emp1,100))
    print()
    print(mathlogic.total_made_commissom_from_products(emp1,100))
    print()
    print(mathlogic.total_from_weekly_pay(emp1,10)) #expecting 150
    
    emp2 = Employee('Sean',float(15),float(.07),float(.10),"december 15 2022","march 23 2001")
    print(mathlogic.final_weekly_pay(emp2,10,100,100))#expecting 167


#I want to keep this change
if __name__ == "__main__":
    main()