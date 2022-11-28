/*
 Program to Count Number of Objects Created for Class
 */
package Basic;

public class ObjectC 
{
    static int count=0;
    ObjectC()
    {
        count++;
    }
    public static void main(String[] args) 
    {
        ObjectC obj1 = new ObjectC();
        ObjectC obj2 = new ObjectC();
        ObjectC obj3 = new ObjectC();
        ObjectC obj4 = new ObjectC();
        System.out.println("Number of objects created:"+count);
    }
}
/*
 Number of objects created:4
 */
