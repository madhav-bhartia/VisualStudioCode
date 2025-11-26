#include <stdio.h>

float forceByGravity(float);

int main()
{
    float mass, weight;
    printf("Enter the mass (in Kgs).\n-> ");
    scanf("%f", &mass);
    weight = forceByGravity(mass);
    printf("The force exerted by gravity on the mass is: %fN\n", weight);

    return 0;
}

float forceByGravity(float mass)
{
    float g = 9.8, weight;
    weight = mass * g;
    return weight;
}