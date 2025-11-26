#include <stdio.h>

int sumN(int);

int main()
{
    int n;
    printf("Enter 'n' for sum of first 'n' numbers.\n-> ");
    scanf("%d", &n);
    printf("Sum: %d\n", sumN(n));

    return 0;
}

int sumN(int n){
    if (n <= 0){
        return n;
    }
    return n + sumN(n-1);
}