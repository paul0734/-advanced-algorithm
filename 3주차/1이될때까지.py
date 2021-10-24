num, k = map(int, input().split())
count=0
while(1):
    if num%k==0:
        count+=1
        num=num//k
    elif num<k: #num이 k보다 작을때 (더 이상 나눌 수 없을때) break
        break
    else:
        num=num-1
        count+=1

print(count)

#num이 1이 될때까지 1을 빼거나, k로 나누거나 -> 나누는게 더 빠르게 1에 도달하므로 나눌수 있으면 
#25 5 => 2
