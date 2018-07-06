import java.util.HashMap;
import java.util.Scanner;

/**
 *
 * @author suvel
 */
public class romentodec2 {
     private static int romtodec(String val){
      int len=val.length(),sum=0,op1=0,op2=0;
    HashMap<Character,Integer> hm=new HashMap<>();
    hm.put('I',1);
    hm.put('V',5);
    hm.put('X',10);
    
    for(int i=len-1;i>=0;i--){
    op1=hm.get(val.charAt(i));
    if(sum==0){ 
      sum=sum+op1;
      
      }
      else{
      if(op2<=op1){
       sum=sum+op1;
      }
      else{
      sum=sum-op1;
      }
      }
      op2=op1;
      if(sum>20){
          sum=0;
          break;
      }
    }
    
        return sum;
    }
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        String userval=null;
        userval=s.next();
        int i=romtodec(userval.toUpperCase());
        if(i==0){
        System.out.printf("enter number between 0 to 20");
        }
        else{
           System.out.printf(""+i);   
        }
        
    }
}
