//find the area and perimeter of a circle by reading its radius
#include <stdio.h>

int main(){
    float r = 0.0f;
    printf("Enter the radius of the circle: ");
    scanf("%f", &r);
    float perimeter = 2 * 3.14159 * r;
    printf("Perimeter: %.2f\n", perimeter);
    float area = 3.14159 * r * r;
    printf("Area: %.2f\n", area);
    return 0;
}