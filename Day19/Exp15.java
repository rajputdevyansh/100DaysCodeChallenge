/*
Enter any line of text and write a program to reverse each word of entered text.
*/
import java.util.Scanner;

public class Exp15 
{
    static String reverseWord(String str) {

        String brandNewString = "";
        int i = 0, k = 0;
        while (i < str.length()) {
          char ch = str.charAt(i);
          if (ch == ' ') {
            int x = i - 1; // x = 4
            while (x >= k) {
              brandNewString = brandNewString + str.charAt(x);
              x--;
            }
            k = i + 1;
            brandNewString = brandNewString + " ";
          }
          i++;
        }
        int x = str.length() - 1;
        while (x >= k) {
          brandNewString = brandNewString + str.charAt(x);
          x--;
        }
        return brandNewString;
      }
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter any statement:- ");
        String st = sc.nextLine();
        System.out.println("Reverse String = " + reverseWord(st));
      }    
}
