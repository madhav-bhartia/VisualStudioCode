#include <stdio.h>

int main()
{

    char ch;
    printf("Enter a character to check if it's lowercase or uppercase.\n-> ");
    scanf("%c", &ch);

    ch >= 97 && ch <= 122 ? printf("Yes, this is a lowercase character!")
                          : printf("No, this is not a lowercase character!");

    return 0;
}