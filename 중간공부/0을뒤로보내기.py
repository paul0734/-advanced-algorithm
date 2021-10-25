## 1. 리스트를 2개 사용
a=[2,3,0,0,4,0,6]
b=[]
count=0
for i in a:
    if i != 0:
        b.append(i)
        count+=1
for i in range(count, len(a)):
    b.append(0)

print(b)



## 2. 리스트를 1개 사용
a=[2,3,0,0,4,0,6]
j=0
count=0
for i in a:
    if i != 0:
        a[j]=i
        j+=1
for i in range(j, len(a)):
    a[i]=0

print(a)

# 2,3,0,0,4,0,6 -> 2,3,4,6,0,0,0
