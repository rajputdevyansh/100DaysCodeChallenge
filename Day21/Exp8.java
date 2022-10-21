import java.util.Scanner;

public class Exp8 
{
    public static void main(String[] args) {
		int sum = 0,n;
		Scanner sc=new Scanner(System.in);
        System.out.print("Enter Range:- ");
        n=sc.nextInt();
        for (int i = 1; i <= n; i++) 
        {
			if (i % 5 == 0) 
            {
				System.out.println(i + " ");
				sum += i;
			}
		}
		System.out.println("Sum:- "+sum);
	}
}
