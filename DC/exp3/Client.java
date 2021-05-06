import java.rmi.*;
import java.util.Scanner;
public class Client{
  public static void main(String args[]){
    System.out.println("---------------------------MENU-------------------------");
    System.out.println("1. Addition 2.Subtraction 3.Multiplication 4.Division");
    System.out.println("Enter your choice >>>> ");
    Scanner sc = new Scanner(System.in);
    try{
      Calc stub = (Calc)Naming.lookup("connect_string");
      int ch = sc.nextInt();
      int x, y;
      switch (ch) {
        case 1:
            {
                System.out.println("Enter 1st Value >>>> ");
                x = sc.nextInt();
                System.out.println("Enter 2nd Value >>>> ");
                y = sc.nextInt();
                System.out.println("Addition of " + x + " " + y + " is >>>> " + stub.add(x, y));
                break;
            }
        case 2:
            {
                System.out.println("Enter 1st Value >>>> ");
                x = sc.nextInt();
                System.out.println("Enter 2nd Value >>>> ");
                y = sc.nextInt();
                System.out.println("Subtraction of " + x + " " + y + " is >>>> " + stub.sub(x, y));
                break;
            }
        case 3:
            {
                System.out.println("Enter 1st Value >>>> ");
                x = sc.nextInt();
                System.out.println("Enter 2nd Value >>>> ");
                y = sc.nextInt();
                System.out.println("Multiplication of " + x + " " + y + " is >>>> " + stub.mul(x, y));
                break;
            }
        case 4:
            {
                System.out.println("Enter 1st Value >>>> ");
                x = sc.nextInt();
                System.out.println("Enter 2nd Value >>>> ");
                y = sc.nextInt();
                System.out.println("Division of " + x + " " + y + " is >>>> " + stub.div(x, y));
                break;
            }
      }
      // System.out.println(stub.add(3,4)); 
    }catch(Exception e){
      System.out.println(e); 
    }
  }
}