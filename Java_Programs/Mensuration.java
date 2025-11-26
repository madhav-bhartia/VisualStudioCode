import java.util.Scanner ;
public class Mensuration {
    public static void main (String[] args)
    {
        float a, b, area = 0; 
        int choice;
        Scanner sc = new Scanner(System.in);
        System.out.println("Shapes' Area Menu"); 
        System.out.println("1. Circle.");
        System.out.println("2. Square.");
        System.out.println("3. Rectangle.");
        System.out.println("4. Triangle.");
        System.out.println("Enter your choice 1 to 4 "); 
        choice = sc.nextInt( );
        switch(choice)
        {
            case 1:
                System.out.println("Area of Circle"); 
                System.out.println("Enter radius:");
                a = sc.nextFloat( );
                area = 3.14f*a*a;
                break;
            case 2:
                System.out.println("Area of Square");
                System.out.println("Enter side:");
                a = sc.nextFloat( );
                area = a*a;
                break;
            case 3:
                System.out.println("Area of Rectangle");
                System.out.println("Enter length and breadth:");
                a = sc.nextFloat( );
                b = sc.nextFloat( );
                area = a* b;
                break;
            case 4:
                System.out.println("Area of Triangle");
                System.out.println("Enter base and hieght:");
                a = sc.nextFloat();
                b = sc.nextFloat();
                area = 0.5f*a*b;
                break;
            default:
                System.out.println("Invalid Choice,Valid choices are 1 to 4");
        }
        System.out.println("Area = "+area);
    }
}