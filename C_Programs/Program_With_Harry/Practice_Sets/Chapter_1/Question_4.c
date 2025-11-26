#include <stdio.h>

int main()
{

    float principal, years, rate_of_intrest, simple_intrest, amount;

    printf("Enter the Principle amount\n-> ");
    scanf("%f", &principal);

    printf("Enter the number of years\n-> ");
    scanf("%f", &years);

    printf("Enter the rate of intrest in percentage\n-> ");
    scanf("%f", &rate_of_intrest);

    simple_intrest = (principal * years * rate_of_intrest) / 100;
    amount = principal + simple_intrest;

    printf("The Simple Intrest is: %f\n", simple_intrest);
    printf("The Total Amount is: %f", amount);

    return 0;
}