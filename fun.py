# #q1
# def count_upper_lower(string):
#     uc=0 
#     lc=0
#     ec=0
#     for i in string:
#         if i.isupper():
#             uc=uc+1
#         elif i.islower():
#             lc=lc+1
#         else:
#             ec=ec+1
#     print(uc)
#     print(lc)
#     print(ec)
# my_string=input("enter a string: ")
#count_upper_lower(my_string)

#q2
# def sort(l):
#     new_list=[]
#     for i in l:
#         if i not in new_list:
#             new_list.append(i)
#     print(new_list)
# l1=eval(input("enter a list : "))
# sort(l1)

#q3
# def ispangram(str):
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    for char in alphabet:
#       if char not in str:
#          return False
#    return True
# string =input("Enter a string : ")
# if(ispangram(string)==True):
#    print("pangram")
# else:
#    print("not pangram")

#q4
# def square_list():
#     # my_list=[x**2 for x in range(1,11)]
#     # print(my_list)
#     or
#     l=[]
#     for x in range(1,11):
#         l.append(x**2)
#     print(l)
# square_list()

#q5
# def sum(list):
#     total=0
#     for i in list:
#         total += i
#     print(total)
# sum(eval(input("enter list :")))

#q6
# def mySum(*n):
#     print(n)
#     sum = 0
#     for i in n:
#         sum = sum + i
#     print(sum)
# mySum(1,2,8,9,6,5,7,4,3)
