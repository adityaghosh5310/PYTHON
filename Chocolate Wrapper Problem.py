print("Enter the shopkeepers offering")
sumc=0
w=int(input("Enter the no. of wrappers required to get m chocolate"))
m=int(input("input the no. of chocolates Ram will get by giving w wrappers"))
x=int(input("Enter the no. of chocolates own by Ram"))
wr=x
if(wr>=w):
    c=((m/w)*wr)
    sumc=sumc+c
    wr=c

print(sumc)
