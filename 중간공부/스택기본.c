#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 1000
#define TRUE 1
#define FALSE 0
typedef char Data;

//스택 생성하는 구조체
typedef struct _stack{
    Data arr[MAX_LEN];
    int top
}Stack;


//스택 초기화하는 함수 (top값을 -1로 세팅)
void StackInit(Stack *sp){
    sp->top = -1;
}


//스택이 비어있는지 확인하는 함수
int IsEmpty(Stack *sp){
    if(sp->top == -1)                   //스택의 top이 -1이라면 스택이 비어있는 것이므로 TRUE리턴
        return TRUE;
    return FALSE;                       //스택에 값이 있으면 FALSE 리턴
}


//스택에 값 넣는 push 함수
void push(Stack *sp, Data data){
    if((sp->top)+1 >= MAX_LEN)          //만약 스택의 top+1값이 최대치를 넘으면 아무작업도 하지않고 리턴
        return;
    sp->top++;                          //스택에 값을 넣기때문에 top증가
    sp->arr[sp->top] = data;            //스택에 값 push
}


//스택에서 팝(데이터를 지움과 동시에 가져오는 것)
Data pop(Stack *sp){
    if(IsEmpty(sp))                     //스택이 비어있다면 가져올게 없음
        return ' ';
    return sp->arr[(sp->top)--];        //스택에서 제일 위에있는 값을 가져오고 top을 감소  (반드시 값을 가져온 뒤 top을 감소시켜야 함)
}


//스택 안 데이터를 출력해주는 함수
void printStack(Stack *sp){
    printf("Stack\n");
    for(int i=0; i<=(sp->top); i++){    //스택의 제일 밑(0)부터 top까지 출력
        printf("%c", sp->arr[i]);
    }
    printf("\n");
}




int main()
{
    Stack stack;                       //스택생성
    StackInit(&stack);                 //스택초기화

    push(&stack, 'a');                 //스택에 데이터 푸쉬
    push(&stack, 'b');
    push(&stack, 'c');

    printStack(&stack);                //스택의 내용 출력

    pop(&stack);                       //스택에서 데이터 가져오기

    printStack(&stack);


    return 0;
}
