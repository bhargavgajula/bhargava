import java.lang.*;
class Test{
	int a b;
	Test(inti int j){
		a=i;
		b=j;
		boolean equalTo(Test o){
			if(o.a=a && o.b=b) return true;
			else return false;
		}
}


class PassOb{
	public staic void main(String args[]){
		Test ob1 = new Test(10,20);
		Test ob2 = new Test(10,20);
		Test ob2 = new Test(10,20);
		System.out.println("ob1==0b2"+ ob1.equalsTo(ob2));
		System.out.println("ob1==0b3"+ ob1.equalsTo(ob3));
	}
}