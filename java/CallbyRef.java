class GB{
    int a,b;
    GB(int i ,int j){
        a=i;
        b=j;
    }
    void val(GB ob){
        ob.i*=3;
        ob.j/=3;
    }
}
public  class CalbyRef{
    public static void main(String[] args) {    
        int a=15;
        int b=30;
        GB ob= new GB();
        System.out.println("values of a and b"+ob.a+" "+ob.b);
        ob.val(a,b);
        System.out.println("values of a and b after"+ob.a+" "+ob.b);
    }        
}