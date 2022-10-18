/*
Write a program to sort a set of names stored in an array in alphabetical order.
*/
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Exp16 
{
    static void String_Sort() {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<String>();
        System.out.println("Enter the length of Array...");
        int n = sc.nextInt();
    
        for (int i = 0; i < n; i++) {
          System.out.println("Enter the " + (i + 1) + " element of array String format = ");
          list.add(sc.next());
        }
        Collections.sort(list);
        System.out.println("sorted element = " + list);
      }
      public static void main(String[] args) {
        String_Sort();
      }
}
