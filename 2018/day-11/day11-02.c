/*
 * Solution for https://adventofcode.com/2018/day/11
 *
 * Brute-force method
 */

#include <stdio.h>

int cell[301][301];

int power(int x, int y, int serial){
    
    int p;
    p = ( x + 10 ) * y + serial;
    p = p * (x+10);
    p  = ((p / 100) % 10) - 5;

    return p;
}

int power_grid_size(int x, int y, int size)  {
	int total = 0;
    int xx, yy;
	
    for (xx = x; xx < x+size; xx++) {
		for (yy = y; yy < y+size; yy++) {
			total += cell[xx][yy];
		}
	}
	return total;
}

int main(){

    int input = 3999;
    int xx, yy;

	for (xx = 1; xx <= 300; xx++) {
		for (yy = 1; yy <= 300; yy++) {
			cell[xx][yy] = power(xx, yy, input);
		}
	}

    int max=0, maxx=0, maxy=0, size=0;
    int grid_size;
    int total;

	for (grid_size = 1; grid_size <= 300; grid_size++) {
		printf("Computing for grid size = %d\n", grid_size);

        for (xx = 1; xx <= 301-grid_size; xx++) {
            for (yy = 1; yy <= 301-grid_size; yy++) {
				total = power_grid_size(xx, yy, grid_size);
				if (total > max) {
					max = total;
					maxx = xx;
					maxy = yy;
					size = grid_size;
				}
			}
		}
	}

	printf("%d,%d,%d\n", maxx, maxy, size);

    return 0;
}