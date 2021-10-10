#include <stdio.h>
#include <stdbool.h>

bool visited[9];
int graph[9][3] = {{0,}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

int dfs(int x){
    visited[x]=true;
    printf("%d ", x);

    for(int node=0; node < 3; node++){
        if(graph[x][node]){
            int value = graph[x][node];
            if(!visited[value]){
                dfs(value);
            }
        }
    }   
}


int main(void){
    dfs(1);
}
