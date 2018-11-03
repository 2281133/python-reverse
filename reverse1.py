def reverse(h): 
  str = "" 
  for i in h: 
    str = i + str
  return str
h ="Hrutvik"  
print("The string is:",end="") 
print(h)   
print("The reversed string is:",end="") 
print(reverse(h)) 
