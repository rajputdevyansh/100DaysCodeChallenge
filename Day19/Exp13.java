/*
Write a program that will read a line and count all occurrences of the word „the‟.
*/
import java.util.Scanner;

public class Exp13 
{
    static int OccurrenceOfWord(String str, String find) 
    {
        String brandNewString = str.toLowerCase();
        String search = find.toLowerCase();
        int leng = search.length(); // 3
        int count = 0;
        char ch = search.charAt(0); // t
        int i = 0;
        while (i < brandNewString.length()) {
          // System.out.print(i+" ");
          String compare = "";
          if (brandNewString.charAt(i) == ch) {
            compare = compare + brandNewString.substring(i, i + leng);
            if (compare.equals(search)) {
              count++;
              i = i + leng - 1;
            }
          }
          i++;
        }
        return count;
      }
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        System.out.println("Enter the statement ");
        String st = sc.nextLine();
        System.out.println("Enter the word looking for ");
        String looking_for = sc.next();
    
        sc.close();
    
        System.out.println("The word " + looking_for + " Occurrences is = " + OccurrenceOfWord(st, looking_for));
      }    
}
