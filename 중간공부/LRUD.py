n=int(input())

x,y =1,1
plans=input().split() # R R R U D D

dx=[0,0,-1,1] #L R U D
dy=[-1,1,0,0] #L R U D
movetype=['L','R','U','D']

for plan in plans:
        for i in range(len(movetype)): 
                if plan == movetype[i]:
                        nx=x+dx[i]
                        ny=y+dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n: # 맵 범위에서 나가면 증가시킨 nx,ny를 x,y에 적용시키지 않고 그냥 넘김
                continue

        x,y=nx,ny
print(x,y)

#n개 크기의 맵
#1,1 시작
#RRRUDD입력
#좌표이동
