import java.rmi.*;
import java.rmi.registry.*;
public class Server{
  public static void main(String args[]){
    try{
      Calc stub = new CalcRemote();
      Naming.rebind("connect_string",stub);
      System.out.println("Server started and connected !!!");
    }catch (Exception e){
      System.out.println("Server could not connect !!!");
      System.out.println(e);
    }
  }
}