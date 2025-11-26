#include <stdio.h>
int main()   {
    printf("Welcome to rectangle area calculator!\n");
    printf("Here is an example");

    int length_hard_coded, width_hard_coded, area_result_hard_coded;
    length_hard_coded = 2;
    width_hard_coded = 3;
    area_result_hard_coded = length_hard_coded * width_hard_coded;

    printf("The area of a rectangle containing the following dimensions!");
    printf("Length: %d\n", length_hard_coded);
    printf("Width: %d\n", width_hard_coded);
    printf("Area: %d\n", area_result_hard_coded);

    int length, width, area;

    printf("Enter the length of the rectangle\n-> ");
    scanf("%d", &length);

    printf("Enter the width of the rectangle\n-> ");
    scanf("%d", &width);

    area = length * width;

    printf("The area of the recatngle is %d", area);

    return 0;
}