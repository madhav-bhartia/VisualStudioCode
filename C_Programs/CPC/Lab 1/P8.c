//Average of three numbers
#include <stdio.h>

int main() {
    int num1 = 0, num2 = 0, num3 = 0;
    float average = 0.0;
    printf("Enter three integers (x,y,z): ");
    scanf("%d,%d,%d", &num1, &num2, &num3);
    average = (num1 + num2 + num3) / 3.0f;
    printf("Average of %d, %d and %d = %.2f\n", num1, num2, num3, average);
    return 0;
}