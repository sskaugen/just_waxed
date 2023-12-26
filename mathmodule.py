from Employee import Employee
class mathlogic():
    #constructor to hold the math logic
    def __init__(self):
        self.__weekpay = 0


    #def weekly_pay(self,employee,hourly_rate,hours_worked,commisson_rate,totalamount):
        #return()
    
    #Parametrs: self,Employee,Commison_rate,total_$_amount_services
    #returns: the total amount to be paid to the employee in commisson
    def total_made_commison_from_services(self,employee,Commisson_rate,total_amount_services):
        commisonRate = Employee.get_commission(employee)
        commison_to_paid = round(total_amount_services * commisonRate,2)
        #print(commison_to_paid) for debugging
        return commison_to_paid
    
    #Parametrs: self,Employee,Commison_rate_products,total_$_amount_products
    #returns: the total amount to be paid to the employee in commisson for products
    def total_made_commissom_from_products(self,employee,Commisson_rate,total_amount_products):
        commisonRateProducts = Employee.get_commission_products(employee)
        commison_to_paid_products = round(total_amount_products * commisonRateProducts,2)
        return commison_to_paid_products
