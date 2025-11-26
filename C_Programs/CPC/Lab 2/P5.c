#include <stdio.h>
#include <math.h>

int main(){
    float a = 0.0f, b = 0.0f, c = 0.0f, x = 0.0f, y = 0.0f, distance = 0.0f;
    printf("Enter the coefficients of the line equation (a,b,c): ");
    scanf("%f,%f,%f", &a, &b, &c);
    printf("Enter the coordinates of the point (x,y): ");
    scanf("%f,%f", &x, &y);
    if(a == 0 && b == 0){
        printf("Invalid line equation.\n");
    } else {
        distance = (abs(a*x + b*y + c)) / (float)sqrt(a*a + b*b);
        printf("The distance the point from the line is: %.2f\n", distance);
    }
    
    return 0;
}