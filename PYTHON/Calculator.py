#step 1: Ask the user to input first 

num1 = float(input("Enter the first number: "))

#step 2: Ask the user to input second number

num2 = float(input("Enter the second number: "))

#step 3: Ask the user to input an operator

operation =input("Enter an operator (+, *, /, -, %)):")

#step 4: use if -elif -else to perform the operation based on the operator input

if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '*':                                                                                                                          
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '-':                                                                                                                           
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '%':                                                                                                                           
    result = num1 / num2
    print(f"{num1} % {num2} = {result}")

elif operation == '/':    
    if num2 != 0:                                                                                                                       
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error:Cannot divide by zero")
        
else:
    print("Invalid operator.please enter (+, *, /, -, %)")

