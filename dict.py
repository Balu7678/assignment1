#q1
# my_dict=eval(input("enter a dictionary : "))
# my_dict[2]=30
# my_dict.update({3:40})
# print(my_dict)

#q2
#my_dict=eval(input("enter a dictionary : "))
#keys =eval(input("enter keys: "))
#for key in keys:
#    if key in my_dict.keys(): #> if value in my_dict.values() 
#        print("already key is exist")
#    else:
#        print("key is not exist")

#q3
# my_dict=eval(input("enter a dictionary :"))
# for key, value in my_dict.items():
#     print(key, value)

#q4
# my_dict={x:x**2 for x in range(1,16)} > same as list and tuple expression and loop , condition
# print(my_dict)
# or
# my_dict=dict()
# for x in range(1,100):
#     if x == 16: 
#         break
#     my_dict[x]=x**2
# print(my_dict)

#q5
# str=input("enter a string: ")
# my_dict={}
# for ch in str:
#     if ch in my_dict:
#         my_dict[ch] +=1
#     else:
#         my_dict[ch]=1
# print(my_dict)

#q6
# my_dict=eval(input("enter a dictionary: "))
# print(sum(my_dict.values())) # using sum(), values()
# #or
# my_dict=eval(input("enter a dictionary: "))
# sum_of_items=0
# for item in my_dict.values(): > loop the dict values using values()
#     sum_of_items=sum_of_items+item > add the values to sum_of_items variable
# print(sum_of_items)

#q7
# my_dict1=eval(input("enter a dictionary: "))
# my_dict2=eval(input("enter a dictionary: "))
# for key in my_dict2:
#     if key in my_dict1:
#         my_dict1[key]=my_dict1[key]+my_dict2[key]
#     else:
#         my_dict1[key]=my_dict2[key]
# print(my_dict1)

#q8
# my_dict=eval(input("enter a dictionary: "))
# # for key in my_dict:
# #     print(key)
# #or
# print(list(my_dict)[0])
# print(list(my_dict)[1])
# print(list(my_dict)[2])
# print(list(my_dict)[3])

#q9
# my_dict=eval(input("enter a dictionary: "))
# #print(my_dict.pop("101")) or
# del my_dict['101'] 
# print(my_dict)

#q10
# my_dict1=eval(input("enter a dictionary: "))
# my_dict2=eval(input("enter a dictionary: "))
# my_dict1.update(my_dict2) # using update method
# print(my_dict1)