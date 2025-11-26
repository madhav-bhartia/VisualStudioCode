// Write a program which prints all even numbers between 20 and 70.
#include <stdio.h>

int main()
{
    for (int i = 20; i <= 70; i++)
    {
        if (i % 2 == 0)
        {
            printf("%d ", i);
        }
    }
    return 0;
}