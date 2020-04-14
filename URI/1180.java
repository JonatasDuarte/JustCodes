import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int n1 = x.nextInt();
		int[] lista = new int[n1];
		for (int i = 0; i < n1; i++) {
			int a = x.nextInt();
			lista[i] = a;
		}
		int k = lista[0];
		int j = 0;
		for (int i = 1; i < n1; i++) {
			int a = lista[i];
			if (a < k) {
				k = a;
				j = i;
			}
		}
		System.out.println("Menor valor: " + k);
		System.out.println("Posicao: " + j);
	}
}
