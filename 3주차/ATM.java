package 고급알고리즘;

import java.util.Arrays;
import java.util.Scanner;

public class ATM {

	public static void main(String[] args) {
		Scanner sc  = new Scanner(System.in);
		int sum=0;
		int prev=0;
		int n = sc.nextInt();
		int arr[] = new int[n];
		for(int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);
		
		for(int i=0; i<n; i++) {
			sum += prev + arr[i];
			prev += arr[i];
		}
		System.out.println(sum);
	}

}
