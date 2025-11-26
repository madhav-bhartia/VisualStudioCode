#include <stdio.h>

float tempCtoF(float);

int main()
{
    float tempC, tempF;
    printf("Enter the temperature in degree celcius.\n-> ");
    scanf("%f", &tempC);
    tempF = tempCtoF(tempC);
    printf("The temperature in fahrenheit is: %f\n", tempF);

    return 0;
}

float tempCtoF(float tempC){
    float tempF;
    tempF = tempC * 9 / 5 + 32;
    return tempF;
}