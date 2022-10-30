/*
program to calulate the power of an integer
*/
package CH1;
import java.util.Scanner;
public class Power 
{
        static int power(int N, int P)
        {
            if (P == 0)
                return 1;
            else
                return N * power(N, P - 1);
        }
        public static void main(String[] args)
        {
            Scanner Sc= new Scanner(System.in);
            int N = Sc.nextInt();
            int P = Sc.nextInt();
            System.out.println(power(N, P));
        }
}
/*
Output
2
2
4
*/
/*
Output
10
8
100000000
*/
