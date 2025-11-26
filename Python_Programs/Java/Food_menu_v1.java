import java.util.ArrayList;
import java.util.Scanner;

public class FoodMenu {

    public static void main(String[] args) {

        // Creating food items
        FoodItem burger = new FoodItem("Burger", "Continental", 100);
        FoodItem fries = new FoodItem("Fries", "Continental", 50);
        FoodItem pasta = new FoodItem("Pasta", "Italian", 150);
        FoodItem pizza = new FoodItem("Pizza", "Italian", 200);
        // add more items here

        // Grouping food items by category
        ArrayList<FoodItem> continentalItems = new ArrayList<>();
        continentalItems.add(burger);
        continentalItems.add(fries);

        ArrayList<FoodItem> italianItems = new ArrayList<>();
        italianItems.add(pasta);
        italianItems.add(pizza);

        // Creating menu
        ArrayList<ArrayList<FoodItem>> menu = new ArrayList<>();
        menu.add(continentalItems);
        menu.add(italianItems);

        // Printing menu
        System.out.println("Welcome to the restaurant!");
        System.out.println("What would you like to order?");
        System.out.println("Type 'done' when you're finished.");

        Scanner scanner = new Scanner(System.in);
        ArrayList<FoodItem> order = new ArrayList<>();

        while (true) {
            // Printing categories
            System.out.println("Categories:");
            for (int i = 0; i < menu.size(); i++) {
                System.out.println((i + 1) + ". " + menu.get(i).get(0).category);
            }
            System.out.println("Enter the number of the category you want to order from:");
            int categoryIndex = scanner.nextInt() - 1;

            // Printing items in the chosen category
            ArrayList<FoodItem> chosenCategory = menu.get(categoryIndex);
            System.out.println("Items:");
            for (int i = 0; i < chosenCategory.size(); i++) {
                System.out.println((i + 1) + ". " + chosenCategory.get(i).name + " - " + chosenCategory.get(i).price + " INR");
            }
            System.out.println("Enter the number of the item you want to order:");
            int itemIndex = scanner.nextInt() - 1;

            // Adding item to order
            FoodItem chosenItem = chosenCategory.get(itemIndex);
            order.add(chosenItem);
            System.out.println("Added " + chosenItem.name + " to your order.");

            // Asking if user wants to order more
            System.out.println("Do you want to order more? (yes/no)");
            String answer = scanner.next().toLowerCase();
            if (answer.equals("no")) {
                break;
            }
        }

        // Calculating total price
        int totalPrice = 0;
        for (FoodItem item : order) {
            totalPrice += item.price;
        }

        // Printing order and total price
        System.out.println("Order:");
        for (FoodItem item : order) {
            System.out.println("- " + item.name + " - " + item.price + " INR");
        }
        System.out.println("Total price: " + totalPrice + " INR");
    }

    static class FoodItem {
        String name;
        String category;
        int price;

        public FoodItem(String name, String category, int price) {
            this.name = name;
            this.category = category;
            this.price = price;
        }
    }

}
