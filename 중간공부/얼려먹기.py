

def dfs(x, y):
        if x<=-1 or x>=n or y <=-1 or y>=m: #만약 맵의 범위를 초과하면 False
                return False
        if graph[x][y]==0:     # 맵의 값이 0이라면
                graph[x][y]=1  # 1로바꾸고
                dfs(x-1, y)    # 상하좌우 탐색 시작
                dfs(x, y-1)
                dfs(x+1, y)
                dfs(x, y+1)
                return True    # 주변에 더 이상 탐색할 0값이 없다면 True 리턴
        return False           # 더 이상 0인 공간이 없다면 False리턴(끝)


n ,m = map(int, input().split())

graph=[]
for i in range(n):
        graph.append(list(map(int, input())))

result=0
for i in range(n):
        for j in range(m):
                if dfs(j,i) ==True:
                        result+=1
print(result)


# 4 5
# 00010
# 00011
# 11111
# 00000   --> 3 출력

# 0인 공간을 하나로 묶어서 몇 묶음인지 푸는 문제
