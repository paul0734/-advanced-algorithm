n, price = map(int, input().split())
coin=[]
count=0
for i in range(n):
    coin.append(int(input()))
    
for j in coin[::-1]:
    count+=price//j
    price=price%j
print(count)

#https://www.acmicpc.net/problem/11047
