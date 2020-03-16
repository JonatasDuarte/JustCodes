import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String linha;
		while ((linha = br.readLine()) != null) {
			if (linha.length() >= 6 && linha.length() <= 32 && ehValida(linha) && haMaiuscula(linha) && haNumero(linha)
					&& haMinuscula(linha) && !haEspaco(linha)) {
				System.out.println("Senha valida.");
			} else {
				System.out.println("Senha invalida.");
			}
		}
	}

	public static boolean ehValida(String frase) {
		for (int i = 0; i < frase.length(); i++) {
			int l = (int) frase.charAt(i);
			// System.out.println(l);
			if ((l > 0 && l < 48) || (l > 57 && l < 65) || (l > 90 && l < 97) || l > 123) {
				return false;
			}
		}
		return true;
	}

	public static boolean haMaiuscula(String frase) {
		for (int i = 0; i < frase.length(); i++) {
			int l = (int) frase.charAt(i);
			if (l >= 65 && l <= 90) {
				return true;
			}
		}
		return false;
	}

	public static boolean haNumero(String frase) {
		for (int i = 0; i < frase.length(); i++) {
			int l = (int) frase.charAt(i);
			if (l >= 48 && l <= 57) {
				return true;
			}
		}
		return false;
	}

	public static boolean haEspaco(String frase) {
		for (int i = 0; i < frase.length(); i++) {
			if (frase.charAt(i) == ' ') {
				return true;
			}
		}
		return false;
	}

	public static boolean haMinuscula(String frase) {
		for (int i = 0; i < frase.length(); i++) {
			int l = (int) frase.charAt(i);
			if (l >= 97 && l <= 122) {
				return true;
			}
		}
		return false;
	}
}