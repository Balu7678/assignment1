#Q1 using replace 

#s = 'sdf vhj gvfk nvn'
#print(len(s))
#s1 = s.replace('j', '')
#print(len(s1))
#print(s1)

#Q2 reversed the string

#s = 'balulab'
#rev_s = reversed(s)
#print(rev_s)
#if list(s) == list(rev_s):
#   print("The string is palindrome.")
#else:
#   print("The string is not palindrome.")

#method 2

#s=input("enter input : ")
#if (s==s[::-1]):
#    print("The string is palindrome.")
#else:
#    print("The string is not palindrome.")

#Q3

#c=input("enter input: ")
#if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
#    print("vowel")
#else:
#    print("consonant")

#Q4

#s = input("Enter String : ")
#s1 = ''  
#c = input("Enter Character : ")
#for i in s:  
#        if i == ' ':  
#            i = c   
#        s1 += i   
#print(s1)

#Q5

#s1 = input("Enter String : ")
#ac = 0  # alphabets count
#dc = 0  # digits count
#sc = 0  # special char count

#for i in range(len(s1)):
 #   if((s1[i] >= 'a' and s1[i] <= 'z') or (s1[i] >= 'A' and s1[i] <= 'Z')): # using s1.isalpha()
 #       ac = ac + 1 
 #   elif(s1[i] >= '0' and s1[i] <= '9'): # using s1.isdigit()
 #       dc = dc + 1
 #   else:
 #       sc = sc + 1
        
#print(ac)
#print(dc)
#print(sc)

#Q6

#s=input("enter string : ")
#s1=s.replace(" ","")
#print(s1)

#Q7

#s=input("enter string: ")
#sum=0
#for i in s:
#    if i.isdigit(): >i>=0 or i<=9
#        sum=sum+int(i)
#print(sum)  

#Q8

#s=input("enter string: ")
#r=""
#for i in s:
#    if i not in r:
#        r=r+i
#print(r)

#Q9

#s=input("enter string: ")
#chr=input("enter char: ")
#oc=0
#for i in s:
#    if i==chr:
#        oc=oc+1
#print(oc)

#Q10

#s="top"
#s1="pot"
# some cases using lower(), upper()
#if sorted(s)==sorted(s1): > sorted strings
#    print(s,"and",s1,"are anagram")
#else:
#    print(s,"and",s1,"are not anagram")

#Q11

#a="xhfvuvxvcgd2rr@^@"
#a1=''.join(sorted(a)) # a1=sorted(a) 

#print(a1[::-1]) > print reversed order