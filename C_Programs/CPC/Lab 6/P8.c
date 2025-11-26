#include <stdio.h>

int main(){
    int rows = 0;
    printf("Enter number of rows: ");
    scanf("%d", &rows);

    for(int i = 1; i <= rows; i++){
        for(int spaces = 1; spaces <= rows-i; spaces++){
            printf(" ");
        }
        for(int num = 1; num <= (2*i-1); num++){
            printf("%d", num);
        }
        printf("\n");
    }

    return 0;
}