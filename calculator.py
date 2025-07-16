#Simple Calculator
print(
'''************
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponent
6.Floor division
**************''')
print("ADDITION")
print("Enter two numbers to add")
#prompts a user to enter first number
first_number = (input("Enter first number:"))
#prompts a user to enter second number
second_number = (input("Enter second number:"))
sum =float(first_number) + float(second_number)
print(f"{first_number} + {second_number} is = {sum:.2f}")


print("***********")
print("SUBTRACTION")
print("Enter two numbers to subtract")
#prompts a user to enter first number
first_number = (input("Enter first number:"))
#prompts a user to enter second number
second_number = (input("Enter second number:"))
sub =float(first_number) - float(second_number)
print(f"{first_number} - {second_number} is = {sub:.2f}")
 
print("***********")
print("MULTIPLICATION")
print("Enter two numbers to multiply")
#prompts a user to enter first number
first_number = (input("Enter first number:"))
#prompts a user to enter second number
second_number = (input("Enter second number:"))
mul =float(first_number) * float(second_number)
print(f"{first_number} * {second_number} is = {mul:.2f}")

print("***********")
print("DIVISION")
print("Enter two numbers to divide")
#prompts a user to enter first number
first_number = (input("Enter first number:"))
#prompts a user to enter second number
second_number = (input("Enter second number:"))
div =float(first_number) / float(second_number)
print(f"{first_number} / {second_number} is = {div:.2f}")
  
 

print("***********")
print("EXPONENTIAL")
print("Enter two numbers to exponent")
#prompts a user to enter first number
first_number = (input("Enter first number:"))
#prompts a user to enter second number
second_number = (input("Enter second number:"))
expo =float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} is = {expo:.2f}")
 
print("***********")
print("FLOOR DIVISION")
print("Enter two numbers to divide")
#prompts a user to enter first number
first_number = (input("Enter first number:"))
#prompts a user to enter second number
second_number = (input("Enter second number:"))
div =float(first_number) // float(second_number)
print(f"{first_number} // {second_number} is = {div:.2f}")
 

