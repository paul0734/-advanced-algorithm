#비열비교1는 조건에 해당되는 인덱스 하나만 출력하지만 배열비교2는 조건에 해당하는 인덱스 모두를 출력한다

def findElement(arr,n):
    leftMax=[0]*n
    rightMin=[0]*n

    leftMax[0]=min(arr)
    rightMin[n-1]=max(arr)

    for i in range(1,n):
        if(leftMax[i-1]>arr[i-1]):
            leftMax[i]=leftMax[i-1]
        else:
            leftMax[i]=arr[i-1]

    for i in range(n-2,-1,-1):
        if(rightMin[i+1]>arr[i+1]):
            rightMin[i]=arr[i+1]
        else:
            rightMin[i]=rightMin[i+1]

    for i in range(0,n):
        if((leftMax[i]<=arr[i]) & (rightMin[i]>=arr[i])):
            print(i, end=" ")
    return -1




arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
findElement(arr,n)
