n = int(input())
#exclusiveor 사용// 1을 익스클루시브 했을때 +1이 되면 짝수, -1이되면 홀수
def isEven(num):
    if (num^1) == (n+1):#짝수
        return 0
    else:               #홀수
        return 1
if isEven(n) == 1:
    print("Even")
else:
    print("Odd")

#and 사용 // 1을 and 했을때 1이나오면 홀수 0이 나오면 짝수
# def isEven(num):
#     return (n&1)
