#include <stdio.h>

int isEven(int num);

int main(){

    int num = 0;
    printf("Enter a number: ");
    scanf("%d", &num);
    if(isEven(num)){
        printf("%d is even.\n", num);
    } else {
        printf("%d is odd.\n", num);
    }

    return 0;
}

int isEven(int num){
    if (num % 2 == 0){
        return 1;}
    else {
        return 0;}
}