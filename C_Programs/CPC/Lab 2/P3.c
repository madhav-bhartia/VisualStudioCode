//find midpoint of a line segment
#include <stdio.h>

void midpoint(float *x1, float *y1, float *x2, float *y2) {
    float midX = (*x1 + *x2) / 2;
    float midY = (*y1 + *y2) / 2;
    printf("Midpoint of the line segment: (%.2f, %.2f)\n", midX, midY);
}

int main() {
    float x1 = 0, y1 = 0, x2 = 0, y2 = 0;
    printf("Enter the coordinates of the first point (x1,y1): ");
    scanf("%f,%f", &x1, &y1);
    printf("Enter the coordinates of the second point (x2,y2): ");
    scanf("%f,%f", &x2, &y2);
    midpoint(&x1, &y1, &x2, &y2);
    return 0;
}