#include <stdio.h>
#include <stdbool.h>

int main()
{
    int a = 0;
    float b = 0.0f;
    double c = 0.0;
    bool d = true;
    char e = 'A';

    printf("A: %d\n", a);
    printf("B: %.2f\n", b);
    printf("C: %.2lf\n", c);
    printf("D: %d\n", d);
    printf("E: %c\n", e);

    return 0;
}