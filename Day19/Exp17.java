/*
Write a program to delete all vowels from a sentence.
*/
import java.util.Scanner;

public class Exp17 
{
    static void delete_Vowels() {
        Scanner sc = new Scanner(System.in);
       String brandNewString = "";
        System.out.println("Enter the Statement:- ");
        String str = sc.nextLine();
        int i=0; 
        while(i<str.length()){
          char ch = str.charAt(i);
          if (!(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')) {
            brandNewString = brandNewString + ch;
          }
          i++;
        }
        System.out.println(brandNewString);
      }
      public static void main(String[] args) 
      {
        delete_Vowels();
      }
}
