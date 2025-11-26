// Write a program which will print all numbers which are either a multiple of 3 or 5 but not both. For example: 3 5 6 9 10 12 18 20 …… (assuming till 100)
#include <stdio.h>

int main()
{
    printf("Numbers which are either a multiple of 3 or 5 but not both up to 100 are:\n");
    for (int i = 3; i <= 100; i++)
    {
        if ((i % 3 == 0) ^ (i % 5 == 0)) // XOR operator
        {
            printf("%d ", i);
        }
    }
    return 0;
}