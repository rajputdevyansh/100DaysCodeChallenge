/*
To take input of 3 values of iteams and give the total without gst and then gst 18 % and then total sum

sample input
Enter Values
741.2
885.2
74.12

sample output
Total Amount Without GST:- 1700.52
GST:- 306.0936
Final Amount:- 2006.6136
*/

import java.util.Scanner;

public class Bill3I {
    public static void main(String[] args) {
        float p1,p2,p3,sum,gst,Total;
        Scanner Sc=new Scanner(System.in);
        System.out.println("Enter Values");
        p1=Sc.nextFloat();
        p2=Sc.nextFloat();
        p3=Sc.nextFloat();
        sum=p1+p2+p3;
        System.out.println("Total Amount Without GST:- "+sum);
        gst=sum*18/100;
        System.out.println("GST:- "+gst);
        Total=sum+gst;
        System.out.println("Final Amount:- "+Total);

    }
}
