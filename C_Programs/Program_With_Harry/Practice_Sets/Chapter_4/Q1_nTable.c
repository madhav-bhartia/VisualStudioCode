#include <stdio.h>

int main() {
    int n, control;
    printf("Enter the number 'n' for it's multiplication table.\n-> ");
    scanf("%d", &n);
    printf("Enter till what number you want it's table!\n-> ");
    scanf("%d", &control);
    printf("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n");3

    for (int count = 1; count <= control; count++) {
        printf("> %d X %d = %d\n", n, count, n * count);
    }

    return 0;
}