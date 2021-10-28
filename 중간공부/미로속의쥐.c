#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 1000
#define TRUE 1
#define FALSE 0
#define N 4
#define M 5

int n=N, m=M; //미로의 크기

int fx,fy; //최종목적지
int visited[N][M]; //방문여부를 검사하기 위한 배열

//본격적인 맵 탐색을 위한 함수
int IsReachable(int maze[N][M]){
    int i=0,j=0;
    
    Stack stack;        //스택 만들고
    StackInit(&stack);  //스택 초기화

    Data temp;  //첫 시작점 데이터를 0,0좌표의 방향0 으로 설정
    temp.x=i;
    temp.y=j;
    temp.dir=0;

    push(&stack, temp);
    

    //스택이 빌 때까지 반복
    while(!IsEmpty(&stack)){
        
        temp = pop(&stack); //스택에서 제일 위에있는 데이터를 가져옴
        int d = temp.dir;   //가져온 정보에서 좌표랑 이동방향을 분리
        int i = temp.x;
        int j = temp.y;

        temp.dir++;         //방향을 증가시키면서
        push(&stack, temp); //탐색

        if (i==fx && j ==fy){ //도착점에 도착하면 스택내용을 출력
            printStack(&stack);
            return TRUE;
        }

        if (d==0){ //UP //i-1이 한칸 위를 뜻 함
            if(i-1 >= 0 && maze[i-1][j] && visited[i-1][j]){ //순서대로 윗칸이 맵 범위에서 벗어나지 않았고, 길이 맞고, 방문하지 않았다면
                Data temp1;     //해당좌표 데이터를 생성
                temp1.x=i-1;
                temp1.y=j;
                temp1.dir=0;

                visited[i-1][j] = FALSE;    //방문처리
                push(&stack, temp1);        //해당좌표 데이터 스택에 푸쉬
            }
        }
        else if(d==1){ //LEFT
            if(j-1 >=0 && maze[i][j-1] && visited[i][j-1]){
                Data temp1;
                temp1.x=i;
                temp1.y=j;
                temp1.dir=1;

                visited[i][j-1] = FALSE;
                push(&stack, temp1);
            }
        }
        else if(d==2){ //DOWN
            if(i+1 < n && maze[i+1][j] && visited[i+1][j]){
                Data temp1;
                temp1.x=i+1;
                temp1.y=j;
                temp1.dir=2;

                visited[i+1][j] = FALSE;
                push(&stack, temp1);
            }
        }
        else if(d==3){ //RIGHT
            if(j+1 < m && maze[i][j+1] && visited[i][j+1]){
                Data temp1;
                temp1.x=i;
                temp1.y=j+1;
                temp1.dir=3;

                visited[i][j+1] = FALSE;
                push(&stack, temp1);
            }
        }
        else{
            visited[temp.x][temp.y] = TRUE;
            temp = pop(&stack);
        }
    }
    return FALSE;
}

//스택에 들어가는 데이터값 : x,y좌표랑 상하좌우값(dir)
typedef struct Data{
    int x;
    int y;
    int dir;
}Data;


typedef struct _stack{
    Data arr[MAX_LEN];
    int top;
}Stack;



Data pop(Stack *sp){
    Data data;
    data.x=-1;
    data.y=-1;
    data.dir=-1;
    if(IsEmpty(sp))
        return data;
    return sp->arr[(sp->top)--];
}

void push(Stack *sp, Data data){
    if((sp->top)+1 >= MAX_LEN)
        return;
    sp->top++;
    sp->arr[sp->top] = data;
}

void StackInit(Stack *sp){
    sp->top = -1;
}


int IsEmpty(Stack *sp){
    if(sp->top == -1)
        return TRUE;
    return FALSE;
}



void printStack(Stack *sp){
    printf("Stack : ");
    for (int i=0; i<=(sp->top); i++){
        printf("%d %d %d  ", sp->arr[i].x, sp->arr[i].y, sp->arr[i].dir);
    }
    printf("\n");
}

int main()
{
    memset(visited, TRUE, sizeof(visited)); //visited배열의 값을 TRUE로 세팅

    int maze[N][M]={ //맵 그려주고
        {1,0,1,1,0},
        {1,1,1,0,1},
        {0,1,0,1,1},
        {1,1,1,1,1}
    };

    fx=2;       //도착점
    fy=3;       //도착점

    if(IsReachable(maze)){      //maze값이 TRUE가 나오면 (길을 찾았다면)
        printf("Path Found!\n");
    }
    else
        printf("Path Not Found!\n");

    return 0;
}


