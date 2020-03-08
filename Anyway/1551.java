import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int n = x.nextInt();
		x.nextLine();
		for (int k = 0; k < n; k++) {
			String gad = x.nextLine();
			int cont = 0;
			for (int i = 97; i <= 122; i++) {
				if(gad.indexOf(i) != -1) {
					cont++;
				}
			}
			if (cont == 26) {
				System.out.println("frase completa");
			} else if (cont >= 13) {
				System.out.println("frase quase completa");
			} else if (cont > 0) {
				System.out.println("frase mal elaborada");
			}
		}
	}
}