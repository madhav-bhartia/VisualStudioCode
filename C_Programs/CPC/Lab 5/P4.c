#include <stdio.h>

void swap(int a, int b);

int main() {
    int x, y;
    printf("Enter two numbers to swap: ");
    scanf("%d %d", &x, &y);
    printf("Before swapping: x = %d, y = %d\n", x, y);
    swap(x, y);
    printf("After swapping (inside main): x = %d, y = %d\n", x, y);
    return 0;
}

void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swap function: a = %d, b = %d\n", a, b);
}