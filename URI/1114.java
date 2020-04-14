import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x =  new Scanner(System.in);
		int n = 0;
		while(n == 0){
			int s = x.nextInt();
			if(s == 2002){
				System.out.println("Acesso Permitido");
				n = 1;
			} else{
				System.out.println("Senha Invalida");
			}
			
		}
	}
	

}