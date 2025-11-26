#include <stdio.h>

int main() {
    int num1 = 0, num2 = 0, remainder = 0;
    printf("Enter two integers (x,y): ");
    scanf("%d,%d", &num1, &num2);
    remainder = num1 % num2;
    printf("Remainder of %d / %d = %d\n", num1, num2, remainder);
    return 0;
}