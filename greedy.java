package 고급알고리즘;

import java.util.Scanner;

public class greedy {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	    int n = sc.nextInt();//동전종류
	    int k = sc.nextInt();//계산할 금액
	    int cnt=0;
	    int i;
	    int[] coinTypes = new int[n+1];
	    for(i=1; i<=n; i++){
	    	coinTypes[i] = sc.nextInt();
	    }
	    for(i = n; i > 0; i--){
	        cnt += k/coinTypes[i];
	        k %= coinTypes[i];
	    }
	    System.out.println(cnt);
	    sc.close();
	}

}
