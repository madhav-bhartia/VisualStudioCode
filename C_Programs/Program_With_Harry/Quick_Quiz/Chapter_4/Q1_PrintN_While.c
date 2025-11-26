#include <stdio.h>

int main()
{
    int count = 0;
    while(count <= 20){
        if(count >= 10){
            printf("> %d\n",count);
        }
        count++;
    }

    return 0;
}