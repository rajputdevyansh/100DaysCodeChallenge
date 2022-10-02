public class SumN {
    public static void main(String[] args) {
        int i,n,sum=0;
        Scanner Sc=new Scanner(System.in);
        System.out.println("Enter Numbers");
        n=Sc.nextInt();
        for(i=0;i<=n;i++)
        {
            sum=sum+i;
        }
        System.out.println("Sum:-  "+sum);
    }
}
