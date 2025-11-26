/*Write a function to calculate the power of a number.
 Function Signature: int power(int base, int exp);
 Hint:
o Use a loop to multiply base by itself exp times.
o Initialize result as 1, and in each iteration, multiply result by base.*/
#include <stdio.h>

int power(int base, int exp);

int main() {
    int base, exp;
    printf("Enter base and exponent: ");
    scanf("%d %d", &base, &exp);
    int result = power(base, exp);
    printf("%d raised to the power of %d is: %d\n", base, exp, result);
    return 0;
}

int power(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;  // Multiply result by base in each iteration
    }
    return result;
}