#include <stdio.h>

int fib(int);

int main()
{
    int n;
    printf("Enter a value 'n' for nth element in fibonacci series.\n-> ");
    scanf("%d", &n);
    printf("%d\n", fib(n));    

    return 0;
}

int fib(int n){
    if (n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}