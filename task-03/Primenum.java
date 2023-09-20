import java.util.Scanner;

public class Prime {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("n= ");
		int n= scanner.nextInt();
		
		for (int a = 2; a < n; a++) {
			int k=0;
			for (int i = 2 ; i< a/2; i++) {
				if (a%i == 0) {
					k++;
				}
			if (k==0) {
				System.out.println(a);
			}
		}
	}
}
