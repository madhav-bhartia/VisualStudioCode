#include <stdio.h>

void celcius_to_fahrenheit()
{
    float celsius = 0.0f, fahrenheit = 0.0f;
    printf("Enter temperature in Celsius: ");
    scanf("%f", &celsius);
    fahrenheit = (celsius * 1.8f) + 32.0f;
    printf("%.2f Celsius = %.2f Fahrenheit\n", celsius, fahrenheit);
}

void fahrenheit_to_celcius()
{
    float fahrenheit = 0.0f, celsius = 0.0f;
    printf("Enter temperature in Fahrenheit: ");
    scanf("%f", &fahrenheit);
    celsius = (fahrenheit - 32.0f) / 1.8f;
    printf("%.2f Fahrenheit = %.2f Celsius\n", fahrenheit, celsius);
}

int main()
{
    printf("Temperature Conversion Program\n");
    celcius_to_fahrenheit();
    fahrenheit_to_celcius();

    return 0;
}