/*
Enter any number and check number is perfect number or not?
*/
import java.util.Scanner;

public class Exp4 
{
    public static void main(String[] args) {
        int n;
        boolean key=false;
        Scanner Sc=new Scanner(System.in);
        System.out.println("Enter Number:- ");
        n=Sc.nextInt();
        for(int i = 2;i<=n/2;i++)
        {
            if(n%i==0)
            {
                key=true;
                break;
            }

        }
        if(!key)
        {
            System.out.println(n+ " is a prime number");
        }
        else
        {
            System.out.println(n+ " is not a prime number");
        }
    
}
}
