def dfs(graph, v, visited):
        visited[v]=True #처음 시작한 노드 방문처리
        print(v, end=" ")
        for i in graph[v]: #시작한 노드의 인접노드들 접근
                if visited[i] == False: #만약 방문하지 않았다면
                        dfs(graph, i, visited) #방문
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

dfs(graph, 1, visited)
