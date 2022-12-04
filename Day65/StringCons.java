class String_Initialise
{
    String a, b;
    public String_Initialise()
    {
        System.out.println("Base Class Constructor");
        a = "String from Base Class";
    }
}
public class String_Initialise1 extends String_Initialise
{
   public String_Initialise1()
    {
        System.out.println("Derived Class Constructor");
        b = "String from Derived Class";
    }
    public static void main(String... arg) 
    {
        String_Initialise1 obj = new String_Initialise1();
        System.out.println("the strings initialised in the constructors of Base and Derived classes are :");
        System.out.println(obj.a +" and "+obj.b);
    }
}
