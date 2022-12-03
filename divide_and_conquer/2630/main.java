import java.util.Scanner;

public class Main {
	
	public static int white = 0;
	public static int blue = 0;	
	public static int[][] arr;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		arr = new int[n][n];
		
		for(int i =0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		check(0, 0, n);
		
		System.out.println(white);
		System.out.println(blue);
		
	}
	
	
	static void check(int a, int b, int num) {		
		
		if(same(a, b, num)) {
			if(arr[a][b] == 0) {
				white++;
			}else {
				blue++;
			}
			return;
		}
		
		int newnum = num / 2;
		
		check(a, b, newnum);
		check(a + newnum, b, newnum);
		check(a, b + newnum, newnum);
		check(a + newnum, b + newnum, newnum);
}
	
	static Boolean same(int a, int b, int num) {
		int c = arr[a][b]; 
		for(int i = a; i < a + num; i++) {
			for(int j = b; j < b + num; j++) {
				if(c != arr[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
	
}