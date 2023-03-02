public class Magic
{
	public static void main(String args[])
	{	 	

		int nb=6;
  		int arr[]={25,5,15,20,10,50};
		int count=0;
  		for(int i=0; i<nb; i++)
		{
    		count=0;
			for(int j=0; j<nb; j++)
			{
      			if(arr[i]%arr[j]!=0)
					break;
				else
        			count=count+1;
  				if(count==nb)
				{
    				System.out.println(arr[j]);
				}
				else{
					System.out.println("-1");
				}
			}
		}
	}
}