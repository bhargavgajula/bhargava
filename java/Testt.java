import java.lang.*;
class Testt{
	int a;
	int b;
	Testt(int i,int j){
			i=a;
			j=b;
	}
	int Value(Testt o){
		if(o.a*o.b<100){
			return -1;
		}
		else{
			return 1;
		}
	}
}

class Suma{
	public static void main(String args[]){
		Testt ob1 = new Testt(20,5);
		Testt ob2 = new Testt(24,3);
		System.out.println("the product is"+ob1.Value(ob1));
	}
}		


				