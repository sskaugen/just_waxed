
class mathlogic():
    #constructor to hold the math logic
    def __init__(self):
        self.final_weekly_pay_to_employee = 0
        self.commison_to_pay_services = 0
        self.commison_to_pay_products = 0
        self.total_hourly_to_pay = 0
        self.total_revenue_earned = 0
        
    #Parametrs: self,Employee,Commison_rate,total_$_amount_services
    #returns: the total amount to be paid to the employee in commisson
    #this would have to be after tips where deducted
    
    def total_made_commison_from_services(self,employee,total_amount_services):
        from Employee import Employee
        commison_rate_services = employee.get_commission_services()
        self.commison_to_pay_services = round(total_amount_services * commison_rate_services,2)
        return self.commison_to_pay_services
    
    #Parametrs: self,Employee,,total_$_amount_products
    #returns: the total amount to be paid to the employee in commisson for products
    
    def total_made_commissom_from_products(self,employee,total_amount_products):
        from Employee import Employee
        commison_rate_products = employee.get_commission_products()
        commison_to_pay_products = round(total_amount_products * commison_rate_products,2)
        return commison_to_pay_products
    
    #Parametrs: self,Employee,total_hours_worked
    #returns: the total to be paid for houly
    
    def total_from_weekly_pay(self,employee,hours_worked):
        from Employee import Employee
        self.total_hourly_to_pay = employee.get_hourly_rate() * hours_worked
        return self.total_hourly_to_pay
    
    #Parametrs: self,Employee,total_hours_worked,total_products,total_sevices
    #returns: the total to be paid to employee for weekely pay
    
    def final_weekly_pay(self,employee,hours_worked,total_products,_total_services):
        from Employee import Employee
        #calculate the total hourly pay
        total_hourly_to_pay = self.total_from_weekly_pay(employee,hours_worked)
        #calculate the total commisson Services
        total_commisson_services_made = self.total_made_commison_from_services(employee,_total_services)
        #calculate the total commisson Products
        total_commisson_products_made = self.total_made_commissom_from_products(employee,total_products)
        self.final_weekly_pay_to_employee = total_hourly_to_pay + total_commisson_services_made + total_commisson_products_made
        return self.final_weekly_pay_to_employee
    
    #paramaters: self, employee
    #return: total_revenue_earned
    #This will only accurately account for the number if calculation includes total_products, _total_services
    def revenue_after_paying_employee(self,total_products,_total_services):
        gross_money = total_products + _total_services
        self.total_revenue_earned = gross_money - self.final_weekly_pay_to_employee
        return self.total_revenue_earned