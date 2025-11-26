#include <stdio.h>
#include <math.h>

int main() {
    float radius, area, surfaceArea, volume = 0.0f;
    const float PI = 3.14159f;
    
    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);

    area = PI * radius * radius;
    surfaceArea = 4 * PI * radius * radius;
    volume = (4.0f / 3.0f) * PI * radius * radius * radius;

    printf("Area of the circle: %.2f\n", area);
    printf("Surface area of the sphere: %.2f\n", surfaceArea);
    printf("Volume of the sphere: %.2f\n", volume);

    return 0;
}