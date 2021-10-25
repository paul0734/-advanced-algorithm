n = int(input())

m=list(map(int, input().split()))
sum=0
result=0
m.sort()
for i in range(0, len(m)):#3 1 4 3 2
    sum=sum+m[i]
    result=result+sum

print(result)


# 5
# 3 1 4 3 2 -> 1 2 3 3 4
# 결과 : 32
# 시간을 단축시키기 위해서 오름차순 정렬을 해준다 (앞사람의 시간은 계속 누적되기 때문에)
# 1+3+6+9+13 = 32
