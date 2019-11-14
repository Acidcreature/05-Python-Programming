# This program tests the EMPW class exercise

import empw

def main():
    # Create production worker objects
    name = input("What is the Name: ")
    empnum = input("What is the Employee Number: ")
    shift = input("Is the Employee on Shift 1 or 2: ")
    payrate = input("What is the Employee's PayRate: ")
    salary = input("What is the Employee's Salary or N/A: ")
    bonus = input("What is the Employee's Bonus or N/A: ")
    employee = empw.ProWork(name, empnum, shift, payrate)
    shiftsuper = empw.ShiftSuper(name, empnum, salary, bonus)

    #Display Employee info
    print('Name: ', employee.get_name())
    print('Employee Num: ', employee.get_empnum())
    print('Shift: ', employee.get_shift())
    print('Pay: ', employee.get_payrate())

    #Display Shift Supervisor info
    print('Name: ', shiftsuper.get_name())
    print('Employee Num: ', shiftsuper.get_empnum())
    print('Salary: ', shiftsuper.get_salary())
    print('Bonus: ', shiftsuper.get_bonus())
main()

