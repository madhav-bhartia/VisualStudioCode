#include <stdio.h>
#include <math.h>

int main()
{
    double side, area;
    printf("Enter the value of side of square to find it's area.\n-> ");
    scanf("%lf", &side);
    area = pow(side, 2.0);
    printf("The area of the square is: %lf\n", area);

    return 0;
}