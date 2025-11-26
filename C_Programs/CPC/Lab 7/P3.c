#include <stdio.h>

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    int arr[n];
    int *ptr = arr;
    
    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", ptr + i);
    }
    
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += *(ptr + i);
    }
    
    float average = (float)sum / n;
    
    printf("Sum: %d\n", sum);
    printf("Average: %.2f\n", average);
    
    return 0;
}