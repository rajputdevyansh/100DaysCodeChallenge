public static int B,H;
    public static boolean Check=false;
    
    static
    {
        Scanner sc=new Scanner(System.in);
        B=sc.nextInt();
        H=sc.nextInt();
        if(B>0 && H>0)
        {
          Check=true;
        }
        else
        {
          System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
    }

    public static void main(String[] args) 
    {
        if(Check)
        {
           int area=B*H;
           System.out.println(area); 
        }
    }
