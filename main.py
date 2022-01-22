# Write a python program to print a dictionary where the keys are numbers between 1 and 159 both included) and the values are cubes of keys
k=0;
dic={}
while k<160:
  dic[k]=k*k*k
  k=k+1

print(dic)
