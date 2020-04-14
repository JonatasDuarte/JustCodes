import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int m = 0;
		int k = 0;
		double j = 0;
		while(m >= 0) {
			 m = x.nextInt();
			 if (m >= 0) {
				 k += m;
				 j += 1;
			 }
		}
		System.out.printf("%.2f\n", k/j);
		
	}

}