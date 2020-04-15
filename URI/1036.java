import java.util.Scanner;
import java.lang.Math;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		double A = x.nextDouble();
		double B = x.nextDouble();
		double C = x.nextDouble();
		double Delta = (B * B) - 4 * A * C;
		if (A == 0 || Delta < 0) {
			System.out.println("Impossivel calcular");
		} else {
			double x1 = (-B + Math.sqrt(Delta))/ (2 * A);
			double x2 = (-B - Math.sqrt(Delta))/ (2 * A);
			System.out.printf("R1 = %.5f\n", x1);
			System.out.printf("R2 = %.5f\n", x2);
		}
	}
}