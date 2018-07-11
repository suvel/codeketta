/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
	Scanner s=new Scanner(System.in);
	int count=1,y=s.nextInt();
	 List q = new ArrayList();
	while(y>0){
		count++;
		q.add(y%10);
		y=y/10;
		
	}
	 int k=s.nextInt();
               int j=k,sum1=0,sum2=0;
   for(int h=count-j+1;h>=0;h--){
                       sum1=0;
     j=k-1;
     try{
     while(j>=0){
       sum1=sum1*10+(int)q.get(h+j);
       j--;
     }
     }
     catch(Exception e){
      //System.out.println(""+e);
     }

     if(sum2==0){
       sum2=sum1;
     }
     
     if(sum1<sum2){
       sum2=sum1;
     }
   
   }

   System.out.printf("--->"+sum2);
 }
	}
