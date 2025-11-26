import java.util.Scanner;
public class Assessment1 {
    public static void main (String args[]) {
        int average,sum=0;
        Scanner input = new Scanner(System.in);
        Scanner length = new Scanner(System.in);
        Scanner option = new Scanner(System.in);

        System.out.println("Enter 1 for arrays, 2 to use ArrayLists, or any other number to end the program");
        int x = option.nextInt();
        switch(x){
            case 1:
                System.out.println("Input array size: ");
                int len = length.nextInt();
                int[] numbers = new int[len];
                for (int i = 0; i < numbers.length; i++)
                {
                    System.out.println("Please enter number");
                    numbers[i] = input.nextInt();
                    sum += numbers[i];
                }
                average = sum/len;
                System.out.println("Total sum of all numbers: "+sum);
                System.out.println("Average of all numbers: "+average);
            case 2:
                //insert your "ArrayList code here,you haven't explained what you 
                //want here
            default:
                System.out.println("Program terminated.");
        }
    }
}