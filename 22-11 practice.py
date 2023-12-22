#Write a program to reverse an integer in Python.
# num=1234
# s=str(num)
# print(s[::-1])

# num=34567
# r_num=0
# while num!=0:
#     d=num%10
#     r_num=r_num*10+d
#     num=num//10
# print(r_num)


#Write a program in Python to check whether an integer is Armstrong number or not.

# num=153
# t=num
# s=0
# while num >0:
#     d=num%10
#     s=s+d**3
#     num=num//10
# if s==t:
#     print("it is armstrong number")
# else:
#     print("it is not armstrong")

#palindrome

# s="MadaM"
# l=s[::-1]
# if s==l:
#     print("palindrome")
# else:
#     print("it is not palindrome")

# n=123454321
# t=n
# l=0
# while n!=0:
#     d=n%10
#     l=l*10+d
#     n = n//10
# print(l)
# if t==l:
#     print("palindrome")
# else:
#     print("not a palindrome")


#leap or not

# year=int(input("enter a year:"))

# if (year % 400==0) and (year % 100==0):# ending with 00 it is a century year
#     print("{} it is leap year".format(year))
# elif(year%4==0) and (year%100 !=0):  #ending not  00 it is not a century year
#     print("{} it is leap year".format(year))
# else:
#     print("{} it is not a leap year".format(year))

#remove char given string

# s="marolix"
# s1="o"
# if s1 in s:
#     s2=s.replace("o","")
# print(s2)

#count char

# s="marolix technology"
# s1="o"
# c=0
# for i in s:
#     if s1 == i:
#         c=c+1
# print(c)

# anagram

# s="tub"
# s1="but"
# if len(s) == len(s1):

#     s_s=sorted(s)
#     s_s1=sorted(s1)

#     if s_s == s_s1:
#         print(s,"and",s1,"is a anagram")
#     else:
#         print(s,"and",s1,"is not a anagram")

# else:
#     print(s,"and",s1,"is not a anagram")

#delete vowels in string

# s="marolix technology"
# s1=['a','e','i','o','u']
# s2=""
# for i in s:
#     if i not in s1:
#         s2=s2+i
# print(s2)

# count occurence of vowels and consonants

# s="marolixtechnology"
# s1=['a','e','i','o','u']
# vc=0
# cc=0
# for i in s:
#     if i in s1:
#         vc=vc+1
#     else:
#         cc=cc+1
# print("Consonant count is:",cc)
# print("Vowels count is:",vc)

# highest frequency value of string
# s="mar"
# print(max(s))

# first vowel in string replace '-'

# s="marolix"
# s1=['a','e','i','o','u']
# c=0
# for i in s:
#     if i in s1:
#         c=c+1
#         n=s.replace(i,'-')
#     if c == 1:
#         break
# print(n)

# def Fibonacci(n):
 
#     if n < 0:
#         print("Incorrect input")
 
#     elif n == 0:
#         return 0
 
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(9))

# n=10
# n1=0
# n2=1
# n3=n2
# c=0
# print(n1)
# print(n2)
# while c<=n:
#     print(n3,end=" ")
#     c=c+1
#     n1,n2=n2,n3
#     n3=n1+n2

# x = "malayalam"
 
# w = ""
# for i in x:
#     w = i + w
#     print(w)
# if (x == w):
#     print("Yes")
# else:
#     print("No")

# s="123456"

# sum=0
# for i in s:
#     if i.isdigit():

#         sum=sum+i
# print(sum)

# s="marSM"
# print(max(s))

class cal:
    def __init__(self):
        self.num1=int(input("enter number"))
        self.num2=int(input("enter number"))
    def add(self):
        self.addition=self.num1+self.num2
        print(self.addition)
    def mul(self):
        self.multiplication=self.num1*self.num2
        print(self.multiplication)
    def sub(self):
        self.substraction=self.num1-self.num2
        print(self.substraction)
    def div(self):
        self.division=self.num1/self.num2
        print(self.division)

    def process(self):
        while True:
            print("select operation :")
            print("Addition -1")
            print("substraction -2")
            print("multiplication - 3")
            print("division -4")
            print("exit-5")
            section=input("enter")
            if section in  ["1","2","3","4","5"]:
                if section=="1":
                    object.add()
                elif section=="2":
                    object.mul()
                elif section=="3":
                    object.sub()
                elif section=="4":
                    object.div()
                elif section=="5":

                    break
object=cal()
object.process()
