/*
Write a program that takes a set of names of individuals and abbreviates the first, middle and other names except the last name by their first letter.
*/
import java.util.Scanner;

public class Exp19 
{
        static void name(){
          Scanner sc = new Scanner(System.in);
          System.out.println("Enter your full Name ");
          String name = sc.nextLine();      
          int i = 0;
          String print = "";
          int count = 1;
          while (i < name.length()) {
            char ch = name.charAt(i);
            print = print + ch;
            if (ch == ' ' && count == 1) {
              count++;
              System.out.println("First Name = " + print);
              print = "";
            } else if (ch == ' ' && count == 2) {
              count++;
              System.out.println("Middle Name = " + print);
              print = "";
            }
            i++;
          }
          if (count == 2) {
            System.out.println("Last Name = " + print.charAt(0));
          } else {
            System.out.println("Last Name = " + print.charAt(0));     
          }
        }
        public static void main(String [] args){
          name();
      }
}
