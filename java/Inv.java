public class Invoice1 {
	String partNumber;
	String Description;
	int quantity;
	double price;	
	Invoice(String pNum, String des, int qty, double pri) {
		partNumber = pNum;
		partDescription = desc;
		quantity = qty;
		price = prc;
	}
	public String getPartNumber() {
		return partNumber;
	}
	public String getPartDesc() {
		return partDescription;
	}
	public int getQuantity() {
		return quantity;
	}
	public double getPrice() {
		return price;
	}
	public void setPartNumber(String pNum) {
		partNumber = pNum;
	}
	public void setPartDesc(String desc) {
		Description = desc;
	
	public void setQuantity(int qty) {
		if (qty < 0) {
			qty = 0;
		} else {
			quantity = qty;
		}
	}
	public void setPrice(double prc) {
		if (prc < 0.0) {
			price = 0.0;
		} else {
			price = pri;
		}
	}
	public double getInvoiceAmount() {
		return (double) quantity * price;
	