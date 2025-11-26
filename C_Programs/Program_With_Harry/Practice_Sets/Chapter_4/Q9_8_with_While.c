#include <stdio.h>

int main()
{
    int n, i = 1, factorial;
    printf("Enter a number to calculate the factorial of:\n-> ");
    scanf("%d", &n);
    while (i <= n)
    {
        factorial *= i;
        i++;
    }
    printf("factorial: %d\n", factorial);

    return 0;
}