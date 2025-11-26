#include <stdio.h>

int main(){
    int rows = 0;
    printf("Enter number of rows: ");
    scanf("%d", &rows);

    for(int i = rows; i >= 1; i--){
        for(int spaces = rows-i; spaces >= 1; spaces--){
            printf(" ");
        }
        for(int num = 1; num <= (2*i-1); num++){
            printf("%d", num);
        }
        printf("\n");
    }

    return 0;
}