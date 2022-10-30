/*
Program to calculate the avg of elements of an array
*/
package CH1;
import java.util.Scanner;
public class ArrayAvg 
{
    public static void main(String[] args) 
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter array size: ");
        int size = s.nextInt();
        int[] array = new int[size];
        System.out.println("Enter array values :  ");
        for (int i = 0; i < size; i++) 
        {
            int value = s.nextInt();
            array[i] = value;
        }
        int length = array.length;
        int sum = 0;
        for (int i = 0; i < array.length; i++) 
        {
            sum += array[i];
        }
        double average = sum / length;
        System.out.println("Average of array : " + average);
    }
}
/*
Output
Enter array size:
5
Enter array values :
1
4
7
8
4
Average of array : 4.0
*/
