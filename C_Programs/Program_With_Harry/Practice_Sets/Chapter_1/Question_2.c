#include <stdio.h>

int main()   {

    float radius, area_circle;
    const float PI = 3.14159;
    printf("Enter the radius of the circle\n-> ");
    scanf("%f", &radius);
    area_circle = radius * radius * PI;
    printf("Area of the circle is: %f\n", area_circle);

    float height, area_cylinder;
    printf("Enter the height to calculate the area of the cylinder.\n");
    printf("(Formed with the circle as the base)\n-> ");
    scanf("%f", &height);
    area_cylinder = height * area_circle;
    printf("Area of the cylinder is: %f\n", area_cylinder);

    return 0;
}