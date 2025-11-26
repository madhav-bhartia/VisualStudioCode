#include <stdio.h>

int main()
{

    int num;
    printf("Enter a number to check for divisibility with 97\n-> ");
    scanf("%d", &num);

    printf("If answer is '0' then it's divisible by 97");
    printf("otherwise it's not divisible by 97\n> ");
    printf("%d", num % 97);

    return 0;
}