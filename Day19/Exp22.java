/*
Define a class which represent a book in library. Include following members as data
members
Book number, book name, author, publisher, price, No. of copies issued
Member function
(i) To assign initial value
(ii) To issue a book after checking its availability
(iii) To return a book
(iv) To display book information
*/
import java.util.Scanner;

public class Exp22 
{
    int Bookno,NOCI;
    float price;
    String Bname,Author,Publisher;
    Scanner sc = new Scanner(System.in);
    void initial()
    {
        System.out.print("Enter Book No:- ");
        Bookno=sc.nextInt();
        System.out.print("Enter Book Name:- ");
        Bname=sc.next();
        System.out.print("Enter Author Name:- ");
        Author=sc.next();
        System.out.print("Enter Publisher Name:- ");
        Publisher=sc.next();
        System.out.print("Enter Price:- ");
        price=sc.nextFloat();
        System.out.print("Enter No. of copies issued:- ");
        NOCI=sc.nextInt();
    }
    void issue(int Bookno, String Bname)
    {
        if((Bookno == this.Bookno) && (Bname.equals(this.Bname)))
        {
            System.out.println("Book Issued Successfully");
        }
        else
        {
            System.out.println("Book, Not Avaliable");
        }
    }
    void return_book(int Bookno, String Bname)
    {
        if((Bookno == this.Bookno) && (Bname.equals(this.Bname)))
        {
            System.out.println("Book Returned Successfully");
        }
        else
        {
            System.out.println("Book dose not match");
        }
    }
    void bookinfo()
    {
        System.out.println("Book No:- "+Bookno);
        System.out.println("Book Name:- "+Bname);
        System.out.println("Author Name:- "+Author);
        System.out.println("Publisher Name:- "+Publisher);
        System.out.println("Price:- "+price);
        System.out.println("No. of copies issued:- "+NOCI);
    }
    public static void main(String[] args) 
    {
        Exp22 obj = new Exp22();
        obj.initial();
        Scanner sd = new Scanner(System.in);
        System.out.println("\nProvide Data For Issue");
        System.out.print("Enter Book no:- ");
        int b = sd.nextInt();
        System.out.print("Enter Book Name:- ");
        String a = sd.next();
        obj.issue(b,a);
        System.out.println("\nProvide Data For Return");
        System.out.print("Enter Book no:- ");
        int c = sd.nextInt();
        System.out.print("Enter Book Name:- ");
        String d = sd.next();
        obj.return_book(c, d);
        obj.bookinfo();
    }
}
