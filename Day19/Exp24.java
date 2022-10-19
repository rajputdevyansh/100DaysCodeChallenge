/*
Define a class student with following specifications
members of class student
Registration number integer
Sname Char(20)
Eng, Maths, Science Float
Total Float
Ctotal() Function which calculates total marks
*/
import java.util.Scanner;

public class Exp24 
{
    int regno;
    String Sname;
    float eng,maths,Sci,total;
    Scanner sc=new Scanner(System.in);

    void initial()
    {
        System.out.println("Enter Details");
        System.out.print("Enter Student Name:- ");
        Sname=sc.next();
        System.out.println("Enter Marks");
        System.out.print("English:- ");
        eng=sc.nextFloat();
        System.out.print("Maths:- ");
        maths=sc.nextFloat();
        System.out.print("Science:- ");
        Sci=sc.nextFloat();
    }
    void Ctotal()
    {
        total=eng+maths+Sci;
        System.out.println("\nTotal Marks of Student:- "+total);
    }
    public static void main(String[] args) {
        Exp24 obj = new Exp24();
        obj.initial();
        obj.Ctotal();
    }   
}
