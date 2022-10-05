/*
Problem:- to delete the occurance of an word form an statement 

Sample Input/Output:-
Enter the statement ...
Hello how do you do Hello are you fine Hello its good to see you  
Enter the word you want to delete ...
Hello
 how do you do  are you fine  its good to see you 

*/
import java.util.Scanner;

public class DelOccurrence {
    static void deleteOccurrence(String str, String delete) {
        String brandNewString = str.toLowerCase();
        String search = delete.toLowerCase();
        String ResultString = "";
    
    
        int len = search.length(); // 3
        char ch = search.charAt(0); // t
    
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
        System.out.println("Enter the statement ... ");
        String str = sc.nextLine();
        System.out.println("Enter the word you want to delete ...");
        String delete = sc.next();
    
        deleteOccurrence(str, delete);
    
      }
}
