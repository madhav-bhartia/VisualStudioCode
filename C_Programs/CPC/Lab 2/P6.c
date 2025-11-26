#include <stdio.h>
#include <math.h>

int main() {
    float a = 0.0f, b = 0.0f, c = 0.0f, radius = 0.0f, centerX = 0.0f, centerY = 0.0f;
    printf("Enter the coefficients of the circle equation (a,b,c): ");
    scanf("%f,%f,%f", &a, &b, &c);
    centerX = -a / 2; 
    centerY = -b / 2;
    radius = sqrt(((a*a)/4) + ((b*b)/4) - c);
    printf("The center of the circle is: (%.2f, %.2f)\n", centerX, centerY);
    printf("The radius of the circle is: %.2f\n", radius);

    return 0;
}