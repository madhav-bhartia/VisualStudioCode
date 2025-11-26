#include <stdio.h>

int main()
{
    int sum, tmp;
    printf("The sum table of 8:\n");
    for (int i = 1; i <= 10; i++)
    {
        tmp = i * 8;
        sum += tmp;
    }
    printf("sum: %d\n", sum);
    
    sum = 0;
    for (int i = 1; i <= 10; i++)
    {
        sum += (i * 8);
    }
    printf("sum: %d\n", sum);

    return 0;
}