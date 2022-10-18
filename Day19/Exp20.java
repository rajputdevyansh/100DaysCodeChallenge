/*
Write a program to count the number of occurrences of any two vowels in succession in a line of text. For example, in the sentence
“Pleases read this application and give me gratuity”
such occurrences are ea, ea, ui.
*/
import java.util.ArrayList;
import java.util.Scanner;

public class Exp20 
{
    static void vowelsCount(String str){
        String vowel = "";
       ArrayList<String> S = new ArrayList<String>();
       int i=0; 
       while(i<str.length()-1){
         char ch1 = str.charAt(i);
         char ch2 = str.charAt(i+1);
   
         if((ch1=='a' || ch1=='e' || ch1=='i' || ch1=='o' || ch1=='u' || ch1 == 'A' || ch1 == 'E' || ch1=='I' || ch1=='O' || ch1 == 'U') && (ch2=='a' || ch2=='e' || ch2=='i' || ch2=='o' || ch2=='u' || ch2 == 'A' || ch2 == 'E' || ch2=='I' || ch2=='O' || ch2 == 'U')){
           vowel = vowel+ ch1 + ch2;
           S.add(vowel);
           vowel = "";
         }
   
         i++;
       }
     System.out.println(S);
     }
   public static void main(String [] args){
     Scanner sc = new Scanner(System.in);
     System.out.println("Enter the statement:- ");
     String str = sc.nextLine();
     vowelsCount(str);
   }
}
