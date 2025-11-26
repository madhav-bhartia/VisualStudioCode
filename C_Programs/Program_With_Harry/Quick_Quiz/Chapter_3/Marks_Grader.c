#include <stdio.h>

int main()
{

    int marks;
    printf("Enter your marks to calculate your grade.\n-> ");
    scanf("%d", &marks);

    if (marks > 90 && marks <= 100)
    {
        printf("Your grade is: A");
    }
    else if (marks > 80 && marks <= 90)
    {
        printf("Your grade is: B");
    }
    else if (marks > 70 && marks <= 80)
    {
        printf("Your grade is: C");
    }
    else if (marks > 60 && marks <= 70)
    {
        printf("Your grade is: D");
    }
    else if (marks >= 0 && marks <= 60)
    {
        printf("Your grade is: F");
    }
    else
    {
        printf("Unexpected Error!");
    }

    return 0;
}