def list1(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
#a=[1,2,3,4,2,3,5,6,4,8,7]
a=list(map(int,input().split()))
print(a)
print(list1(a))
