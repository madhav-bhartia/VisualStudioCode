#include <stdio.h>
#include <math.h>

int main() {
    float a = 0.0f, b = 0.0f, c = 0.0f;
    printf("Enter the sides (a,b,c): ");
    scanf("%f,%f,%f", &a, &b, &c);
    float cosA = (b*b + c*c - a*a) / (2 * b * c);
    float angleA = acos(cosA) * (180.0 / 3.14159);
    printf("The angle opposite to side a is: %.2f degrees\n", angleA);
    
    return 0;
}