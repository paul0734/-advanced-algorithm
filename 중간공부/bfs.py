from collections import deque

def bfs(graph, start, visited):
        que = deque([start])  #큐 생성
        visited[start] = True   #시작 노드 방문처리
        while que:  #큐 안에 값이 있으면 실행 -> 큐가 비워지면 종료
                v= que.popleft()  #큐에 있는 값 팝
                print(v, end=" ")  #팝 후 출력
                for i in graph[v]: #인접노드들 검사
                        if visited[i]== False: #인접노드가 방문 안한 노드라면
                                que.append(i) #큐에넣고
                                visited[i] = True #방문처리
graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
]

visited = [False]*9

bfs(graph, 1, visited)
