#include <stdio.h>

//8x8체스판에서 나이트(말)가 이동할 수 있는 경우의 수 구하기
int main(void) {
		//현재 나이트의 위치 입력받기 로우는 1~8 컬럼은 a~h
        char input[1];
		scanf("%s", &input);
		int column = input[0] - 'a'+ 1;
		int row = input[1] - '0';
		
		//나이트가 이동할수 있는 방향 8가지
		int dx[] = {-2,-1,1,2,2,1,-1,-2};
		int dy[] = {-1,-2,-2,-1,1,2,2,1};
		
		//8가지 방향에 대하여 각 위치로 이동 가능한지 확인
		int result=0;
		for(int i=0;i<8;i++) {
			//이동하고자 하는 위치 확인
			int nextRow = row + dx[i];
			int nextColumn = column + dy[i];
			
			//해당위치로 이동이 가능하면 카운트 증가
			if(nextRow >=1 && nextRow <=8 && nextColumn >=1 && nextColumn<=8) {
				result+=1;
			}
		}
		printf("%d", result);
	}

