public class Exp7 
{
    public static void main(String[] args) 
     {
        int n, count, a, b, sum = 0;
        System.out.print("Armstrong numbers from 1 to 1000: ");
        for(int i = 1; i <= 1000; i++)
        {
            n = i;
            a=i;
            count=0;
            while(a > 0)
            {
            a = a / 10;
            count++;
            }
            while(n > 0)
            {
                b = n % 10;
                sum = (int) (sum+Math.pow(b, count));
                n = n / 10;
            }
            if(sum == i)
            {
                System.out.print(i+" ");
            }
            sum = 0;
        }
    }
}
