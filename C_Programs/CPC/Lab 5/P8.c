/*Write a function to find the greatest common divisor (GCD) of two numbers.
 Function Signature: int gcd(int a, int b);
 Hint:
o Use the Euclidean algorithm:
 While b is not zero, set a = b and b = a % b.
o When b becomes 0, a contains the GCD.*/
#include <stdio.h>

int gcd(int a, int b);

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    int result = gcd(a, b);
    printf("The GCD of %d and %d is: %d\n", a, b, result);
    return 0;
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;  // Update b to a % b
        a = temp;   // Update a to the old value of b
    }
    return a; // When b is 0, a contains the GCD
}