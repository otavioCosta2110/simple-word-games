#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char word[20], gap[20];
    int a, i, lives=7, cont=0;

    printf("This is a simple game of 'Hangman'.\nFirst, a person writes the word to be guessed, then the terminal automatically clears and another person tries to guess it.\n\n");

    printf("Enter the word to be guessed: ");
    fgets(word, 20, stdin);
    word[strcspn(word, "\n")] = 0;
    system("clear"); // use "cls" if on Windows
    char letter;

    for (a = 0; a < strlen(word); a++){
        gap[a]='_';
    }
    gap[a] = '\0';

    printf("Word has %d letters. \n", strlen(word));
    printf("Remaining lives: %d \n", lives);
    while(lives>0){

        printf("%s\n", gap);

        printf("\nEnter a letter: ");
        letter=getchar();
        getchar();
        printf("%c\n", letter);

        for (a = 0; a < strlen(word); a++){
            if (word[a]==letter){
                gap[a]=letter;
                cont++;
            }
        }
        if (cont==0){
            printf("You guessed a letter incorrectly!\n");
            lives--;
            printf("Remaining lives: %d \n", lives);
            cont=0;
        }
        else if (cont>0){
            printf("You guessed a letter\n");
            cont=0;
        }

        if (strcmp(word,gap) == 0) {
            printf("Congratulations, you won the game! \n");
            break;
        }

        if (lives==0){
            printf("You Lost :( \n");
            break;
        }
    }

    return 0;
}
