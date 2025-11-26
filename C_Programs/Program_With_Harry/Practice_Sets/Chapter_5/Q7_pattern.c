#include <stdio.h>

int pattern(int);

int main(){
    int line, control = 1;
    printf("Enter the number of lines for this pattern!\n-> ");
    scanf("%d", &line);
    for(int i = 1; i <= line; i++){
        pattern(control);
        control += 2;
    }

    return 0;
}

int pattern(int control){
    for (int n = 1; n < control; n++)
        printf("* ");
    printf("*\n");
}

// Mine WORKS! :D
// What Harry did:


// #include <stdio.h>

// void star(int);

// int main()
// {
//     int n;
//     printf("Enter the number of lines for this pattern!\n-> ");
//     scanf("%d", &n);
//     star(n);
//     return 0;
// }

// void star(int n){
//     for (int i = 0; i < n; i++){
//         // print 2i + 1 stars!
//         for (int j = 0; j < (2 * i + 1); j++){
//             printf("*");
//         }
//         printf("\n");
//     }
// }