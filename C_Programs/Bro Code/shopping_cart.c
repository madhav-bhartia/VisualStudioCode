#include <stdio.h>

int main()
{
    char item[50] = "";
    int quantity = 0;
    float price, total = 0.0f;
    char currency[3] = "INR";

    printf("Welcome to the Shopping Cart!\n");

    printf("Enter the item name: ");
    scanf("%49s", item);

    printf("Enter the quantity: ");
    scanf("%d", &quantity);

    printf("Enter the price of the item: ");
    scanf("%f", &price);

    total = quantity * price;

    printf("\nShopping Cart Summary:\n");
    printf("Item: %s\n", item);
    printf("Quantity: %d\n", quantity);
    printf("Price per item: %.2f %s\n", price, currency);
    printf("Total cost: %.2f %s\n", total, currency);
    printf("Thank you for shopping with us!\n");
    printf("Have a great day!\n");

    return 0;
}