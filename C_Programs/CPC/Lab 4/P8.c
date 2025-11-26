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
        sum += (temp * (i + 1));
    }
    printf("Weighted Sum: %d\n", sum);
}