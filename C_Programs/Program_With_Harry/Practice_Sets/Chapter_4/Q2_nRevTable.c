#include <stdio.h>

int main()
{
    int n, count;
    printf("Enter the number 'n' for it's multiplication table.\n-> ");
    scanf("%d", &n);
    printf("Enter from what number you want it's table!\n-> ");
    scanf("%d", &count);
    printf("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n");

    // just "count" for "true" or "false" works
    // but this protects from negative inputs
    for (; count > 0; count--)
    {
        printf("> %d X %d = %d\n", n, count, n * count);
    }

    return 0;
}