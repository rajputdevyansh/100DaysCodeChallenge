/* 
 * Program to Create Outer Class Bank Account and the Inner Class Interest in it
*/
package Basic;
class BankAcct 
{
    int principal = 2000, rate = 6, time = 3;
    void test() 
    {
        Interest inner_obj = new Interest();
        inner_obj.display();
    }
    class Interest 
    {
        void display() 
        {
            int si = (principal * rate * time) / 100;
            System.out.println("Interest : " + si + " Rs");
        }
    }
}
public class Bank 
{
    public static void main(String args[]) 
    {
        BankAcct outer_obj = new BankAcct();
        outer_obj.test();
    }
}
/*
 Interest : 360 Rs
 */
