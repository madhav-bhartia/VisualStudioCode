#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int number, guess, guess_count = 1;
    srand(time(0));
    number = rand() % 100 + 1; 

    // Uncomment this to see what the secret number is!
    // printf("%d\n", number);
    printf("Guess the number b/w 1 to 100.\n");
    do{
        printf("-> ");
        scanf("%d", &guess);
        if (guess < number){
            printf("Enter a higher number!\n");
        }
        else if (guess > number){
            printf("Enter a lower number!\n");
        }
        else{
            printf("Congratulations! :D\n");
            printf("You have guessed the number!\n");
            printf("Your score was %d.", guess_count);
        }
        guess_count++;
    } while (guess != number);

    return 0;
}