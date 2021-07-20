n=int(input("enter the no"))
ctr=0
if (n>1):
    for i in range(2,n):
        if((n%i)==0):
            ctr=ctr+1
            break
        
else:
    print("not prime")

if(ctr==1):
    print("its not prime")
else:
    print("its prime")


f = 1;
if(ctr==1):
    
        for i in range(1,n+1):
            f *= i;
            

print("Factorial is")         
print(f)
