/*
Enter any 5 digit number and find the sum of square of all five digits
*/
import java.util.Scanner;

public class Exp2
{
    public static void main(String[] args) 
    {
        int n,n1;
        int sum=0,count=0;
        Scanner sc =  new Scanner(System.in);
        System.out.println("Enter the number:- ");
        n=sc.nextInt();
        while(n>0)
        {
            n1=n%10;
            sum=sum+n1*n1;
            n=n/10;
            count++;
        }
        if(count==5)
        {
        System.out.println("Sum of Square of Digits:- " +sum);
        }
        else
        {
            System.out.println("no count is not 5 digits");
        }   
    }
        
}
