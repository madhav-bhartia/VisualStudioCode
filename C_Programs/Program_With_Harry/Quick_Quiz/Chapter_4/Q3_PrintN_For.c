#include <stdio.h>

int main()
{
    int n;
    printf("Enter the number for first 'n' natural numbers.\n-> ");
    scanf("%d", &n);

    for (int count = 1; count <= n; count++)
    {
        printf("> %d\n", count);
    }

    return 0;
}