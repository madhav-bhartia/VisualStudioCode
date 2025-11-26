import java.io.*;
class Square
{
    public static void main(String[] args)
    {
        InputStreamReader in = new InputStreamReader (System.in);
        BufferedReader br = new BufferedReader(in);
        try
        {
            System.out.println ("Square --- 1");
            System.out.println ("cube --- 2");
            System.out.println ("enter the choice");
            int chc=Integer.parseInt (br.readLine());

            System.out.println ("Enter the number");
            int m=Integer.parseInt (br.readLine());

            int a=m*m;
            int b=m*m*m;

            switch (chc)
            {
                case 1: System.out.println (" the square is:" +a);
                break;

                case 2: System.out.println (" the cube is:" +b);
                break;

                default: System.out.println ("Invalid operation");

            }
        }
        catch (Exception IO)
        {
            System.out.println ("Unexpected");
        }
    }
}