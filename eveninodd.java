
import java.util.Scanner;

class eveninodd {
   
    public static void main(String args[]){
        try{
        int N,y;
        Scanner s=new Scanner(System.in);
        N=s.nextInt();
        int A[]=new int[N];
        for(int j=0;j<N;j++){
        A[j]=s.nextInt();
        }
        String h="";
        for(y=0;y<N;y++){
            //System.out.println("top "+y);
        if(A[y]%2!=0 && y%2==0){
        h=h+(" "+A[y]);
        }
         //System.out.println("b4 "+y);
         //System.out.println("at "+y);
        if(A[y]%2==0 && y%2!=0){
        h=h+(" "+A[y]);
        }
        }
        System.out.println(h.trim());
        
        
    }
         catch(Exception e){
           System.out.println(e);
}
    }
  
}
