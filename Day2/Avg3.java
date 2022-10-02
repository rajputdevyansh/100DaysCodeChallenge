import java.util.Scanner;

public class Avg3 {
    public static void main(String[] args) {
        int a,b,c,avg,sum;
        Scanner Sc=new Scanner(System.in);
        System.out.println("Enter Numbers");
        a=Sc.nextInt();
        b=Sc.nextInt();
        c=Sc.nextInt();
        sum=a+b+c;
        avg=sum/3;
        System.out.println(avg);
    }
}
