import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int as = x.nextInt();
		for (int i = 0; i < as+1; i ++){
			String num = x.nextLine();
			char[] numQ = num.toCharArray();
			int cont = 0;
			for (char k: numQ){
				switch(k){
				case 48:
					cont += 6;
					break;
				case 49:
					cont += 2;
					break;
				case 50:
					cont += 5;
					break;
				case 51:
					cont += 5;
					break;
				case 52:
					cont += 4;
					break;
				case 53:
					cont += 5;
					break;
				case 54:
					cont += 6;
					break;
				case 55:
					cont += 3;
					break;
				case 56:
					cont += 7;
					break;
				case 57:
					cont += 6;
					break;
				}
			}
			if(cont != 0){
			System.out.println(cont + " leds");
			}
		}
	}

}