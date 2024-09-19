# ##if condition :
#     statement
# elif condition :
#     statement
# else
#     condition

# name=input("Enter the name:")
# marks=int(input("Enter the Mathematic marks:"))
# if (marks >=90):
#     print("Grade A")
# elif (marks >=80):
#     print("Grade B")
# elif (marks >=60):
#     print("Grade C")
# else :
#     print("Pass")

# num=int(input("Enter the number"))
# if (num > 0):
#     print("Positive no")
# elif (num == 0):
#     print("Zero")
# else :
#     print("Negative Number")

# num1=int(input("Enter the number1:"))
# num2=int(input("Enter the number2:"))
# num3=int(input("Enter the number3:"))
# if (num1<num2) and (num1<num3):
#     print("A is gretaer")
# if (num2<num3):
#     print("B is greater")
# else:
#     print ("C is greater")

# marks=int(input("Enter the marks:"))
# if (marks >=70):
#     print("Grade A")
# elif (marks >=60 and marks <70):
#     print("Grade B")
# elif(marks >=50 and marks <60):
#     print("Grade C")
# elif (marks >=40 and marks <50):
#     print("Grade D")
# else:
#     print("Fail")
#
# inum=[1,2,3,4,5]
# inum2=[]
#
# for t in inum:
#    inum2.append(t*t)
#
# print(inum2)
#
# l1=[1,2,3,4,5,6,7]
# l2=0
# l3=0
#
# for m in l1:
#     if (m % 2 == 0):
#         l2 = l2+m
#     else:
#         l3=l3+m
#
# print("Sum of Even Numbers in ist:",l2)
# print("Sum of odd Numbers in ist:",l3)
# print("Total",l2+l3)

# str = 'AAnjini'

# for i in str.lower():
#     if i in ['a','e','i','o','u'] :
#         break
#
# print("Vowels",i,"is present")
#
# str1 = 'Ranjini'
# value = ''
# value = ''
#
# for i in str1:
#     if i.islower():
#         value = value + i.upper()
#     elif i.isupper():
#         value = value + i.lower()
#
# print(value)

# r=range(200)
# print(r)
#
# for i in r:
#     print(i)

##******sum of odd numbers and Even numbers using for loop with range****#
sum=0
sum1=0

for j in range(0,10):
    if j % 2 ==0:
        sum=sum+j
    elif j % 2 !=0:
        sum1=sum1+j
print(j,end=" ")
print()
print('Sum of odd number',sum1)
print("Sum of even numbers",sum)

# factorial=1
# for i in range(1,6):
#     factorial=factorial*i
#
# print("Factorial of 5",factorial)






