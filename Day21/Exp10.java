import java.util.Scanner;

public class Exp10 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Marks of Student 1");
        System.out.println("Subject 1");
        int s1=sc.nextInt();
        System.out.println("Subject 2");
        int s2=sc.nextInt();
        System.out.println("Subject 3");
        int s3=sc.nextInt();
        System.out.println("Subject 4");
        int s4=sc.nextInt();
        System.out.println("Subject 5");
        int s5=sc.nextInt();
        System.out.println("Enter Marks of Student 2");
        System.out.println("Subject 1");
        int s6=sc.nextInt();
        System.out.println("Subject 2");
        int s7=sc.nextInt();
        System.out.println("Subject 3");
        int s8=sc.nextInt();
        System.out.println("Subject 4");
        int s9=sc.nextInt();
        System.out.println("Subject 5");
        int s10=sc.nextInt();
        System.out.println("Enter Marks of Student 2");
        System.out.println("Subject 1");
        int s11=sc.nextInt();
        System.out.println("Subject 2");
        int s12=sc.nextInt();
        System.out.println("Subject 3");
        int s13=sc.nextInt();
        System.out.println("Subject 4");
        int s14=sc.nextInt();
        System.out.println("Subject 5");
        int s15=sc.nextInt();
        int sum1=s1+s2+s3+s4+s5;
        int sum2=s6+s7+s8+s9+s10;
        int sum3=s11+s12+s13+s14+s15;
        if(sum1>sum2 && sum1>sum3)
        {
            System.out.println("Marks of Student 1 are highest");
        }
        if(sum2>sum1 && sum2>sum3)
        {
            System.out.println("Marks of Student 2 are highest");
        }
        if(sum3>sum1 && sum3>sum2)
        {
            System.out.println("Marks of Student 3 are highest");
        }
    }
    
}
