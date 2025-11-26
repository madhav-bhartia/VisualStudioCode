#include <stdio.h>

int greatestOfThree(int a, int b, int c);

int main() {
    int a, b, c;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    int greatest = greatestOfThree(a, b, c);
    printf("The greatest of the three numbers is: %d\n", greatest);
    return 0;
}

int greatestOfThree(int a, int b, int c) {
    if (a >= b && a >= c) {
        return a;
    } else if (b >= a && b >= c) {
        return b;
    } else {
        return c;
    }
}