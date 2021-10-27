
def dfs(x,y):
        arr=[]
        arr.append((x,y))                                               #처음시작 장소 스택(리스트)에 추가 0,0
        
        while arr:                                                      #스택(리스트)에 값이 있으면
                x= arr[-1][0]                                           #스택은 나중에 들어온 값을(맨 뒤에있는) 먼저 가져와야 함
                y= arr[-1][-1]                                          #스택은 나중에 들어온 값을(맨 뒤에있는) 먼저 가져와야 함
                del arr[len(arr)-1]                                     #값을 가져왔다면 제일 뒤에있는 값을 삭제(팝)
                for i in range(4):                                      #U D L R 순서로 탐색
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx < 0 or nx >= n or ny < 0 or ny >= m:      #맵 밖으로 나갔다면 패스
                                continue
                        if graph[nx][ny] == 0:                          #0이라면(길이 아니라면) 패스
                                continue
                        if graph[nx][ny] == 1:                          #1이라면(길이라면)
                                graph[nx][ny] = graph[x][y] + 1         #값을 1 증가(카운트)
                                arr.append((nx,ny))                     #스택에 삽입
                                if nx == n-1 and ny==m-1:               #만약 맵의 끝지점에 도달했다면
                                        return graph[n-1][m-1]          #끝지점의 카운트값 리턴
        

n,m =map(int, input().split()) 

graph=[]
for i in range(n):
        graph.append(list(map(int, input())))

dx=[-1,1,0,0]   # U D L R
dy=[0,0,-1,1]   # U D L R

print(dfs(0,0)) # 0 0부터 시작
