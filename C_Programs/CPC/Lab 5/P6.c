/*Write a function to check if a number is prime.
 Function Signature: int isPrime(int num);
 Hint:
o Use a loop from 2 to sqrt(num) to check if the number is divisible by any integer.
o If divisible by any number other than 1 and itself, return 0 (not prime); otherwise,
return 1 (prime).*/
#include <stdio.h>

int isPrime(int num);

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    if (isPrime(num)) {
        printf("%d is a prime number.\n", num);
    } else {
        printf("%d is not a prime number.\n", num);
    }
    return 0;
}

int isPrime(int num) {
    if (num <= 1) {
        return 0; // Numbers less than or equal to 1 are not prime
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0; // Found a divisor, not prime
        }
    }
    return 1; // No divisors found, is prime
}