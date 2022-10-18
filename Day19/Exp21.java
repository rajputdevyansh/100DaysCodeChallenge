/*
Write a Program in JAVA that returns the sum of multiples of 3 and 5 between 0 and
limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12,
15, 18, 20.
*/
import java.util.Scanner;

public class Exp21
{
    static int limit(int N)
    {
        int sum1 = 0;
        for (int i = 0; i <= N; i++)
            if (i % 3 == 0 || i % 5 == 0)
                sum1 += i;
        return sum1;
    }
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Limit:- ");
        int n=sc.nextInt();
        System.out.println("Sum:- "+limit(n));
    }
}
