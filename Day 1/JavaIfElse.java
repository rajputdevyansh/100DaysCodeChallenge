/* In this challenge, we test your knowledge of using if-else conditional statements to automate decision-making processes. An if-else statement has the following logical flow:

Wikipedia if-else flow chart

Source: Wikipedia

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.
*/
import java.util.Scanner;

public class JavaIfElse 
{
    public static void main(String[] args) 
    {
        Scanner Sc=new Scanner(System.in);
        int n=Sc.nextInt();
        if(n%2==0 && 2<=n && n<=5)
        {
            System.out.println("Not Weird");
        }
        else if(n%2==0 && 6<=n && n<=20)
        {
            System.out.println("Weird");
        }
        else if(n%2==0 && n>20)
        {
            System.out.println("Not Weird");
        }
        else
        {
            System.out.println("Weird");
        }
        
    }
    
}
