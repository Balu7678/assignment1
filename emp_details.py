def emp_details(emp_name,empid,email,domain):
    
    if True:
        name = input('Enter employee name: ')
        info = employees.get(name)
        if info == 0:
            print('Employee does not exist')
            
        else:
            print('emp_name:', emp_name,)
            print('empId: ', empid)
            print('email:', email)
            print('domain: ', domain)
            
n = int(input('Enter the number of employee: '))
employees = {}
    
for i in range(n):
   emp_name = input('Enter the name of the employee: ')
   empid = input("Enter employee Id: ")
   email= (input("Enter the employee email: "))
   domain = input('Enter the employee domain: ')
   employees[emp_name] = [emp_name,empid,email , domain]      
emp_details(emp_name,empid,email,domain)