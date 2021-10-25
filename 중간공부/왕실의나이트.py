
input_data = input() #a1
col = int(ord(input_data[0])) - int(ord('a')) + 1
# ord함수는 해당 문자의 아스키값 리턴 a -> 97
row = int(input_data[1])

#나이트가 이동할 수 있는 방향 8가지 (체스)
step=[(-2,-1),(-2,1),(2,1),(2,-1),(1,-2),(1,2),(-1,2),(-1,-2)]

count=0
for steps in step: #모든 방향에 대해 검사 ex) -2, -1
        next_row = row+steps[1] # -1
        next_col = col+steps[0] # -2

        #체스판은 1~8사이즈의 8x8 사이즈가 조건이기 때문에 해당 위치로 이동이 가능하면 카운트
        if next_row >=1 and next_row <=8 and next_col >= 1 and next_col <= 8:
                count+=1
print(count)


# 1~8, a~h 8x8사이즈의 체스판
#체스룰 - 나이트
#나이트가 이동가능한 곳이 있는지 탐색 -> 모든 경우를 전부 탐색해보는 완전탐색사용
