//area and perimeter of rectangle
#include <stdio.h>

void rectangPerimeter(int length, int breadth, int *perimeter) {*perimeter = 2 * (length + breadth);}

void rectangArea(int length, int breadth, int *area) {*area = length * breadth;}

int main() {
    int length = 0, breadth = 0, area = 0, perimeter = 0;
    printf("Enter length and breadth of rectangle (l,b): ");
    scanf("%d,%d", &length, &breadth);
    rectangArea(length, breadth, &area);
    rectangPerimeter(length, breadth, &perimeter);
    printf("Perimeter of rectangle = %d\n", perimeter);
    printf("Area of rectangle = %d\n", area);
    return 0;
}