/*
Define a class batsman in cricket team. Include the following members:
First name, Last name, Runs made, Number of fours, Number of Six
Member function:
(i) To assign initial value
(ii) To update runs made
(iii) To display batsman’s information
*/
import java.util.Scanner;

public class Exp23 
{
    int Runs,n4,n6;
    String Fname,Lname;
    Scanner sc = new Scanner(System.in);
    void initial()
    {
        System.out.print("Enter First Name:- ");
        Fname=sc.next();
        System.out.print("Enter Last Name:- ");
        Lname=sc.next();
        System.out.print("Enter Runs Made:- ");
        Runs=sc.nextInt();
        System.out.print("Enter No of 4s:- ");
        n4=sc.nextInt();
        System.out.print("Enter No of 6s:- ");
        n6=sc.nextInt(); 
    }
    void update_runs()
    {
        System.out.print("\nEnter Updated runs:- ");
        this.Runs=sc.nextInt();
        System.out.print("Updated No of 4s:- ");
        this.n4=sc.nextInt();
        System.out.print("Updated No of 6s:- ");
        this.n6=sc.nextInt();
    }
    void info()
    {
        System.out.println("\nFirst Name:- "+Fname);
        System.out.println("Last Name:- "+Lname);
        System.out.println("Runs:- "+Runs);
        System.out.println("No of 4s:- "+n4);
        System.out.println("No of 6s:- "+n6);
    }
    public static void main(String[] args) 
    {
        Exp23 obj = new Exp23();
        obj.initial();
        obj.update_runs();
        obj.info();
    }
}
