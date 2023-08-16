#Q1

# s1=int(input("enter size of list1: "))
# s2=int(input("enter size of list2: "))
# l1=[]
# l2=[]
# l3=[]
# for i in range(0,s1):
    
#     e1=int(input("enter value for index"+str(i)+":"))
#     l1.append(e1)
# for j in range(0,s2):
#     e2=int(input("enter value for index"+str(j)+":"))
#     l2.append(e2)
# print(l1)
# print(l2)
# l1.extend(l2)#using extend 
# print(l1)
# l1=l1+l2 # using concatination
# print(k)

#Q2
# s1=int(input("enter size of list1: "))
# l1=[]
# sol=0
# for i in range(0,s1):
#     e1=int(input("enter value for index"+str(i)+":"))
#     l1.append(e1)
# print(l1)
# for i in range(len(l1)):
#     sol=sol+l1[i]
# print("sum of elements: ",sol)

#Q3 and Q4
# s1=int(input("enter size of list1: "))
# l1=[]
# en=[]
# od=[]
# for i in range(0,s1):
#     e1=int(input("enter value for index"+str(i)+":"))
#     l1.append(e1)
# print(l1)
# for num in l1:
#     if num %2 == 0:
#         en.append(num) 
#     elif num %2 != 0:
#         od.append(num)
# print(en)
# print(od)

#Q5

# s1=int(input("enter size of list1: "))
# l1=[]
# for i in range(0,s1):
#     e1=int(input("enter value for index"+str(i)+":"))
#     l1.append(e1)
# print(l1)
# del l1[6] # also using slice [6:78]
# print(l1)
# l1.pop()# it removes default last element
# print(l1)

#Q6 and Q7
# s1=int(input("enter size of list1: "))
# l1=[]
# for i in range(0,s1):
#     e1=int(input("enter value for index"+str(i)+":"))
#     l1.append(e1)
# print(l1)
# l1.insert(4,13) > using index 
# l1.insert(10,56) > index value is out of range value add into last and also using negative index through last value.
# print(l1)

#Q8

# s1=int(input("enter size of list1: "))
# l1=[]
# for i in range(0,s1):
#     e1=int(input("enter value for index"+str(i)+":"))
#     l1.append(e1)
# print(l1)
# s2=int(input("enter size of list1: "))
# l2=[]
# for j in range(0,s2):
#     e2=int(input("enter value for index"+str(j)+":"))
#     l2.append(e2)
# print(l1)
# l1.sort()
# l2.sort()
# if l1==l2:
#     print("same")
# elif len(l1)==len(l2):
#     print("same")
# else:
#     print("not same")
