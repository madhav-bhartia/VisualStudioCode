#include <stdio.h>
#include <math.h>

int main()
{
    float centerH = 0.0f, radius = 0.0f, vertLineX = 0.0f, chordLen = 0.0f;
    printf("Enter the center (h), radius of the circle(r) and the verticle line(x) [like(h,r,x)]: ");
    scanf("%f,%f,%f", &centerH, &radius, &vertLineX);
    float dist = fabs(vertLineX - centerH);
    chordLen = 2 * sqrt(radius * radius - dist * dist);
    printf("The length of the chord is: %.2f units.\n", chordLen);
    return 0;
}