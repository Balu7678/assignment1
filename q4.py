string = "aefvvnbfvbdgf"
# number of words
n = len(string)
print(n)
 
if n%2 == 0:
  string1 = string[0:n//2]
  print("First Half of String:",string1)
  
else:
  string1 = string[0:(n//2+1)]
  print("First Half of String:",string1)
  


