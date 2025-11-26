#include <stdio.h>

int main()
{
    int i = 1, sum = 0;

    printf("Using 'for loops':\n");
    printf("The sum of first ten natural numbers:\n");
    for(; i <= 10; i++){
        sum += i;
    }

    printf("Using 'while loops':\n");
    printf("The sum of first ten natural numbers:\n");
    while(i <= 10){
        sum += i;
        i++;
    }

    printf("Using 'do while loops':\n");
    printf("The sum of first ten natural numbers:\n");
    do{
        sum += i;
        i++;
    } while (i <= 10);

    return 0;
}