import java.io.*;
import java.lang.*;
class Calc

{

    public static void main(String[] args)

    {

        InputStreamReader in= new InputStreamReader (System.in);
        BufferedReader br= new BufferedReader(in);
        try
        {
            System.out.println ("Single Number Operation - 1");
            System.out.println ("Double Number Operation - 2");
            System.out.println ("Four/Quadruple Number Operation - 3");
            System.out.println ("Triple Number Operation - 4");
            System.out.println ("Five/Quintuple Number Operation - 5");
            System.out.println ("\n\nEnter the choice");
            int a = Integer.parseInt (br.readLine());

             switch (a)
              {
               case 1: System.out.println ("Perfect Square - 1");
                       System.out.println ("Perfect Cube - 2");
                       System.out.println ("Perfect Square Root - 3");
                       System.out.println ("Perfect Cube Root - 4");
                       System.out.println ("/n/nEnter the choice");
                       int b = Integer.parseInt (br.readLine());
                       
                        switch (b)
                         {
                          case 1: System.out.println ("Enter the number");
                                  int a = Integer.parseInt (br.readLine());
                                  System.out.println ("The perfect square is: "+(a*a));
                                  
                                  break;
                                  
                          case 2: System.out.println ("Enter the number");
                                  int b = Integer.parseInt (br.readLine());
                                  System.out.println ("The perfect cube is: "+(b*b*b));
                                  
                                  break;
                                  
                          case 3: System.out.println ("Enter the number");
                                  int c = Integer.parseInt (br.readLine());
                                  System.out.println ("The perfect cube is: "+(b*b*b));
                                  
                                  break;
                                  
                          case 4: System.out.println (" Enter the number");