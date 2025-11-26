/*Write a function to convert a temperature from Celsius to Fahrenheit.
 Function Signature: float celsiusToFahrenheit(float celsius);
 Hint:
o Use the formula Fahrenheit = (Celsius * 9/5) + 32.
o Simply perform the calculation and return the result.*/
#include <stdio.h>

float celsiusToFahrenheit(float celsius);

int main() {
    float celsius;
    printf("Enter temperature in Celsius: ");
    scanf("%f", &celsius);
    float fahrenheit = celsiusToFahrenheit(celsius);
    printf("%.2f Celsius is equal to %.2f Fahrenheit.\n", celsius, fahrenheit);
    return 0;
}

float celsiusToFahrenheit(float celsius) {
    return (celsius * 9.0 / 5.0) + 32.0; // Convert Celsius to Fahrenheit
}