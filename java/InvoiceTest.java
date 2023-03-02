package box;

class InvoiceTest{
	public static void main(String args[]) {                                                             
		//creating objects for Invoice class
		Invoice o1 =new Invoice("32589797","cat",17,-35.12);
		Invoice o2 =new Invoice("-3239898","mat",-16,37877687.15);
		Invoice o3 =new Invoice("3","goat",15,-44.6768768178);
		Invoice o4 =new Invoice("-3","apple",14,54.62);
		Invoice o5 =new Invoice("0","map",32,12.00);
		//displaying the objects
	    System.out.println("this is invoice of items :"+o1.getNumber()+"-"+o1.getDescription()+"("+o1.getQuantity()+")"+"Rs"+o1.getPricePerItem());
	    System.out.println("this is invoice of items :"+o2.getNumber()+"-"+o2.getDescription()+"("+o2.getQuantity()+")"+"Rs"+o2.getPricePerItem());
	    System.out.println("this is invoice of items :"+o3.getNumber()+"-"+o3.getDescription()+"("+o3.getQuantity()+")"+"Rs"+o3.getPricePerItem());
	    System.out.println("this is invoice of items :"+o4.getNumber()+"-"+o4.getDescription()+"("+o4.getQuantity()+")"+"Rs"+o4.getPricePerItem());
	    System.out.println("this is invoice of items :"+o5.getNumber()+"-"+o5.getDescription()+"("+o5.getQuantity()+")"+"Rs"+o5.getPricePerItem());
	      	    
	    double ammount=o1.getPricePerItem()+o2.getPricePerItem()+o3.getPricePerItem()+o4.getPricePerItem()+o5.getPricePerItem();
	    System.out.println("totalammount:"+ammount);
	}   
}

