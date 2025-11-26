#include <stdio.h>

int main(){
    float a = 0.0f, b = 0.0f, c = 0.0f;
    float p = 0.0f, q = 0.0f, r = 0.0f;
    printf("Enter the a, b and c of the line equation (ax + by + c = 0) like (a,b,c): ");
    scanf("%f,%f,%f", &a, &b, &c);
    printf("Enter the p, q and r of the line equation (px + qy + r = 0) like (p,q,r): ");
    scanf("%f,%f,%f", &p, &q, &r);
    if ((a * q) - (b * p) == 0){
        printf("The lines are parallel.\n");
    } else {
        float x = ((b * r) - (c * q)) / ((a * q) - (b * p));
        float y = ((c * p) - (a * r)) / ((a * q) - (b * p));
        printf("The lines intersect at point (%.2f, %.2f).\n", x, y);
    }
    
    return 0;
}