/*
Write a program that will read a line and delete from it all occurrences of the word „the‟.
*/
import java.util.Scanner;

public class Exp18 
{
    static void deleteOccurrence(String str, String delete) {
        String brandNewString = str.toLowerCase();
        String search = delete.toLowerCase();
        String ResultString = "";
        int len = search.length();
        char ch = search.charAt(0);
    
        int i = 0;
        while (i < brandNewString.length()) {
    
          String compare = "";
          char c = brandNewString.charAt(i);
          if ((c == ch) && (i + len) < brandNewString.length()) {
            compare = compare + brandNewString.substring(i, i + len);
    
            if (compare.equals(search)) {
              i = i + len;
              continue;
            } else {
              ResultString = ResultString + c;
            }
          } else {
            ResultString = ResultString + c;
          }
          i++;
        }
        System.out.println(ResultString);
      }
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the statement:- ");
        String str = sc.nextLine();
        System.out.println("Enter the word you want to delete:- ");
        String delete = sc.next();
        deleteOccurrence(str, delete);
      }
    
}
