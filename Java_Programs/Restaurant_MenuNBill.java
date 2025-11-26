import java.io.*;
public class Restaurant_MenuNBill {
    public static void main(String[] args) {
        InputStreamReader in = new InputStreamReader (System.in);
        BufferedReader br = new BufferedReader(in);
        try {
            System.out.println ("Welcome to The Foodies Restaurant");
            System.out.println ("Here's our menu");
            System.out.println ("Note:You can only order 3 items at once (Since they are enough for a family of 4 😉)");
            System.out.println ("Also we recommend to order 1 Bread, 1 Subzi and for the 3rd what u want");

            System.out.println ("1. Vada Pav (Bombay Style) || ₹80");
            System.out.println ("2.Chura Pav || ₹80");
            System.out.println ("3.Vada Pav Grilled || ₹86");
            System.out.println ("4.Vada Pav Cheese || ₹99");
            System.out.println ("5.Kutch Ni Dabeli || ₹99");
            System.out.println ("6.Papad Paneer Pakoda || ₹86");
            System.out.println ("7.Moong Daal Ke Pakode || ₹80");
            System.out.println ("8.Pohe || ₹80");
            System.out.println ("9.Sev Pudi || ₹99");
            System.out.println ("10.Alu Tikki Burger || ₹80");
            System.out.println ("11.Veg Patty Burger || ₹86");
            System.out.println ("12.Coleslaw Sandwich || ₹90");
            System.out.println ("13.Tomato Cucumber Sandwich || ₹99");
            System.out.println ("14.Veg Supreme Momos || ₹99");
            System.out.println ("15.Paneer Momos || ₹79");
            System.out.println ("16.Plain Parantha || ₹80");
            System.out.println ("17.Alu Parantha || ₹85");
            System.out.println ("18.Pyaz Parantha || ₹88");
            System.out.println ("19.Paneer Parantha || ₹90");
            System.out.println ("20.Mix Parantha || ₹99");
            System.out.println ("21.Pav Bhaji || ₹99");
            System.out.println ("22.Daal, Baati, Churma || ₹99");
            System.out.println ("23.Litti Chokha || ₹86");
            System.out.println ("24.Veg. Thali || ₹99");
            System.out.println ("25.Poori Subji || ₹70");
            System.out.println ("26.Gatte Ki Subji || ₹50");
            System.out.println ("27.Kair Sangri ki Subji || ₹50");
            System.out.println ("28.Bajre ka Roti || ₹50");
            System.out.println ("29.Makke ki Roti || ₹50");
            System.out.println ("\n\n Enter your First choice");
            int x = Integer.parseInt (br.readLine());
            System.out.println ("Please enter the price of your First choice");
            int prc_1 = Integer.parseInt (br.readLine());

            System.out.println ("\n Enter your Second choice");
            int y = Integer.parseInt (br.readLine());
            System.out.println ("Please enter the price of your Second choice");
            int prc_2 = Integer.parseInt (br.readLine());

            System.out.println ("\n Enter your Third choice");
            int z = Integer.parseInt (br.readLine());
            System.out.println ("Please enter the price of your Third choice");
            int prc_3 = Integer.parseInt (br.readLine());

            System.out.println ("\n Please wait for 10 minutes");
            System.out.println ("\n *10 minutes pass*");
            System.out.println ("\n Here is your order!");
            System.out.println ("\n x \n y \n z");
            System.out.println ("\n Bon appétit!");
            System.out.println ("\n *after 1 hour*");
            System.out.println ("\n here is your bill: ₹"+(prc_1+prc_2+prc_3));
            System.out.println ("\n *Bill paid*");
            System.out.println ("\n Thank you for dining out.");
            System.out.println ("\n Come sometime again");
        }
        catch (Exception IO) {
            System.out.println ("Unexpected");
        }
    }
}