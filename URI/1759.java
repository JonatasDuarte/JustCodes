import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int Ho = x.nextInt();
		for (int i = 0; i < Ho; i++) {
			System.out.print("Ho");
			if (i != Ho-1) {
				System.out.print(" ");
			}
		}
		System.out.println("!");
	}
}
