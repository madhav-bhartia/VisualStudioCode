#include <stdio.h>

void add(float *a, float *b, float *result) {*result = *a + *b;}

void subtract(float *a, float *b, float *result) {*result = *a - *b;}

void multiply(float *a, float *b, float *result) {*result = (*a) * (*b);}

void divide(float *a, float *b, float *result) {
    if (*b != 0) {*result = (float)(*a) / (float)(*b);}
    else{
        printf("Error: Division by zero\n");
        *result = 0; // or some error value
    }
}

int main() {
    float num1, num2, sum, difference, product, quotient;
    
    printf("Enter two floating-point numbers: ");
    scanf("%f,%f", &num1, &num2);
    
    add(&num1, &num2, &sum);
    subtract(&num1, &num2, &difference);
    multiply(&num1, &num2, &product);
    divide(&num1, &num2, &quotient);
    
    printf("Sum: %.2f\n", sum);
    printf("Difference: %.2f\n", difference);
    printf("Product: %.2f\n", product);
    printf("Quotient: %.2f\n", quotient);
}