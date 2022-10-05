/*
to print a simple pattern of * using loop

Sample output:- 

*
**
***
****

*/
public class Starpat {
    public static void main(String[] args) {
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=i;j++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
