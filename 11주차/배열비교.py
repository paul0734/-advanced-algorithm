#배열에서 어떤 수를 기준으로 왼쪽값들이 기준값보다 작고 오른쪽값들이 기준값보다 큰 조건이 성립한다면 그 기준값의 인덱스 출력
#5,1,4,3,6,8,10,7,9 -> 6을 기준으로 조건이 성립됨 -> 출력 4

def findElement(arr,n):
    leftMax=[0]*n                   #크기 9의 왼쪽값들 비교 배열 생성
    rightMin=[0]*n                  #크기 9의 오른쪽값들 비교 배열 생성

    leftMax[0]=min(arr)             #왼쪽비교배열의 첫 인덱스 최소값으로 세팅
    rightMin[n-1]=max(arr)          #오른쪽비교배열의 첫 인덱스 최댓값으로 세팅

    for i in range(1,n-1):          #왼쪽부터 비교하면서 가장 큰값들로 비교배열을 채움
        if(leftMax[i-1]>arr[i-1]):
            leftMax[i]=leftMax[i-1]
        else:
            leftMax[i]=arr[i-1]

    for i in range(n-2,0,-1):       #오른쪽부터 비교하면서 가장 작은값들로 비교배열을 채움
        if(rightMin[i+1]>arr[i+1]):
            rightMin[i]=arr[i+1]
        else:
            rightMin[i]=rightMin[i+1]

    for i in range(0,n):            #조건검사
        if((leftMax[i]<arr[i]) & (rightMin[i]>arr[i])):
            return i
    return -1




arr=[5,1,4,3,6,8,10,7,9]
n=len(arr)
idx=findElement(arr,n)
print(idx)
