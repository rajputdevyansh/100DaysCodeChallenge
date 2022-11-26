/*
Program to Illustrates Use of Abstract Class and Method
*/package Basic;

import java.util.Scanner;

abstract class Calculation
{
    Scanner sc = new Scanner(System.in);
    float a = sc.nextFloat();
    float b = sc.nextFloat();
    float c;
    abstract void add();
    void subtract()
    {
        c = a - b;
        System.out.println("Result:"+c);
    }
    abstract void multiply();
    void divide()
    {
        c = a / b;
        System.out.println("Result:"+c);
    }
}
public class ab extends Calculation
{
    void add()
    {
        c = a + b;
        System.out.println("Result:"+c);
    }
    void multiply()
    {
        c = a * b;
        System.out.println("Result:"+c);
    }
    public static void main(String[] args)
    {
        System.out.println("Enter Numbers");
        ab obj = new ab();
        obj.add();
        obj.subtract();
        obj.multiply();
        obj.divide();
    }
}
/*
Enter Numbers
14
15
Result:29.0
Result:-1.0
Result:210.0
Result:0.93333334
 */
