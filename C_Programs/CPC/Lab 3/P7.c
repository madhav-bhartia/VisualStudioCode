// Write a program which will print all numbers which are even but not a multiple of either 3 or 5. (assuming till 100)
#include <stdio.h>

int main()
{
    printf("Even numbers which are not multiple of 3 or 5 up to 100 are:\n");
    for (int i = 2; i < 100; i++)
    {
        if (i % 2 == 0 && i % 3 != 0 && i % 5 != 0)
        {
            printf("%d ", i);
        }
    }
    return 0;
}