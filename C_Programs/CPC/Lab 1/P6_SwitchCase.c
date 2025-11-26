#include <stdio.h>

void calc(float *a, float *b, float *result, char op)
{
    switch (op)
    {
    case '+':
        *result = *a + *b;
        break;
    case '-':
        *result = *a - *b;
        break;
    case '*':
        *result = (*a) * (*b);
        break;
    case '/':
        *result = (*b != 0) ? *a / *b : 0.0f;
        break;
    default:
        printf("Unknown operator\n");
        *result = 0.0f;
    }
}

int main()
{
    float x, y, result;
    char op;

    printf("Enter expression (e.g. 5.5 [+|-|*|/] 2.2): ");
    scanf("%f %c %f", &x, &op, &y);

    calc(&x, &y, &result, op);

    if (!(op == '/' && y == 0))
        printf("Result: %.2f\n", result);

    return 0;
}
