'''a=[1,2,3,4,5,6,"python","program"]
for i in range(0,7,2):
    print(i,end=" ")

i=1
while(i<10):
    print(i,end=" ")
    i=i+1


#prime
a=int(input("enter first number"))
b=int(input("enter second number"))
for n in range(a,b):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n,end=" ")
'''
#To check break,contuniue, pass

k=20
for i1 in range(0,k):
    print(i1)
    break
    print(i1+1)
print(i1)

k=20
for i1 in range(0,k):
    print(i1,end=" ")
    continue
    print("program")
print("python")
k=20
for i1 in range(0,k):
    print(i1,end=" ")
    pass
    print("program")
print("python")