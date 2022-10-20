/*
Write a program to display all perfect number up to 500.
*/
public class Exp5 
{
    public static void main(String[] args) 
    {
        int i,j,sum;
        System.out.println("All perfect no between 1 to 500");
        for(i=1;i<=500;i++)
        {
            sum=0;
            for(j=1;j<i;j++)
            {
                if(i%j==0)
                {
                    sum+=j;
                }
            }
            if(sum == i)
            {
                System.out.println(i);
            }
        }
        
    }
}
