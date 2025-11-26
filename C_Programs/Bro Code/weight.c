#include <stdio.h>
int main() {
    int chc = 0;
    float weight = 0.0f;

    printf("Weight Conversion Program:\n");
    printf("1. Convert from Pounds to Kilograms\n");
    printf("2. Convert from Kilograms to Pounds\n");
    printf("Enter your choice (1 or 2): ");
    scanf("%d", &chc);

    if (chc == 1) {
        printf("Enter weight in Pounds: ");
        scanf("%f", &weight);
        weight = weight * 0.453592; // Convert pounds to kilograms
        printf("Weight in Kilograms: %.2f kg\n", weight);
    } else if (chc == 2) {
        printf("Enter weight in Kilograms: ");
        scanf("%f", &weight);
        weight = weight / 0.453592; // Convert kilograms to pounds
        printf("Weight in Pounds: %.2f lbs\n", weight);
    } else {
        printf("Invalid choice! Please enter 1 or 2.\n");
    }

    return 0;
}