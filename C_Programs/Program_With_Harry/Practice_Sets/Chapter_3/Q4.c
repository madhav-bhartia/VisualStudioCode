#include <stdio.h>

int main()   {

    int year;
    printf("Enter a year to check wether it's a leap year or not.\n-> ");
    scanf("%d", &year);

    year%4 == 0 ? printf("This is a leap year!")\
                : printf("This is not a leap year!");
    // just remembered to use the shorthand "if-else", i.e., ?:
    // "if(!(year % 4))" also worked! :)
    // if(year % 4 == 0)
    //     printf("This is a leap year!");
    // else
    //     printf("This is not a leap year!");

    return 0;
}