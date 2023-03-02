package box;

public class Invoice {
	//declaring instance variables
    String number;
    String description;
    int quantity;
    double priceperitem;
    //constructor initializing all instance variables
    Invoice(String n,String dis,int qty,double ppi){  
    	number=n;
    	description=dis;
    	quantity=qty;
        priceperitem=ppi;
    }
    //using set methods for all instance variables
    void setNumber(String n) {
    	number=n;
    }
    void setDescription(String dis) {
        description=dis;
    }
    void setQuantity(int qty) {                                                                                                                                                                
    	quantity=qty;	
        if(qty<0) {
        	qty=0;
        }
    }   
    void setPricePerItem(double ppi ) {
    	priceperitem=ppi;
      if(ppi<0) {
    	  ppi=0.0;
      }
    }
    //now get methods for instance varibles
    String getNumber() {
    	return number;
    }
    String getDescription() {
    	return description;
    }
    int getQuantity() {
    	return quantity;
    }
    double getPricePerItem() {
    	return priceperitem;	
    }
    //getting total amount
    double InvoiceAmmount() {
    	return quantity*priceperitem;
    	
    }

}

    
