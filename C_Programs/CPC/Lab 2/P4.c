//find the slope of a line
#include <stdio.h>

int main(){
    float x = 0.0f, y = 0.0f;
    printf("Enter the coefficients of the line equation (a,b): ");
    scanf("%d,%d", &x, &y);
    if(y == 0){
        printf("The line is vertical, slope is undefined.\n");
    }
    else {
        float slope = -(x/y);
        printf("The slope of the line is: %.2f\n", slope);
    }

    return 0;
}