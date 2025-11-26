import java.util.Scanner;
/* import java.util.Dictionary;
import java.util.Hashtable; */
class Adv_Restaurant_MenuNBill {
public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        /*  Dictionary<Integer,Integer> menu = new Hashtable<>();

        menu.put(1, 49);
        menu.put(2, 79);
        menu.put(3, 59);
        menu.put(4, 99);
        menu.put(5, 99);
        menu.put(6, 109);
        menu.put(7, 99);
        menu.put(8, 79);
        menu.put(9, 99);
        menu.put(10, 49);
        menu.put(11, 59);
        menu.put(12, 89);
        menu.put(13, 99);
        menu.put(14, 99);
        menu.put(15, 79);
        menu.put(16, 79);
        menu.put(17, 79);
        menu.put(18, 89);
        menu.put(19, 99);
        menu.put(20, 109);
        menu.put(21, 99);
        menu.put(22, 99);
        menu.put(23, 89);
        menu.put(24, 99);
        menu.put(25, 79);
        menu.put(26, 49);
        menu.put(27, 49);
        menu.put(28, 49);
        menu.put(29, 49); */


        int[][] menu = new int[29][1];
        menu[0][0] = 1;
        menu[1][0] = 2;
        menu[2][0] = 3;
        menu[3][0] = 4;
        menu[4][0] = 5;
        menu[5][0] = 6;
        menu[6][0] = 7;
        menu[7][0] = 8;
        menu[8][0] = 9;
        menu[9][0] = 10;
        menu[10][0] = 11;
        menu[11][0] = 12;
        menu[12][0] = 13;
        menu[13][0] = 14;
        menu[14][0] = 15;
        menu[15][0] = 16;
        menu[16][0] = 17;
        menu[17][0] = 18;
        menu[18][0] = 19;
        menu[19][0] = 20;
        menu[20][0] = 21;
        menu[21][0] = 22;
        menu[22][0] = 23;
        menu[23][0] = 24;
        menu[24][0] = 25;
        menu[25][0] = 26;
        menu[26][0] = 27;
        menu[27][0] = 28;
        menu[28][0] = 29;

        menu[0][1] = 49;
        menu[1][1] = 79;
        menu[2][1] = 59;
        menu[3][1] = 99;
        menu[4][1] = 99;
        menu[5][1] = 109;
        menu[6][1] = 99;
        menu[7][1] = 79;
        menu[8][1] = 99;
        menu[9][1] = 49;
        menu[10][1] = 59;
        menu[11][1] = 89;
        menu[12][1] = 99;
        menu[13][1] = 99;
        menu[14][1] = 79;
        menu[15][1] = 79;
        menu[16][1] = 79;
        menu[17][1] = 89;
        menu[18][1] = 99;
        menu[19][1] = 109;
        menu[20][1] = 99;
        menu[21][1] = 99;
        menu[22][1] = 89;
        menu[23][1] = 99;
        menu[24][1] = 79;
        menu[25][1] = 49;
        menu[26][1] = 49;
        menu[27][1] = 49;
        menu[28][1] = 49;
        
        System.out.println ("Welcome to The Foodies Restaurant");
        System.out.println ("Here's our menu");
        System.out.println ("Note:You can only order 3 items at once (Since they are enough for a family of 4 or 1 very hungry person (we won't judge)😉)");
        System.out.println ("Also we recommend to order 1 Bread, 1 Subzi and for the 3rd what u want");
    
        System.out.println ("1. Vada Pav (Bombay Style) || ₹49");
        System.out.println ("2.Chura Pav || ₹79");
        System.out.println ("3.Vada Pav Grilled || ₹59");
        System.out.println ("4.Vada Pav Cheese || ₹99");
        System.out.println ("5.Kutch Ni Dabeli || ₹99");
        System.out.println ("6.Papad Paneer Pakoda || ₹109");
        System.out.println ("7.Moong Daal Ke Pakode || ₹99");
        System.out.println ("8.Pohe || ₹79");
        System.out.println ("9.Sev Pudi || ₹99");
        System.out.println ("10.Alu Tikki Burger || ₹49");
        System.out.println ("11.Veg Patty Burger || ₹59");
        System.out.println ("12.Coleslaw Sandwich || ₹89");
        System.out.println ("13.Tomato Cucumber Sandwich || ₹99");
        System.out.println ("14.Veg Supreme Momos || ₹99");
        System.out.println ("15.Paneer Momos || ₹79");
        System.out.println ("16.Plain Parantha || ₹79");
        System.out.println ("17.Alu Parantha || ₹79");
        System.out.println ("18.Pyaz Parantha || ₹89");
        System.out.println ("19.Paneer Parantha || ₹99");
        System.out.println ("20.Mix Parantha || ₹109");
        System.out.println ("21.Pav Bhaji || ₹99");
        System.out.println ("22.Daal, Baati, Churma || ₹99");
        System.out.println ("23.Litti Chokha || ₹89");
        System.out.println ("24.Veg. Thali || ₹99");
        System.out.println ("25.Poori Subji || ₹79");
        System.out.println ("26.Gatte Ki Subji || ₹49");
        System.out.println ("27.Kair Sangri ki Subji || ₹49");
        System.out.println ("28.Bajre ka Roti || ₹49");
        System.out.println ("29.Makke ki Roti || ₹49\n");
        
        while (true) {
            System.out.println("Please enter the S.No. of the food u want to eat!");
            System.out.println("To complete the order enter '0'!");
            int food = sc.nextInt();

            if (food == 0) {
                break;
            }

            int bill = 0;

            for (int m = 0; m < 30; m++) {
                if (food == menu[m][0]) {
                    bill += menu[m][1];
                    break;
                }
            }

            System.out.println("The bill is " + bill);

            sc.close();

        }
    }
}
