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
        int last2digits = temp % 100;
        temp /= 100;
        int revLast2digits = (last2digits % 10) * 10 + (last2digits / 10);
        sum += ((temp * 100) + revLast2digits);
    }
    printf("Sum with last two digits reversed: %d\n", sum);
}