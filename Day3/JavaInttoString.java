import java.util.Scanner;

public class JavaInttoString {
    public static void main(String[] args) 
    {
      Scanner sc=new Scanner(System.in);
      int n=sc.nextInt();
      String s;
      if(n>=-100 && n<=100)
      {
        s=Integer.toString(n);  
        System.out.println("Good job");
      }
      else
      {
          System.out.println("Wrong answer");
      } 
    }
}
