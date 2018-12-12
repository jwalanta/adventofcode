/*
 * Solution for https://adventofcode.com/2018/day/11
 *
 * Summation-area table method
 */

#include <stdio.h>

int sat[301][301];

int serial = 3999;

int power(int x, int y){ 
    int p;
    p = ( x + 10 ) * y + serial;
    p = p * (x+10);
    p  = ((p / 100) % 10) - 5;

    return p;
}


int main(){

    int x, y;

    /* compute summed-area table */
    for (x=0;x<=300;x++)
        for (y=0;y<=300;y++)
            if (x==0 || y==0)
                sat[x][y] = 0;
            else
                sat[x][y] = power(x,y) + sat[x-1][y] + sat[x][y-1] - sat[x-1][y-1];


    int max=0, maxx=0, maxy=0, size=0;
    int grid_size;
    int total;

    for (grid_size = 1; grid_size <= 300; grid_size++) {
        for (x = 1; x <= 301-grid_size; x++) {
            for (y = 1; y <= 301-grid_size; y++) {
				total = sat[x-1][y-1] + sat[x+grid_size-1][y+grid_size-1] - sat[x+grid_size-1][y-1] - sat[x-1][y+grid_size-1];
				if (total > max) {
					max = total;
					maxx = x;
					maxy = y;
					size = grid_size;
				}
			}
		}
	}

	printf("%d,%d,%d\n", maxx, maxy, size);

    return 0;
}