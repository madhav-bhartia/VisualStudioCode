// Write a program which prints all numbers between 20 and 40, and all even numbers between 50 and 80 (separate loops).
#include <stdio.h>

int main()
{
    for (int i = 20; i <= 40; i++)
    {
        printf("%d ", i);
    }
    for (int i = 50; i <= 80; i++)
    {
        if (i % 2 == 0)
        {
            printf("%d ", i);
        }
    }
    return 0;
}