#include <stdio.h>

int main()
{
    int n;
    printf("Enter the number for");
    printf("printing the first 'n' natural numbers in reverse order.\n-> ");
    scanf("%d", &n);

    for (int count = n; count; count--)
    {
        printf("> %d\n", count);
    }

    return 0;
}