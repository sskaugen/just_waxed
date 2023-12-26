from Employee import Employee
from mathmodule import mathlogic
#def __init__(self, name, hourly_rate,commission,start_date,birth_date):
def main():
    emp1 = Employee('Ximena',float(15),float(.07),"december 15 2022","march 23 2001")
    mathforemp1 = mathlogic()
    mathforemp1.total_made_commison_from_services(emp1,emp1.get_commission(),565.50)


if __name__ == "__main__":
    main()