class Magic{
    public static void main(String[] args) {
        int arr[]={20,25,15,10,5,50};
        int nb=arr.length;
        int count=0;
        for (int i : arr) {
            count=0;
            for (int j : arr) {
                if(arr[i]%arr[j]==0){
                   
                    count++;
                }
                if(count==nb){
                    System.out.println(arr[j]);

                }    
                
                

            }
                
        }
            
    }
}
 