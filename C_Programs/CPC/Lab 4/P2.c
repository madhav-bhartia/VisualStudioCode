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
        temp /= 10;
        sum += (temp%10);
    }
    printf("Sum of second last digits: %d\n", sum);
}