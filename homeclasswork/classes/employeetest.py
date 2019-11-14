# This program tests the Employee Class
import employeeclass as e



def main():
    # Get a list of employee's
    employees = employee_list()

    #display the list
    print('Empolyee information on record: ')
    display_list(employees)

#Makes a list for employee objects.
def employee_list():
    # Create empty list
    employee_list = []

    # Adds information for employees
    print('Employee info being entered:')
    for count in range(1, 4):
        name = input('Name: ')
        ID = input('ID Number: ')
        dep = input('Department: ')
        job = input('Job Title: ').title()
        print()

        #Create a new employee object in memory
        employee = e.Employee(name, ID, dep, job)

        # Add the object to the list
        employee_list.append(employee)
    # returns list
    return employee_list

# The display_list function accepts a list as arg
# and displays the data.

def display_list(employee_list):
    for employee in employee_list:
        print(employee.get_name())
        print(employee.get_ID())
        print(employee.get_dep())
        print(employee.get_job())
        print()

main()

        
