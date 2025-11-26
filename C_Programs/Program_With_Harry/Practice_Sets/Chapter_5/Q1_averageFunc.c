#include <stdio.h>

float average(float, float, float);

int main()
{
    float num1, num2, num3, avg;
    printf("Enter 3 numbers to find thier average.\n");
    printf("Separate numbers by \" \" <space>\n-> ");
        scanf("%f %f %f", &num1, &num2, &num3);

    avg = average(num1, num2, num3);

    printf("The three numbers: %f, %f, %f\n", num1, num2, num3);
    printf("Average: %f\n", avg);

    return 0;
}

float average(float num1, float num2, float num3){
    return (num1 + num2 + num3) / 3;
}