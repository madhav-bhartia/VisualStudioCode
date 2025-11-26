// Write a program in Java to find the sum of three numbers entered by the user.
import java.io.*;
class Sum
{
    public static void main  (String[]  args)
    {

        InputStreamReader  in= new InputStreamReader  (System.in);
        BufferedReader  br= new BufferedReader  (in);
        try
        {

            System.out.println  ("Enter The First Number");

            int  m=Integer.parseInt  (br.readLine());

            System.out.println  ("The second number");

            int  n=Integer.parseInt  (br.readLine());

            System.out.println  ("Enter the third number");

            int  o=Integer.parseInt  (br.readLine());

            int  sum= m+n+o;

            System.out.println ("the sum of three numbers entered are :"+sum) ;

        }

        catch  (Exception  IO)

        {

            System.out.println  ("unexpected");

        }

    }

}