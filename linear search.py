a = []
m =int(input("Enter the no that has to be searched"))
n = int(input("Enter the no. of elements"))
for i in range(0,n):
    a.append(int(input()))

ctr=0
for i in range(0,n):
    if(a[i]==m):
        ctr+=1


if(ctr==1):
    print("Search succesful")
else:
    print("Search unsuccesful")
    
