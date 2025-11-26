#include <stdio.h>

int main()   {

    float sub1, sub2, sub3, total;   // Marks for 3 subjects.
    printf("Enter the marks of the 3 best subjects!");

    printf("Enter the marks of the first subject (Out of 100)\n-> ");
    scanf("%f", &sub1);
    printf("Enter the marks of the second subject (Out of 100)\n-> ");
    scanf("%f", &sub2);
    printf("Enter the marks of the third subject (Out of 100)\n-> ");
    scanf("%f", &sub3);
    total = (sub1 + sub2 + sub3)/3;
    // Not taking pecentage values... because
    // (x/100)*100 is x.

    total >= 40 && sub1 >= 33 && sub2 >= 33 && sub3 >= 33 ?\
          printf("You passed! Congratz :)"):\
          printf("You Failed! :(");
    // if (total >= 40 && sub1 >= 33 && sub2 >= 33 && sub3 >= 33)
    //     printf("You passes! Congratz :)");
    // else
    //     printf("You Failed! :(");

    return 0;
}