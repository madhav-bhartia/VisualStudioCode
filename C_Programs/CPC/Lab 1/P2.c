#include <stdio.h>
#include <string.h>

int main()
{
    char name[20] = "N/A";
    long long int phone_number = 0;

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0'; // Remove newline character if present
    printf("Enter your number: ");
    scanf("%lld", &phone_number);

    printf("Your name is %s and your number is %lld", name, phone_number);

    return 0;
}