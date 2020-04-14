import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sk = new Scanner(System.in);
		String a = sk.nextLine();
		double b = sk.nextDouble();
		double c = sk.nextDouble();
		double Salario = b + (c*0.15);
		System.out.printf("TOTAL = R$ %.2f\n",Salario);
		}


}
