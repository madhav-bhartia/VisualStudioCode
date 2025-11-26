#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);

    printf("Original value: %d\n", num);
    printf("Post-increment: %d\n", num++);
    printf("After post-increment: %d\n", num);
    num--; // reset to original value

    printf("Pre-increment: %d\n", ++num);
    printf("After pre-increment: %d\n", num);
    num--; // reset to original value

    printf("Post-decrement: %d\n", num--);
    printf("After post-decrement: %d\n", num);
    num++; // reset to original value
    
    printf("Pre-decrement: %d\n", --num);
    printf("After pre-decrement: %d\n", num);

    return 0;
}