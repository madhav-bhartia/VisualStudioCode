#include<stdio.h>
int main()
{
    for (int i = 4; i>=0 ;i=i-1)
    {
        for (int j = i; j >= 0;j=j-1)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}