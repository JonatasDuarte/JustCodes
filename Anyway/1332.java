import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int tri = x.nextInt();
		char[] one = {'o', 'n', 'e'};
		char[] two = {'t', 'w', 'o'};
		for(int i = 0; i < tri; i++){
			String tru = x.next();
			char[] ca = tru.toCharArray();
			if(ca.length == 5){
				System.out.println("3");
			} else{
				int cont = 0;
				for(int j = 0; j < ca.length; j++){
					if(ca[j] != one[j] ){
						cont ++;
					}
				}
				if(cont <= 1){
					System.out.println("1");
				} else {
					cont = 0;
					for(int j = 0; j < ca.length; j++){
						if(ca[j] != two[j] ){
							cont ++;
						}
					}
					if(cont <= 1){
						System.out.println("2");
					}
					

				}
			}
				
			
		}
			
	}

}
