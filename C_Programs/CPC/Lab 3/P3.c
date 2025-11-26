// Write a program which will print all even numbers less than 50 and all odd numbers more than 50.
// assuming max limit as 100. And that 50 is not included in either.
#include <stdio.h>

int main()
{
    for (int i = 2; i < 49; i++)
    {
        if (i % 2 == 0)
        {
            printf("%d ", i);
        }
    }
    for (int i = 51; i < 100; i++)
    {
        if (i % 2 != 0)
        {
            printf("%d ", i);
        }
    }
    return 0;
}