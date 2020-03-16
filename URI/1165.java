import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int k = x.nextInt();
		for (int i = 0; i < k; i++) {
			int d = 0;
			int j = x.nextInt();
			for (int p = 1; p < j + 1; p++) {
				if (j % p == 0) {
					d ++;
				}
			}
			if (d > 2) {
				System.out.println(j + " nao eh primo");
			} else {
				System.out.println(j + " eh primo");
			}
		}

	}
}
