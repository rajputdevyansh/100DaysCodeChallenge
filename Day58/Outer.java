/*
Program to Illustrates Use of Referencing the Object from Inner Class
 */
public class Outer
{
    static Outer.InnerClass obj;
    void test1()
    {
        System.out.println("Success");
    }
    static public class InnerClass
    {
    	private String name = "Peakit";
        public void test2()
        {
            Outer outer = new Outer();
            outer.test1();
        }
    }
    public static void main(String[] args)
    {
        obj = new Outer.InnerClass();
        obj.test2();
    }
}
/*
 Success
 */
