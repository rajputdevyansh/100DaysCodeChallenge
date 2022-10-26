/*
Function Description

Complete the isAnagram function in the editor.

isAnagram has the following parameters:

string a: the first string
string b: the second string
Returns

boolean: If  and  are case-insensitive anagrams, return true. Otherwise, return false.
Input Format

The first line contains a string .
The second line contains a string .

Constraints

Strings  and  consist of English alphabetic characters.
The comparison should NOT be case sensitive.
*/
import java.util.Scanner;
public class Solution {
    static boolean isAnagram(String a, String b) 
    {
        String S1 = a;
        String S2 = b;
        S1=S1.toLowerCase();
        S2=S2.toLowerCase();
        
        if(S1.length()==S2.length())
        {
            int[] arr = new int[256];
            int[] brr = new int[256];
            for (int i = 0; i < S1.length(); i++) {
                arr[(int) S1.charAt(i)] += 1;
                brr[(int) S2.charAt(i)] += 1;
            }
            for (int i = 0; i < 256; i++) {
                if (arr[i] != brr[i])
                    return false;
            }
            return true;
        }
        else
        {
            return false;
        }
    }
  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String A = scan.next();
        String B = scan.next();
        scan.close();
        boolean ret = isAnagram(A,B);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}

/*
Test case
Compiler Message
Success
Input (stdin)

anagram
margana
Expected Output

Anagrams
*/

/*
test Case
Compiler Message
Success
Input (stdin)

anagramm
marganaa
Expected Output

Not Anagrams
*/

/*
Test Case
Compiler Message
Success
Input (stdin)

Hello
hello
Expected Output

Anagrams
*/
