from Employee import Employee
class mathlogic():
    #constructor to hold the math logic
    def __init__(self):
        self.__weekpay = 0


    #def weekly_pay(self,employee,hourly_rate,hours_worked,commisson_rate,totalamount):
        #return()
    
    #Parametrs: self,Employee,Commison_rate,total_$_amount_services
    #returns: the total amount to be paid to the employee in commisson
    def total_made_commison_from_services(self,employee,total_amount_services):
        commison_rate_services = Employee.get_commission_services(employee)
        commison_to_pay_services = round(total_amount_services * commison_rate_services,2)
        return commison_to_pay_services
    
    #Parametrs: self,Employee,,total_$_amount_products
    #returns: the total amount to be paid to the employee in commisson for products
    def total_made_commissom_from_products(self,employee,total_amount_products):
        commison_rate_products = Employee.get_commission_products(employee)
        commison_to_pay_products = round(total_amount_products * commison_rate_products,2)
        return commison_to_pay_products
    
    #Parametrs: self,Employee,total_hours_worked
    #returns: the total to be paid for houly
    def total_from_weekly_pay(self,employee,hours_worked):
        total_hourly_to_pay = Employee.get_hourly_rate(employee) * hours_worked
        return total_hourly_to_pay
    
    def final_weekly_pay(self):
        
