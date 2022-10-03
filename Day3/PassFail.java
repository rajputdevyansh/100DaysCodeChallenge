import java.util.Scanner;

public class PassFail {
    public static void main(String[] args) {
        int m;
        Scanner Sc = new Scanner(System.in);
        System.out.println("enter marks");
        m=Sc.nextInt();
        String Rc= (m>=33)?"pass":"Fail";
        System.out.println(Rc);

    }
}
