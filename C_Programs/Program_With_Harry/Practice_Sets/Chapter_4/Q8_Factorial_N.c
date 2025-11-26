#include <stdio.h>

int main()
{
    int n, factorial;
    printf("Enter a number to calculate the factorial of:\n-> ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        factorial *= i;
    }
    printf("(Factorial) %d! is: %d\n", n, factorial);

    return 0;
}