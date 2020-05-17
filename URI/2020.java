import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cont = 0;
		String textos = "";
		while (sc.hasNext()) {
			ArrayList<String> palavras = new ArrayList<>();
			cont++;
			if (cont == 1) {
				textos += "LISTA #1:\n";
			} else {
				textos += "\n\nLISTA #" + cont + ":\n";
			}
			int rep = sc.nextInt();
			sc.nextLine();
			ArrayList<String> letras = new ArrayList<>();
			ArrayList<Integer> gnomos = new ArrayList<>();
			for (int j = 1; j < 27; j++) {
				gnomos.add(j);
			}
			;
			String[] letters = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
					"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
			for (String letra : letters) {
				letras.add(letra);
			}
			for (int i = 0; i < rep; i++) {
				String palavra = "";
				String linha = sc.nextLine();
				String[] quebr = linha.split(" ");
				for (String letra : quebr) {
					if (letra.equals("27")) {
						palavra += " ";
					} else {
						int indi = gnomos.get(Integer.parseInt(letra) - 1);
						gnomos.remove(Integer.parseInt(letra) - 1);
						gnomos.add(indi);
						palavra += letras.get(indi - 1);
						String letr = letras.remove(indi - 1);
						letras.add(letr);
					}
				}
				
				palavras.add(palavra);
				
			}
			palavras.sort(null);
			for (int i = 0; i < palavras.size(); i++) {
				if(i == 0) {
					textos += palavras.get(i);
				} else {
					textos += "\n" + palavras.get(i);
				}
				
			}
		}
		System.out.println(textos);

	}
}
