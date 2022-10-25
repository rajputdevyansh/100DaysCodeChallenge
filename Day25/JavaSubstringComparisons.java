/*
Sample Input 0

welcometojava
3
Sample Output 0

ava
wel
Explanation 0

String  has the following lexicographically-ordered substrings of length :

We then return the first (lexicographically smallest) substring and the last (lexicographically largest) substring as two newline-separated values (i.e., ava\nwel).

The stub code in the editor then prints ava as our first line of output and wel as our second line of output.
*/
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) 
    {
        Scanner SC = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<String>();
        String a = SC.next();
        int b = SC.nextInt();
        for (int i = 0; i <= a.length() - b; i++) {
            String tmp = a.substring(i, b + i);
            list.add(tmp);
        }
        Collections.sort(list);
        System.out.println(list.get(0));
        System.out.println(list.get(list.size() - 1));
    }
}
/*
Test Case 1

Compiler Message
Success
Input (stdin)

welcometojava
3
Expected Output

ava
wel
*/
