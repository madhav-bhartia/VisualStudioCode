#include <stdio.h>

int main()   {

    float celsius, fahrenheit;
    printf("Enter the temperature in Celcius\n-> ");
    scanf("%f", &celsius);

    fahrenheit = celsius * (9.0 / 5.0) + 32.0;
    printf("The value in fahrenheits is: %f", fahrenheit);

    return 0;
}