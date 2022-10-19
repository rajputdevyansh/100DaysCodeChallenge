/*
Define a class employee with the following specifications;
Private members of class employee :
empno integer
ename String
basic,hra,da float
netpay float
calculate( ) A method to calculate basic + hra + da with float return type
Public member functions of class employee :
havedata( ) method to accept values for empno, sname, basic , hra ,da and
invoke
calculate( ) to calculate netpay
dispdata( ) function to display all the data members on the screen
*/
import java.util.Scanner;

class Exp26 
{
    private int empno;
    private float basic,hra,da,netpay;
    private String ename;
    Scanner sc = new Scanner(System.in);

    public void havedata()
    {
        System.out.println("Enter Details");
        System.out.print("Enter Employee name:- ");
        ename=sc.next();
        System.out.print("Enter Empno:- ");
        empno=sc.nextInt();
        System.out.print("Enter Basic Salary:- ");
        basic=sc.nextFloat();
        System.out.print("Enter HRA:- ");
        hra=sc.nextFloat();
        System.out.print("Enter DA:- ");
        da=sc.nextFloat();
    }
    private float calculate()
    {
        netpay=basic+hra+da;
        return netpay;
    }
    public void dispdata()
    {
        System.out.println("\nEmployee No:- "+empno);
        System.out.println("Employee Name:- "+ename);
        System.out.println("Basic Salary:- "+basic);
        System.out.println("HRA:- "+hra);
        System.out.println("DA:- "+da);
        System.out.println("\nTotal Netpay:- "+calculate());
    }
    public static void main(String[] args) {
        Exp26 obj = new Exp26();
        obj.havedata();
        obj.dispdata();
    }
}
