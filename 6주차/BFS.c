#include <stdio.h>
#include <stdbool.h>
#define MAX 100
bool visited[9];
int graph[9][3] = {{0,}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};
int queue[MAX];

void bfs (int v) {
	// 큐에 관련된 변수 선언
	int front = 0, rear = 0;//front는 큐의 삭제지점, rear는 삽입지점
	
	// 첫번째 추가
	queue[rear] = v;
	rear++;
	// 방문 표시
	visited[v] = true;
	
	// 일단 출력
	printf("%d ", v);
	
	// 너비 우선 탐색(bfs)
	while (front < rear) {
		// 큐에서 꺼내기
		int pop = queue[front];
		front++;
		for (int node = 0; node < 3; node++) {
            if(graph[pop][node]){
                int value = graph[pop][node];
                if(!visited[value]){
                    visited[value] = true;
                    queue[rear]=value;
                    rear++;
                    printf("%d ", value);
                }
            }
		}
	}
}


int main(void){
    bfs(1);
}
