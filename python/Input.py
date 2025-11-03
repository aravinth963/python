name = input("Enter your name: ")

print("Hello " + name)


#Sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1+num2
print("sum of two number is = ",  sum)



#Average

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

avg = (float(A+B+C)/3)

print("Average number is: ", avg)



#Area of Rectange

length = float(input("Enter length of Rectange: "))
breath = float(input("Enter breath of Rectange: "))

print("Area of Rectange : " , (float(length * breath)))


#Simple interest

p = float(input("Enter your principle: "))
r = float(input("Enter your rate: "))
t = float(input("Enter the time: "))

SI = (p*r*t) / 100

print("your simple interest is: ", SI)