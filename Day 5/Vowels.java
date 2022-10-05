import java.util.Scanner;

public class Vowels {
    static int countVowels(String str){
        String brandNewString = str.toLowerCase();
    
        int i=0, count = 0;
        while(i<brandNewString.length()){
          char ch = brandNewString.charAt(i);
          if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u'){
            count++;
          }
          i++;
        }
        return count;
      }
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        System.out.println("Enter the statement ");
        String st = sc.nextLine();
     
    
        sc.close();
    
        System.out.println("The Number of vowels = " +countVowels(st));
      }
}
