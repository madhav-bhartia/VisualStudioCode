/*Write a function to find the sum of first N natural numbers.
 Function Signature: int sumOfNaturalNumbers(int n);
 Hint:
o Use a loop from 1 to n to add each number to the sum.
o Alternatively, use the formula sum = n * (n + 1) / 2 for efficiency.*/
#include <stdio.h>

int sumOfNaturalNumbers(int n);

int main() {
    int n;
    printf("Enter a positive integer N: ");
    scanf("%d", &n);
    if (n < 1) {
        printf("Please enter a positive integer greater than 0.\n");
    } else {
        int sum = sumOfNaturalNumbers(n);
        printf("The sum of the first %d natural numbers is: %d\n", n, sum);
    }
    return 0;
}

int sumOfNaturalNumbers(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;  // Add each number from 1 to n to sum
    }
    return sum;
}