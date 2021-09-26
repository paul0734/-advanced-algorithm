package 고급알고리즘;

import java.util.Arrays;

public class Array0 {

	public static void main(String[] args) {
		int[] arr = {6,0,8,2,3,0,4,0,1};
		reorder(arr);
		System.out.println(Arrays.toString(arr));

	}

	public static void reorder(int[] arr) {
		int j=0;
		for(int item : arr) {
			if(item != 0) {
				arr[j] = item;
				j++;
			}
		}
		for(int i=j; i<arr.length; i++) {
			arr[i] = 0;
		}
	}
}
