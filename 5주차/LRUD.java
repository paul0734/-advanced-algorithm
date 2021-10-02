package 고급알고리즘;

import java.util.*; 
public class LRUD { 
	public static void main(String[] args) 
	{ 
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		String[] plans = sc.nextLine().split(" ");
		//nextLine() 문자열 한줄을 통으로 입력받음
		//split() ()안의 문자를 기준으로 문자열을 나눔
		//System.out.println(Arrays.toString(plans));
		
		int x = 1, y = 1;
		int[] dx = {0, 0, -1, 1}; 
		int[] dy = {-1, 1, 0, 0}; 
		char[] moveTypes = {'L', 'R', 'U', 'D'};
		
		for (int i = 0; i < plans.length; i++) { 
			char plan = plans[i].charAt(0);
			//charAt(i)는 String타입의 문자열에서 i번째의 글자를 char타입으로 뽑아온다
			int nx = -1, ny = -1; 
			for (int j = 0; j < 4; j++) {
				if (plan == moveTypes[j]) {
					nx = x + dx[j]; 
					ny = y + dy[j]; 
				} 
			}
			if (nx < 1 || ny < 1 || nx > n || ny > n) continue;// 공간을 벗어나는 경우 무시  
			x = nx; 
			y = ny; 
			}
		System.out.println(x + " " + y); 
	} 
}

	


