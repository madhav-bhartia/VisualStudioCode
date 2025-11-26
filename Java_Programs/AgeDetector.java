//to tell ur correct age
import java.util.Scanner;
class AgeDetector {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);

        try {
            System.out.println ("enter 1 to start");
            System.out.println("enter 2 to exit");
            int chc=sc.nextInt();
            switch (chc) {
                case 1 -> {
                    System.out.println("Enter ur birth year");
                    int m = sc.nextInt();
                    System.out.println("Enter current year if ur birthday will come and previous year if not");
                    int n = sc.nextInt();
                    {
                        System.out.println("ur age is :" + (n - m));
                    }
                }
                case 2 -> {
                    System.out.println(".........exiting");
                    System.out.println("Goodbye!");
                    System.exit(0);
                }
                default -> {
                }
            }
            
        }
        catch (Exception IO) {
            System.out.println ("Unexpected");
          }
    }
}