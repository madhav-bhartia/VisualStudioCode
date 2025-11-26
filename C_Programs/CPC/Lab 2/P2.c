//calculate distance between 2 points
#include <stdio.h>
#include <math.h>

void distance(float *x1, float *y1, float *x2, float *y2) {
    float dist = sqrt(pow((*x2 - *x1), 2) + pow((*y2 - *y1), 2));
    printf("Distance between the two points: %.2f\n", dist);
}

int main() {
    float x1 = 0, y1 = 0, x2 = 0, y2 = 0;
    printf("Enter the coordinates of the first point (x1,y1): ");
    scanf("%f,%f", &x1, &y1);
    printf("Enter the coordinates of the second point (x2,y2): ");
    scanf("%f,%f", &x2, &y2);
    distance(&x1, &y1, &x2, &y2);
    return 0;
}