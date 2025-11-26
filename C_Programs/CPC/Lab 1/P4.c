#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void swapWithoutTemp(int *a, int *b) {
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

int main() {
    int x, y;
    printf("Enter two integers: ");
    scanf("%d,%d", &x, &y);

    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("After swap using temp variable: x = %d, y = %d\n", x, y);
    //i am aware the values don't reset but it doesn't really matter for this example
    printf("Before swap: x = %d, y = %d\n", x, y);
    swapWithoutTemp(&x, &y);
    printf("After swap without using temp variable: x = %d, y = %d\n", x, y);

    return 0;
}