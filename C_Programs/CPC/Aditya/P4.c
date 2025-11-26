#include<stdio.h>
int main()
{
    for (int i = 0; i <= 3;i=i+1)
    {
        for (int j = 0; j <= i;j=j+1)
        {
            printf("%d", i + 1);
        }
        printf("\n");
    }
    return 0;
}