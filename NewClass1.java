
import java.util.InputMismatchException;
import java.util.Scanner;
public class NewClass1 {
    private static int rev(int  val){
        int sum=1;
        for(int i=val;i>0;i--){
        sum=sum*i;
        }
    return sum;
    }   
  public static void main(String args[]){
      System.out.printf("-->");
    Scanner s=new Scanner(System.in); 
    int N=0;
    try{
     N=s.nextInt();
     if(N>=0&&N<=20){
    System.out.printf(""+rev(N));
    }
    else{
    System.out.printf("enter number between 0 and  20 ");
    }
    }
    catch(InputMismatchException e){
    System.out.printf("enter a integer-4");
    NewClass1.main(args);
    }
    
  }  
}
