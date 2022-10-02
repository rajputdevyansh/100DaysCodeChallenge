import java.util.Scanner;

public class IncomeTC {
    public static void main(String[] args) {
        int i;
        double tax;

        Scanner Sc= new Scanner(System.in);
        System.out.println("Enter your Income");
        i=Sc.nextInt();
        if(i<=500000)
        {
            System.out.println("Tax is 0");
        }
        else if(i<=1000000)
        {
            tax=i*0.2;
            System.out.println("Tax is 20%:- "+tax );
        }
        else
        {
            tax=i*0.3;
            System.out.println("Tax is 30%:- "+tax);
        }
    }
}
