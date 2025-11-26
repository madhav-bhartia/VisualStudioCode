#include <stdio.h>
#include <math.h>

void areaOfTriangle(float *a, float *b, float *c) {
    float s = ((*a) + (*b) + (*c)) / 2;
    float area = sqrt(s * (s - (*a)) * (s - (*b)) * (s - (*c)));
    printf("Area of the triangle: %.2f\n", area);
}

int main() {
    float x = 0, y = 0, z = 0;
    printf("Enter the lengths of the three sides of the triangle (x,y,z): ");
    scanf("%f,%f,%f", &x, &y, &z);
    areaOfTriangle(&x, &y, &z);
    return 0;
}