import java.util.Scanner;

public class Exp9 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Height of Student 1:- ");
        int h1=sc.nextInt();
        System.out.print("Enter Height of Student 2:- ");
        int h2=sc.nextInt();
        if(h1>h2)
        {
            System.out.println("Student 1 is taller");
        }
        else
        {
            System.out.println("Student 2 is taller");
        }
    }
    
}
