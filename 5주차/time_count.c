#include <stdio.h>
#include <stdbool.h>
//n을 입력했을 때 0부터 n시 59분 59초 안에 3이 얼만큼 등장하는지 카운트하는 문제

bool check(int h, int m, int s){
    if(h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3)
			return true;
		return false;
}

int main(void){
    int h=0; 
    int cnt=0;
    scanf("%d",&h);
    for(int i=0; i<=h; i++) {
        for(int j=0; j<60; j++) {
            for(int k=0; k<60; k++) {
                if(check(i,j,k)) cnt++;
            }
        }
	}
    printf("%d", cnt);
}
