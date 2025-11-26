import java.io.*;
class Rectangle
{
    public static void main  (String[]  args)
    {

        InputStreamReader  in= new InputStreamReader  (System.in);
        BufferedReader  br= new BufferedReader  (in);
        try
        {

            System.out.println  ("Area - 1");
            System.out.println  ("Perimeter - 2");
            System.out.println  ("Enter the choice");

            int  chc=Integer.parseInt (br.readLine());

            System.out.println ("Enter the Length") ;
            int  m=Integer.parseInt (br.readLine());

            System.out.println ("Enter the Breadth") ;
            int  n=Integer.parseInt (br.readLine());

            switch (chc)
            {
                case 1: 
                    int area=m*n;
                    System.out.println (" the area is:" +area);
                    break;

                case 2: 
                    int perimeter=(m+n)*2;
                    System.out.println (" the perimeter is:" +perimeter);
                    break;

                default: System.out.println ("Invalid operation");

            }

        }

        catch  (Exception  IO)

        {

            System.out.println  ("unexpected");

        }

    }

}