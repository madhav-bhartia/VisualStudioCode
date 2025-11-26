import java.io.*;
class Maths_Calculator
{

public static void main(String[] args)
{
     InputStreamReader in= new InputStreamReader (System.in);
     BufferedReader br= new BufferedReader(in);
     try
     {
         System.out.println ("ADDITION- 1");
         System.out.println ("SUBTRACTION- 2");
         System.out.println ("MULTIPLICATION- 3");
         System.out.println ("DIVISION- 4");
         System.out.println ("MODULUS- 5");
         System.out.println ("PERIMETER OF SQUARE- 6");
         System.out.println ("PERIMETER OF RECTANGLE- 7");
         System.out.println ("AREA OF RECTANGLE- 8");
         System.out.println ("PEEIMETER OF PARALLELOGRAM- 9");
         System.out.println ("PERIMETER OF KITE- 10");
         System.out.println ("AREA OF PARALLELOGRAM- 11");
         System.out.println ("AREA OF CYLINDER- 12");
         System.out.println ("AREA OF CONE- 13");
         System.out.println ("AREA OF TRIANGLE- 14");
         System.out.println ("AREA OF KITE- 15");
         System.out.println ("AREA OF RHOMBUS- 16");
         System.out.println ("VOLUME OF CYLINDER- 17");
         System.out.println ("VOLUME OF PRISM- 18");
         System.out.println ("VOLUME OF RIGHT CIRCULAR CONE- 19");
         System.out.println ("VOLUME OF PYRAMID- 20");
         System.out.println ("\n\nENTER THE CHOICE");
         int chc = Integer.parseInt (br.readLine());
         System.out.println ("Enter the first number");
         int m=Integer.parseInt (br.readLine());
         System.out.println ("Enter the second number");
         int n=Integer.parseInt (br.readLine());
         switch (chc)
         {
             case 1: System.out.println ("The addition is :"+(m+n));
             break;
             case 2: System.out.println ("The subtraction is :"+(m-n));
             break;
             case 3: System.out.println ("The multiplication is :"+(m*n));
             break;
             case 4: System.out.println ("The division is :"+(m/n));
             break;
             case 5: System.out.println ("The remainder is :"+(m%n));
             break;
             case 6: System.out.println ("The perimeter of square is :"+(4*m));
             break;
             case 7: System.out.println ("The perimeter of rectangle is :"+((m+n)*2));
             break;
             case 8: System.out.println ("The AREA of rectangle is :"+(m*n));
             break;
             case 9: System.out.println ("The perimeter of parallelogram is :"+((m+n)*2));
             break;
             case 10: System.out.println ("The perimeter of kite is :"+(2*m+2*n));
             break;
             case 11: System.out.println ("The AREA of parallelogram is :"+(m*n));
             break;
             case 12: System.out.println ("The AREA of cylinder is :"+((m+n)*2*3.14*m));
             break;
             case 13: System.out.println ("The AREA of CONE is :"+((m+n)*3.14*m));
             break;
             case 14: System.out.println ("The AREA of TRIANGLE is :"+(m*n*0.5));
             break;
             case 15: System.out.println ("The AREA of KITE is :"+(m*n/2));
             break;
             case 16: System.out.println ("The AREA of RHOMBUS is :"+(0.5*m*n));
             break;
             case 17: System.out.println ("The VOLUME of CYLINDER is :"+(m*m*3.14*n));
             break;
             case 18: System.out.println ("The VOLUME of PRISM is :"+(m*n));
             break;
             case 19: System.out.println ("The VOLUME of RIGHT CIRCULAR CONE is :"+(0.333*3.14*m*m*n));
             break;
             case 20: System.out.println ("The VOLUME of pyramid is :"+(m*n*0.333));
             break;
             default: System.out.println ("Invalid Operation");
         }
    }
            catch (Exception IO)
            {
            System.out.println("Unexpected");
            }
        }
    }