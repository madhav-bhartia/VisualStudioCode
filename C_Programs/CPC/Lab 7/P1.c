#include <stdio.h>

int main() {
    int num;
    int *ptr;
    
    printf("Enter a number: ");
    scanf("%d", &num);
    
    ptr = &num;
    
    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", &num);
    printf("Value of ptr (address it stores): %p\n", ptr);
    printf("Value at address stored in ptr: %d\n", *ptr);
    
    return 0;
}