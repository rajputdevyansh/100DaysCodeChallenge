// String Constructor Program in Java
package Basic;
class String_Initialise
{
    String a, b;
    public String_Initialise()
    {
        System.out.println("Base Class Constructor");
        a = "String from Base Class";
    }
}
public class StringCon extends String_Initialise
{
   public StringCon()
    {
        System.out.println("Derived Class Constructor");
        b = "String from Derived Class";
    }
    public static void main(String... arg) 
    {
        StringCon obj = new StringCon();
        System.out.println("the strings initialised in the constructors of Base and Derived classes are :");
        System.out.println(obj.a +" and "+obj.b);
    }
}
/*
Base Class Constructor
Derived Class Constructor
the strings initialised in the constructors of Base and Derived classes are :
String from Base Class and String from Derived Class
 */
