#include <stdio.h>

int main(){
    int n = 0, i = 0, sum = 0;
    printf("Enter the amount of numbers: ");
    scanf("%d", &n);
    int num[n];
    for(i = 0; i < n; i++){
        printf("Enter number %d: ", i + 1);
        scanf("%d", &num[i]);
    }
    for(i = 0; i < n; i++){
        int temp = num[i];
        temp %= 100; //keeps the last 2 digits [temp = temp % 100]
        int last_digit = temp % 10;
        temp /= 10;
        sum += (last_digit * temp);
    }
    printf("Sum of product of last two digits: %d\n", sum);
}