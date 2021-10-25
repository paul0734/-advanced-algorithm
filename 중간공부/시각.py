h = int(input())

count=0

for i in range(h+1): #0~h시
        for j in range(60): #0~59분
                for k in range(60): #0~59초
                        if '3' in str(i) + str(j) + str(k):  #str로 바꾸는 이유는 -> 3+3=6, '3'+'3'='33'
                                count+=1
                                
print(count)


#h시 59분 59초 까지 숫자 3이 얼마나 들어가는지 카운트 하는 문제
#가능한 경우의 수를 모두 검사해보는 완전 탐색 문제
