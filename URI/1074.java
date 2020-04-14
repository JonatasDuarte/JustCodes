import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int n = x.nextInt();
		for (int i = 0; i < n; i++){
			int j = x.nextInt();
			if(j == 0){
				System.out.println("NULL");
			} else if(j % 2 == 0){
				if(j > 0){
					System.out.println("EVEN POSITIVE");
					
				}else{
					System.out.println("EVEN NEGATIVE");
				}
			} else{
				if(j > 0){
					System.out.println("ODD POSITIVE");
					
				}else{
					System.out.println("ODD NEGATIVE");
				}
				
			}
		
		}
		
	}

}
