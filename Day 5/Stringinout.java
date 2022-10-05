import java.util.Scanner;

public class Stringinout {
    public static void main(String[] args) {
        System.out.println("Enter your name");
        Scanner sc= new Scanner(System.in);
        String A=sc.nextLine();
        System.out.println("Enter your age");
        int n=sc.nextInt();
        System.out.println("Entered Name:- "+A);
        System.out.println("Entered Age:- "+n);
    }
    
}
