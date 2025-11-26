//Write a program which will print those numbers whose last digit is a multiple of 3. For example: 0, 3, 6, 9, 10, 13, 16, 19, 20, 23 …… (assuming till 100)
#include <stdio.h>

int main(){
    for(int i=0; i<100; i++){
        if((i%10)%3==0){
            printf("%d ", i);
        }
    }
    return 0;
}