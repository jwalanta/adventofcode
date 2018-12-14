/*
 * Solution for https://adventofcode.com/2018/day/14
 *
 * Part 1
 */

#include <stdio.h>
#include <stdlib.h>

#define NSIZE 1000000 /* enough space for scores */

int main(){

    int input = 505961;

    int *n = malloc(sizeof(int) * NSIZE);

    int e1 = 0, e2 = 1; /* initial positions for elf 1 & 2 */

    /* initial scores */
    int total_recipes = 2;
    n[0] = 3;
    n[1] = 7;

    int i, total;
    
    for (i = 0; i < NSIZE; i++){

        total = n[e1] + n[e2];

        if (total < 10){
            n[total_recipes++] = total;
            if (total_recipes == input+10) break;
        }
        else{
            n[total_recipes++] = total / 10;
            if (total_recipes == input+10) break;

            n[total_recipes++] = total % 10;
            if (total_recipes == input+10) break;
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

    /* print last 10 scores */
    for (i = total_recipes - 10; i < total_recipes; i++){
        printf("%d",n[i]);
    }
    printf("\n");
    
    free(n);

    return 0;
}
