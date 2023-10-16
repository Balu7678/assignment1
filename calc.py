class Calculator:
    def add(self,a,b):
        return(a+b)

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b
    
cal=Calculator()

while True:
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    
    ch = int(input("Select operation: "))
    

    if ch in (1, 2, 3, 4, 5):
        
        if(ch == 5):
            break
               
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if(ch == 1):
            print(a, "+", b, "=", cal.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", cal.sub(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", cal.mul(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", cal.div(a, b))
    
    else:
        print("Invalid Input")
