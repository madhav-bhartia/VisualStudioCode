// Write a program which will print all numbers which are multiples of either 3 or 7 (till 100).
#include <stdio.h>

int main()
{
    for (int i = 3; i < 100; i++)
    {
        if (i % 3 == 0 || i % 7 == 0)
        {
            printf("%d ", i);
        }
    }
    return 0;
}