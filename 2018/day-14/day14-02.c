/*
 * Solution for https://adventofcode.com/2018/day/14
 *
 * Part 2
 */

#include <stdio.h>
#include <stdlib.h>

#define NSIZE 1000000000  /* enough space for scores */

int match_input(int *recipes, int recipes_size, int *input, int input_size){
    int i;
    for (i = 0; i < input_size; i++){
        if (input[i] != recipes[recipes_size - input_size + i]){
            return 0;
        }
    }
    /* match */
    printf("%d\n", recipes_size - input_size);
    return 1;
}

int main(){

    int *n = malloc(sizeof(int) * NSIZE);

    int input[] = {5,0,5,9,6,1};
    int input_size = sizeof(input) / sizeof(int);

    int e1 = 0, e2 = 1; /* initial positions for elf 1 & 2 */

    /* initial scores */
    int total_recipes = 2;
    n[0] = 3;
    n[1] = 7;

    int i, j, total;
    int match;
    
    for (i = 0; i < NSIZE; i++){

        total = n[e1] + n[e2];

        if (total < 10){
            n[total_recipes++] = total;
            if (match_input(n, total_recipes, input, input_size)) break;
        }
        else{
            n[total_recipes++] = total / 10;
            if (match_input(n, total_recipes, input, input_size)) break;

            n[total_recipes++] = total % 10;
            if (match_input(n, total_recipes, input, input_size)) break;
        }

        e1 = (e1+1+n[e1]) % total_recipes;
        e2 = (e2+1+n[e2]) % total_recipes;

        /* print recipe scores */
        /*
        for (j=0;j<total_recipes;j++){
            if (j==e1){
                printf("(%d)",n[j]);
            }
            else if (j== e2){
                printf("[%d]",n[j]);
            }
            else{
                printf(" %d ",n[j]);
            }
        }
        printf("\n");
        */

    }

    free(n);

    return 0;
}
