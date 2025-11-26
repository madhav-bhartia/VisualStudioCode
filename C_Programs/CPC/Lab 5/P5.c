/*Write a function to calculate the sum of digits of a number.
 Function Signature: int sumOfDigits(int num);
 Hint:
o Use a loop to extract digits using modulus % 10 and then reduce the number by / 10.
o Accumulate the sum of the extracted digits and return the result.*/
#include <stdio.h>

int sumOfDigits(int num);

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    int sum = sumOfDigits(num);
    printf("The sum of digits of %d is: %d\n", num, sum);
    return 0;
}

int sumOfDigits(int num) {
    int sum = 0;
    while (num != 0) {
        sum += num % 10;  // Extract the last digit and add to sum
        num /= 10;        // Remove the last digit
    }
    return sum;
}