def add_emp():
    for i in range(n):
        emp_name = input('Enter the name of the employee: ')
        empid = input("Enter employee Id: ")
        designation = input('Enter the employee designation: ')
        email= input("Enter the employee email: ")
        if email.endswith("@gmail.com"):
            employees[emp_name] = [emp_name,empid,email,designation]
        else:
            print("@gmail.com is required")

n = int(input('Enter the number of employee: '))
employees = {}
           
add_emp()

def get_emp():
    name = input('Please Enter selected employee input: ')
    for i in employees:
        for j in employees[i]:
            if (j == name):
                print(employees[i])
            
get_emp()
