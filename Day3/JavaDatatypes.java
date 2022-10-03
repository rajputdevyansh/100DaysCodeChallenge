import java.util.Scanner;

public class JavaDatatypes {
    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=0;i<n;i++)
        {
                   try
                   {
                   long n1=sc.nextLong();
                   System.out.println(n1+" can be fitted in:");
                   if(n1>=-128 && n1<=127)
                   {
                       System.out.println("* byte");
                   }
                   if(n1>=-32768 && n1<=32767)
                   {
                       System.out.println("* short");
                   }
                   if(n1>=-2147483648 && n1<=2147483647)
                   {
                       System.out.println("* int");
                   }
                   if(n1>=-9223372036854775808L && n1<=9223372036854775807L)
                   {
                       System.out.println("* long");
                   }
                   }
                   catch(Exception e)
                   {
                       System.out.println(sc.next()+" can't be fitted anywhere.");
                   }
        }
        
    }
}

