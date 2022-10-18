/*
Enter any string and check entered string is palindrome or not?
*/
import java.util.Scanner;

public class Exp11 
{
    static boolean isPalindrom(String str){
        int w = 0;
        int a = str.length() - 1;
     
        while (w <= a) 
        {
          if (str.charAt(w) != str.charAt(a)) {
               return false;
          }
          w++;
          a--;
         }
         return true;
        }
       public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
      
         System.out.println("Enter any string ");
          String name= sc.nextLine();
     
          if(isPalindrom(name)){
            System.out.println("String is Palindrome ");
          }else{
            System.out.println("String is not Palindrome ");
          }
       }   
}
