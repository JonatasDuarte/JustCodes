import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int j = 0;
		int p = 0;
		for(int i = 0; i < 100; i++){
			int h = x.nextInt();
			if(h > j){
				j = h;
				p = i + 1;
			}
			
		}
		System.out.println(j);
		System.out.println(p);
	}
}
