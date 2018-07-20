

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class findsmallno
{
	public static void main (String[] args) throws java.lang.Exception
	{
		try{
	Scanner s=new Scanner(System.in);
	int count=1;
        long y=s.nextLong();
	 List<Long> q = new ArrayList();
	while(y>0){
		count++;
		q.add(y%10);
		y=y/10;
		}
	 int k=s.nextInt();
	 k=count-1-k;
               int j=k;
               long sum1=0,sum2=0;
   for(int h=count-j;h>=0;h--){
                       sum1=0;
                       
     j=k-1;
     try{
     	
     while(j>=0){
         //System.out.print("h "+h+"j "+j+" "+q.get(h+j)+"\t");
       sum1=sum1*10+(long)q.get(h+j);
       j--;

     }
     }
     catch(Exception e){
      
      ///	System.out.println(e);
     }

     if(sum2==0){
       sum2=sum1;
     }
     
     if(sum1<sum2){
       sum2=sum1;
     }
   
   }

   System.out.printf(""+sum2);
 }
catch(InputMismatchException ex){
	System.out.println("enter integer");
}		
	}
	}
