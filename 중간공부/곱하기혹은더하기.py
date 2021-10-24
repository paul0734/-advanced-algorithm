#교수님 코드
num = input()
result=int(num[0]) #첫번째 인자 삽입

for i in range(1, len(num)):
    a=int(num[i]) #i 번째 인자 삽입
    if result<=1 or a <=1: #첫번째 인자가 0또는 1이거나, 그 뒤에나오는 인자들이 0또는 1이면 
        result+=a
    else:
        result*=a
print(result)

#내 코드
num = input()
a=0
for i in range(0,len(num)):
    if a==0 or a==1:
        a+=int(num[i])
    else:
        if num[i] == '0' or num[i] =='1':
            a=a+int(num[i])
        else:
            a=a*int(num[i])
print(a)

#숫자가 입력되었을때 곱하거나 더해서 가장 큰 수 만들기
#0 과 1 은 더하고 나머지는 곱하면 됨
#02984 -> 576
