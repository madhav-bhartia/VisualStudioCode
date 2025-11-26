#include <stdio.h>

int main()
{
    int n, count = 1;
    printf("Enter the number for first 'n' natural numbers.\n-> ");
    scanf("%d", &n);

    do{
        printf("> %d\n", count);
        count++;
    } while (count <= n);

    return 0;
}