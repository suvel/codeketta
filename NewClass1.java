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
    int N=s.nextInt();
   
    if(N<=20){
    System.out.printf(""+rev(N));
    }
    else{
    System.out.printf("enter number not greater than 20");
    }
  }  
}
