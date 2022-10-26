import java.util.Scanner;
class Prime{
	public static void main(String args[]){
		Scanner sc = Scanner(System.in);
		int x = sc.nextInt();
		int arr[],k=0;
		for(int i=0;i<=x;i++){
			if(x%i==0){
					arr[i]=sc.nextInt();
		}
		System.out.println(arr[i]);			
	}			
}