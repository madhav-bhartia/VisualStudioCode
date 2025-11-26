#include <stdio.h>

int main(){
    int n = 0, i = 0, lastEven = -1;
    printf("Enter the amount of numbers: ");
    scanf("%d", &n);
    int num[n];
    for(i = 0; i < n; i++){
        printf("Enter number %d: ", i + 1);
        scanf("%d", &num[i]);
    }
    for(i = 0; i < n; i++){
        int temp = num[i];
        if(temp % 2 == 0){lastEven = temp;}
    }
    if(lastEven != -1){
        printf("Last even number is: %d\n", lastEven);
        return 0;
    }
    else{
        printf("No even number found.\n");
    }
    return 0;
}